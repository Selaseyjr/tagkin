"use server";

import { revalidatePath } from "next/cache";
import { adminClient } from "@/lib/supabase/admin";
import { clientKey, hashToken } from "@/lib/request";

export async function finderReply(token: string, form: FormData) {
  const body = String(form.get("body") ?? "").trim();
  if (!body || body.length > 1000) return;
  const db = adminClient();
  const { data: allowed } = await db.rpc("check_rate_limit", {
    p_key: await clientKey("reply"),
    p_max: 30,
    p_window_seconds: 3600,
  });
  if (!allowed) return;
  await db.rpc("finder_reply", { p_token_hash: hashToken(token), p_body: body });
  revalidatePath(`/r/${token}`);
}
