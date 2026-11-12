import { NextResponse } from "next/server";
import { loadReport } from "@/lib/report";

// Polled by the finder's report page for live owner replies. Token-scoped; no owner details.
export async function GET(_req: Request, ctx: { params: Promise<{ token: string }> }) {
  const { token } = await ctx.params;
  const view = await loadReport(token);
  if (!view) return NextResponse.json({ error: "not_found" }, { status: 404 });
  return NextResponse.json(
    { messages: view.messages, return_state: view.return_state },
    { headers: { "Cache-Control": "no-store" } },
  );
}
