import "server-only";
import { parseCode } from "@tagkin/shared";
import { adminClient } from "./supabase/admin";
import { approximateCity, clientKey, isPerson } from "./request";

export type FinderPage =
  | { result: "not_a_code" | "check_the_code" | "not_found" | "rate_limited" }
  | { result: "inactive" | "not_set_up"; code: string }
  | {
      result: "ok";
      code: string;
      state: "normal" | "lost" | "return_active";
      type: "item" | "travel" | "pet";
      product: string;
      test: boolean;
      name: string;
      photo_path: string | null;
      message: string;
      has_care_notes: boolean;
      temperament: string[] | null;
      trip: { mode: string; carrier: string; destination: string } | null;
      status: string | null;
    };

/** Finder lookup: rate-limited, server-only (audit 12 Nov, finding 4). Records a scan for real visitors. */
export async function loadFinderPage(input: string, countScan = true): Promise<FinderPage> {
  const parsed = parseCode(input);
  if (!parsed.ok) return { result: parsed.reason === "check" ? "check_the_code" : "not_a_code" };
  const db = adminClient();
  const { data: allowed } = await db.rpc("check_rate_limit", {
    p_key: await clientKey("lookup"),
    p_max: 60,
    p_window_seconds: 3600,
  });
  if (!allowed) return { result: "rate_limited" };
  const { data, error } = await db.rpc("get_finder_page", { p_input: parsed.code });
  if (error || !data) throw new Error("finder_lookup_failed");
  const page = data as unknown as FinderPage;
  if (countScan && page.result === "ok" && (await isPerson())) {
    await db.rpc("record_scan", {
      p_code: parsed.code,
      p_city: (await approximateCity()) ?? "",
      p_ua_class: "person",
    });
  }
  return page;
}

export const TYPE_EMOJI = { item: "🎒", travel: "🧳", pet: "🐾" } as const;
