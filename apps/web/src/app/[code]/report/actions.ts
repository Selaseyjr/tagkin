"use server";

import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { z } from "zod";
import { parseCode } from "@tagkin/shared";
import { adminClient } from "@/lib/supabase/admin";
import { clientKey, hashToken, newToken } from "@/lib/request";

const CONTACT = /(\+?\d[\d\s\-()/]{6,}\d)|([^\s@]+@[^\s@]+\.[^\s@]+)/;

const schema = z.object({
  code: z.string(),
  where: z.enum(["with_me", "staff", "safe_place"]),
  place: z.string().trim().min(2).max(200),
  note: z.string().trim().max(500).optional(),
  email: z.union([z.email(), z.literal("")]).optional(),
  shareOk: z.string().optional(),
});

export type ReportState = {
  error?: string;
  needsShareOk?: boolean;
  values?: Record<string, string>;
  attempt?: number;
};

export async function submitReport(prev: ReportState, form: FormData): Promise<ReportState> {
  const raw = Object.fromEntries(form) as Record<string, string>;
  const keep = { values: raw, attempt: (prev.attempt ?? 0) + 1 };
  const parsed = schema.safeParse(raw);
  if (!parsed.success) {
    const field = parsed.error.issues[0]?.path[0];
    return {
      ...keep,
      error:
        field === "where"
          ? "Choose where the item is now."
          : field === "place"
            ? "Tell the owner where exactly (at least 2 characters)."
            : field === "email"
              ? "Check the email address, or leave it empty."
              : "Please check the form.",
    };
  }
  const v = parsed.data;
  const code = parseCode(v.code);
  if (!code.ok) return { ...keep, error: "This tag code is not valid." };
  if (v.note && CONTACT.test(v.note) && !v.shareOk) {
    return {
      needsShareOk: true,
      error: "Your note contains a phone number or email. It will be shared with the owner.",
    };
  }

  const db = adminClient();
  const { data: allowed } = await db.rpc("check_rate_limit", {
    p_key: await clientKey("report"),
    p_max: 10,
    p_window_seconds: 3600,
  });
  if (!allowed)
    return { ...keep, error: "Too many reports from this device. Please wait a while." };

  const token = newToken();
  const { error } = await db.rpc("submit_report", {
    p_code: code.code,
    p_where: v.where,
    p_place: v.place,
    p_note: v.note ?? "",
    p_contact_email: v.email ?? "",
    p_lang: "en",
    p_token_hash: hashToken(token),
  });
  if (error) return { ...keep, error: "This tag can't take reports right now." };

  // Remember the report on this device, so scanning the tag again reopens it (TK-16).
  (await cookies()).set(`tk_r_${code.code}`, token, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    path: "/",
    maxAge: 60 * 60 * 24 * 30,
  });
  redirect(`/r/${token}`);
}
