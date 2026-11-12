import "server-only";
import { adminClient } from "./supabase/admin";
import { hashToken } from "./request";

export type ReportView = {
  code: string;
  item: string | null;
  care_notes: string | null;
  return_state: "open" | "handed_over" | "closed";
  messages: { from: "owner" | "finder" | "system"; body: string; at: string }[];
};

export async function loadReport(token: string): Promise<ReportView | null> {
  if (!/^[A-Za-z0-9_-]{20,64}$/.test(token)) return null;
  const { data } = await adminClient().rpc("get_report_view", { p_token_hash: hashToken(token) });
  return (data as unknown as ReportView) ?? null;
}
