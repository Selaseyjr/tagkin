import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { Suspense } from "react";
import { Priv, Shell } from "@/components/Shell";
import { loadFinderPage, TYPE_EMOJI } from "@/lib/finder";

async function TagPage({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  if (!/^tk/i.test(code)) notFound();
  const page = await loadFinderPage(code);

  if (["not_a_code", "check_the_code", "not_found", "rate_limited"].includes(page.result)) {
    redirect(`/find?e=${page.result}`);
  }
  if (page.result === "inactive") {
    return (
      <>
        <h1 className="center">This tag is no longer active.</h1>
        <p className="m center">Please hand the item to staff or a lost-and-found desk.</p>
        <Link className="btn btn-sec" href="/find">
          Enter another code
        </Link>
      </>
    );
  }
  if (page.result === "not_set_up") {
    return (
      <>
        <h1 className="center">This tag isn&apos;t set up yet.</h1>
        <p className="m center">
          If you found it on something, please hand it to staff or a lost-and-found desk.
        </p>
        <p className="xs center">Is this your tag? Set it up in the Tagkin app.</p>
      </>
    );
  }
  if (page.result !== "ok") return null;
  const lost = page.state === "lost";
  return (
    <>
      {page.test && (
        <p className="note warn">
          Test scan · The owner is testing this tag. Nothing you send here reaches anyone.
        </p>
      )}
      {lost && <p className="urgent">! This item is missing</p>}
      {page.trip && (
        <div className="card">
          <b>✈️ I&apos;m travelling to {page.trip.destination}</b>
          <span className="xs">With {page.trip.carrier}</span>
          {page.status && <span className="badge ret">Owner update: {page.status}</span>}
        </div>
      )}
      {page.photo_path ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          className="photo"
          src={page.photo_path}
          alt={page.name}
          style={{ objectFit: "cover", width: "100%" }}
        />
      ) : (
        <div className="photo" aria-hidden="true">
          {TYPE_EMOJI[page.type]}
        </div>
      )}
      {lost && <h2>{page.name}</h2>}
      <h1>{page.message}</h1>
      {page.temperament && (
        <div className="chips">
          {page.temperament.map((t) => (
            <span key={t} className="badge">
              {t}
            </span>
          ))}
        </div>
      )}
      {page.has_care_notes && (
        <p className="note">
          This pet has care notes. They&apos;re shared with you once you report where they are.
        </p>
      )}
      {page.state === "return_active" && (
        <p className="note ok">
          Someone already reported this. If you have it, you can still tell the owner.
        </p>
      )}
      <Link className="btn btn-pri" href={`/${page.code}/report`}>
        I found it
      </Link>
      <Priv />
    </>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Shell>
      <Suspense fallback={<p className="m center">Loading…</p>}>
        <TagPage params={params} />
      </Suspense>
    </Shell>
  );
}
