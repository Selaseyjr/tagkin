import Link from "next/link";
import { Suspense } from "react";
import { Shell } from "@/components/Shell";
import { OwnerBar } from "@/components/OwnerBar";
import { requireOwner, STATE_LABEL } from "@/lib/owner";
import { TYPE_EMOJI } from "@/lib/finder";

async function TagList() {
  const { db } = await requireOwner();
  const { data: tags } = await db
    .from("tags")
    .select("code, state, product, type, items(name, photo_path)")
    .neq("state", "retired")
    .order("created_at", { ascending: true });
  return (
    <>
      <OwnerBar />
      <h1>My tags</h1>

      <div className="opts">
        {(tags ?? []).map((t) => {
          const item = Array.isArray(t.items) ? t.items[0] : t.items;
          const label = STATE_LABEL[t.state] ?? STATE_LABEL.normal!;
          return (
            <Link
              key={t.code}
              href={`/my-tags/${t.code}`}
              className="opt"
              style={{ textDecoration: "none", color: "inherit" }}
            >
              {item?.photo_path ? (
                // eslint-disable-next-line @next/next/no-img-element
                <img
                  src={item.photo_path}
                  alt=""
                  width={48}
                  height={48}
                  style={{ borderRadius: 12, objectFit: "cover" }}
                />
              ) : (
                <span
                  style={{
                    width: 48,
                    height: 48,
                    display: "grid",
                    placeItems: "center",
                    fontSize: 24,
                  }}
                >
                  {t.type ? TYPE_EMOJI[t.type] : "🏷️"}
                </span>
              )}
              <span style={{ flex: 1 }}>
                <b>{item?.name ?? `Blank ${t.product.replace("_", " ")}`}</b>
                <br />
                <span className="xs">{t.code}</span>
              </span>
              <span className={label.cls}>{label.text}</span>
            </Link>
          );
        })}
        {(tags ?? []).length === 0 && <p className="m">No tags yet.</p>}
      </div>
    </>
  );
}

export default function MyTags() {
  return (
    <Shell>
      <Suspense fallback={<p className="m center">Loading…</p>}>
        <TagList />
      </Suspense>
    </Shell>
  );
}
