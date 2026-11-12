import Link from "next/link";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { requireOwner, toTag } from "@/lib/owner";
import { TYPE_EMOJI } from "@/lib/finder";

async function Messages() {
  const { db } = await requireOwner();
  const { data: rets } = await db
    .from("returns")
    .select("id, tag_code, opened_at")
    .neq("state", "closed")
    .order("opened_at", { ascending: false });
  const codes = (rets ?? []).map((r) => r.tag_code);
  const { data: tags } = codes.length
    ? await db
        .from("tags")
        .select("code, state, product, type, items(name, photo_path)")
        .in("code", codes)
    : { data: [] };
  const byCode = new Map((tags ?? []).map((t) => [t.code, toTag(t as never)]));
  const last = new Map<string, string>();
  for (const r of rets ?? []) {
    const { data: m } = await db
      .from("messages")
      .select("body, sender")
      .eq("return_id", r.id)
      .order("created_at", { ascending: false })
      .limit(1)
      .maybeSingle();
    if (m)
      last.set(r.tag_code, (m.sender === "owner" ? "You: " : "Finder: ") + m.body.split("\n")[0]);
  }
  return (
    <AppScreen tab="messages">
      <h1>Messages</h1>
      {(rets ?? []).map((r) => {
        const t = byCode.get(r.tag_code);
        if (!t) return null;
        return (
          <Link key={r.id} href={`/my-tags/${t.code}/conversation`} className="item">
            <span className="ic">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              {t.photo ? <img src={t.photo} alt="" /> : t.type ? TYPE_EMOJI[t.type] : "🏷️"}
            </span>
            <span className="tx">
              <b>{t.name}</b>
              <span>{last.get(t.code) ?? "New report"}</span>
            </span>
          </Link>
        );
      })}
      {(rets ?? []).length === 0 && (
        <div className="empty">
          <span className="bell">💬</span>
          <p className="m">
            No messages yet. When someone finds one of your items, their message appears here.
          </p>
        </div>
      )}
      <p className="xs center">Messages are deleted 90 days after a return.</p>
    </AppScreen>
  );
}

export default function Page() {
  return (
    <Suspense fallback={<div className="app" />}>
      <Messages />
    </Suspense>
  );
}
