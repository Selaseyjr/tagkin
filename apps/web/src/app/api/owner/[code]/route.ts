import { NextResponse } from "next/server";
import { ownerClient } from "@/lib/supabase/server";

// Live conversation for the owner's tag page (row-level security limits it to the owner's own returns).
export async function GET(_req: Request, ctx: { params: Promise<{ code: string }> }) {
  const { code } = await ctx.params;
  const db = await ownerClient();
  const { data: ret } = await db
    .from("returns")
    .select("id")
    .eq("tag_code", code)
    .neq("state", "closed")
    .maybeSingle();
  if (!ret)
    return NextResponse.json({ messages: [] }, { headers: { "Cache-Control": "no-store" } });
  const { data } = await db
    .from("messages")
    .select("sender, body, created_at")
    .eq("return_id", ret.id)
    .order("created_at");
  return NextResponse.json(
    { messages: (data ?? []).map((m) => ({ from: m.sender, body: m.body, at: m.created_at })) },
    { headers: { "Cache-Control": "no-store" } },
  );
}
