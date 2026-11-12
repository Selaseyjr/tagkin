import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { typesFor, type Product } from "@tagkin/shared";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag, STATE_BADGE } from "@/lib/owner";
import { TYPE_EMOJI } from "@/lib/finder";
import { markFound, setUpBlank } from "./actions";
import { SetUpForm } from "./SetUpForm";

function Photo({
  name,
  photo,
  emoji,
  locked,
}: {
  name: string;
  photo: string | null;
  emoji: string;
  locked?: boolean;
}) {
  return (
    <div className={locked ? "photo sm lockedp" : "photo sm"}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      {photo ? <img src={photo} alt={name} /> : emoji}
      {locked && <small>🔒 Locked during the return</small>}
    </div>
  );
}

async function Detail({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { db, tag } = await loadTag(code);
  if (!tag) notFound();
  const badge = STATE_BADGE[tag.state] ?? STATE_BADGE.normal!;
  const emoji = tag.type ? TYPE_EMOJI[tag.type] : "🏷️";
  const right = <span className={badge.cls}>{badge.text}</span>;
  const back = { href: "/my-tags", label: "My tags" };

  if (tag.state === "unlinked") {
    return (
      <AppScreen back={back} right={right}>
        <h1>Set up {tag.code}</h1>
        <p className="m">Blank {tag.product.replace("_", " ")}. What will it go on?</p>
        <SetUpForm
          types={typesFor(tag.product as Product)}
          action={setUpBlank.bind(null, tag.code, tag.product)}
        />
      </AppScreen>
    );
  }

  const { count: scans } = await db
    .from("scans")
    .select("id", { count: "exact", head: true })
    .eq("tag_code", code);
  const scanLabel = scans ? `${scans} scan${scans === 1 ? "" : "s"} ›` : "None yet ›";

  if (tag.state === "lost") {
    const { data: tagRow } = await db.from("tags").select("lost_at").eq("code", code).single();
    const { data: since } = await db
      .from("scans")
      .select("at, city")
      .eq("tag_code", code)
      .gte("at", tagRow?.lost_at ?? new Date(0).toISOString())
      .order("at", { ascending: false })
      .limit(6);
    return (
      <AppScreen back={back} right={right}>
        <Photo name={tag.name} photo={tag.photo} emoji={emoji} />
        <h1>{tag.name}</h1>
        <p className="m">Scans since marked lost</p>
        <div>
          {(since ?? []).map((s, i) => (
            <div key={i} className="li">
              <span>
                {new Date(s.at).toLocaleString("en-GB", {
                  weekday: "short",
                  hour: "2-digit",
                  minute: "2-digit",
                })}
              </span>
              <span>{s.city ?? "Location unknown"}</span>
            </div>
          ))}
          {(since ?? []).length === 0 && (
            <p className="note info">
              No scans since you marked it lost. You get an alert the moment someone scans it.
            </p>
          )}
        </div>
        <p className="xs">City only, unless a finder shares the item location.</p>
        <Link className="li" href={`/my-tags/${code}/qr`}>
          <span>QR code</span>
          <span>›</span>
        </Link>
        <div className="sp" />
        <form action={markFound.bind(null, code)}>
          <button className="btn pri">I found it myself</button>
        </form>
      </AppScreen>
    );
  }

  if (tag.state === "return_active") {
    return (
      <AppScreen back={back} right={right}>
        <Photo name={tag.name} photo={tag.photo} emoji={emoji} locked />
        <h1>{tag.name}</h1>
        <p className="lockrow">
          🔒 Name, photo and description are locked until the return ends, so the finder sees what
          they expect.
        </p>
        <div>
          <Link className="li" href={`/my-tags/${code}/qr`}>
            <span>QR code</span>
            <span>›</span>
          </Link>
          <Link className="li" href={`/my-tags/${code}/history`}>
            <span>Scan history</span>
            <span>{scanLabel}</span>
          </Link>
        </div>
        <div className="sp" />
        <Link className="btn pri" href={`/my-tags/${code}/conversation`}>
          Open conversation
        </Link>
      </AppScreen>
    );
  }

  return (
    <AppScreen back={back} right={right}>
      <Photo name={tag.name} photo={tag.photo} emoji={emoji} />
      <h1>{tag.name}</h1>
      <div>
        <Link className="li" href={`/my-tags/${code}/qr`}>
          <span>QR code and test scan</span>
          <span>›</span>
        </Link>
        <Link className="li" href={`/my-tags/${code}/history`}>
          <span>Scan history</span>
          <span>{scanLabel}</span>
        </Link>
      </div>
      <div className="sp" />
      <Link className="btn lostb" href={`/my-tags/${code}/lost`}>
        Mark as lost
      </Link>
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <Detail params={params} />
    </Suspense>
  );
}
