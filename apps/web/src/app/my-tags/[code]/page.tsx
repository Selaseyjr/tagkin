import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { typesFor, type Product } from "@tagkin/shared";
import { Shell } from "@/components/Shell";
import { OwnerBar } from "@/components/OwnerBar";
import { requireOwner, STATE_LABEL } from "@/lib/owner";
import { TYPE_EMOJI } from "@/lib/finder";
import { markFound, markLost, markReturned, ownerReply, setUpBlank } from "./actions";
import { OwnerThread } from "./OwnerThread";
import { SetUpForm } from "./SetUpForm";
import { TagQr } from "@/components/TagQr";

async function TagDetail({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { db } = await requireOwner();
  const { data: tag } = await db
    .from("tags")
    .select("code, state, product, type, items(name, photo_path, finder_message)")
    .eq("code", code)
    .maybeSingle();
  if (!tag) notFound();
  const item = Array.isArray(tag.items) ? tag.items[0] : tag.items;
  const label = STATE_LABEL[tag.state] ?? STATE_LABEL.normal!;

  if (tag.state === "unlinked") {
    return (
      <>
        <OwnerBar />
        <span className={label.cls} style={{ alignSelf: "flex-start" }}>
          {label.text}
        </span>
        <h1>Set up {tag.code}</h1>
        <p className="m">
          Blank {tag.product.replace("_", " ")}. Link it to something; only types that fit this
          shape are offered.
        </p>
        <SetUpForm
          types={typesFor(tag.product as Product)}
          action={setUpBlank.bind(null, tag.code, tag.product)}
        />
      </>
    );
  }

  const { data: ret } = await db
    .from("returns")
    .select("id")
    .eq("tag_code", code)
    .neq("state", "closed")
    .maybeSingle();
  const { data: msgs } = ret
    ? await db
        .from("messages")
        .select("sender, body, created_at")
        .eq("return_id", ret.id)
        .order("created_at")
    : { data: [] };
  const { data: scans } = await db
    .from("scans")
    .select("at, city, is_test, report_id")
    .eq("tag_code", code)
    .order("at", { ascending: false })
    .limit(8);

  return (
    <>
      <OwnerBar />
      {item?.photo_path ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          className="photo"
          src={item.photo_path}
          alt=""
          style={{ objectFit: "cover", width: "100%" }}
        />
      ) : (
        <div className="photo">{tag.type ? TYPE_EMOJI[tag.type] : "🏷️"}</div>
      )}
      <div className="row" style={{ justifyContent: "space-between" }}>
        <h1>{item?.name}</h1>
        <span className={label.cls}>{label.text}</span>
      </div>
      <p className="xs">
        {tag.code} · <Link href={`/${tag.code}`}>Open its finder page</Link>
      </p>

      {tag.state === "return_active" && (
        <div className="card">
          <h2>A finder reported it</h2>
          <p className="xs">
            🔒 Name and photo are locked until the return ends, so the finder sees what they expect.
          </p>
          <OwnerThread
            code={tag.code}
            initial={(msgs ?? []).map((m) => ({ from: m.sender, body: m.body, at: m.created_at }))}
            reply={ownerReply.bind(null, tag.code)}
          />
          <form action={markReturned.bind(null, tag.code)}>
            <button className="btn btn-sec">Got it back? Mark as returned</button>
          </form>
        </div>
      )}
      {tag.state === "normal" && (
        <form action={markLost.bind(null, tag.code)} className="opts">
          <button className="btn btn-lost">Mark as lost</button>
          <p className="xs">
            Finders then see “This item is missing”, and every scan alerts you with the city.
          </p>
        </form>
      )}
      {tag.state === "lost" && (
        <form action={markFound.bind(null, tag.code)}>
          <button className="btn btn-pri">I found it myself</button>
        </form>
      )}

      <TagQr code={tag.code} />

      <div className="card">
        <h2>Scan history</h2>
        {(scans ?? []).length === 0 && <p className="m">No scans yet.</p>}
        {(scans ?? []).map((s, i) => (
          <div key={i} className="li">
            <span>
              {new Date(s.at).toLocaleString([], {
                day: "numeric",
                month: "short",
                hour: "2-digit",
                minute: "2-digit",
              })}
              {s.report_id ? " · report" : s.is_test ? " · test" : ""}
            </span>
            <span className="m">{s.city ?? "Location unknown"}</span>
          </div>
        ))}
        <p className="xs">City only, never an exact place unless a finder shares it.</p>
      </div>
    </>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Shell>
      <Suspense fallback={<p className="m center">Loading…</p>}>
        <TagDetail params={params} />
      </Suspense>
    </Shell>
  );
}
