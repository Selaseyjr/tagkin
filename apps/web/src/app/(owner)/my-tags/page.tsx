import Link from "next/link";
import { Suspense } from "react";
import { AppScreen, QrIcon } from "@/components/app/AppScreen";
import { hasOpenReturn, requireOwner, STATE_BADGE, toTag } from "@/lib/owner";
import { TYPE_EMOJI } from "@/lib/finder";

async function MyTags() {
  const { db } = await requireOwner();
  const { data } = await db
    .from("tags")
    .select("code, state, product, type, items(name, photo_path)")
    .neq("state", "retired")
    .order("created_at");
  const tags = (data ?? []).map((r) => toTag(r as never));
  const unread = await hasOpenReturn();
  return (
    <AppScreen tab="tags" unread={unread}>
      <h1>My tags</h1>
      {tags.map((t) => {
        const b = STATE_BADGE[t.state] ?? STATE_BADGE.normal!;
        const sub =
          t.state === "unlinked"
            ? `${t.code} · tap to set up`
            : !t.photo
              ? `${t.code} · add a photo`
              : t.code;
        return (
          <div key={t.code} className="item">
            <Link
              href={`/my-tags/${t.code}`}
              className="row-link"
              style={{
                display: "flex",
                gap: 12,
                alignItems: "center",
                flex: 1,
                minWidth: 0,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              <span className="ic">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                {t.photo ? <img src={t.photo} alt="" /> : t.type ? TYPE_EMOJI[t.type] : "🏷️"}
              </span>
              <span className="tx">
                <b>{t.name}</b>
                <span>{sub}</span>
              </span>
              <span className={b.cls}>{b.text}</span>
            </Link>
            {t.state !== "unlinked" && (
              <Link
                href={`/my-tags/${t.code}/qr`}
                className="qrb"
                aria-label={`Show QR code for ${t.name}`}
              >
                <QrIcon />
              </Link>
            )}
          </div>
        );
      })}
      {tags.length === 0 && (
        <div className="empty">
          <span className="bell">🏷️</span>
          <p className="m">No tags yet.</p>
        </div>
      )}
    </AppScreen>
  );
}

export default function Page() {
  return (
    <Suspense fallback={<div className="app" />}>
      <MyTags />
    </Suspense>
  );
}
