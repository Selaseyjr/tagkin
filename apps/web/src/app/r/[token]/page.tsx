import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { Priv, Shell } from "@/components/Shell";
import { loadReport } from "@/lib/report";
import { finderReply } from "./actions";
import { Thread } from "./Thread";

async function ReportPage({ params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  const view = await loadReport(token);
  if (!view) notFound();
  if (view.return_state === "closed") {
    return (
      <>
        <div className="done" aria-hidden="true">
          ✓
        </div>
        <h1 className="center">{view.item ?? "The item"} is back with its owner.</h1>
        <p className="m center">Thank you for helping. This conversation is closed.</p>
        <p className="note ok">
          Protect your own things: Tagkin tags help honest finders like you return them.
        </p>
        <Link className="btn btn-sec" href="/">
          Discover Tagkin
        </Link>
      </>
    );
  }
  return (
    <>
      <div className="done" aria-hidden="true">
        ✓
      </div>
      <h1 className="center">Thank you. The owner has been told.</h1>
      <p className="m center">
        Keep this page open to see their reply, or save its link to come back later.
      </p>
      {view.care_notes && (
        <details className="card">
          <summary>
            <b>Care notes from the owner</b>
          </summary>
          <p className="m">{view.care_notes}</p>
        </details>
      )}
      <Thread token={token} initial={view.messages} reply={finderReply.bind(null, token)} />
      <p className="xs center">
        Your report link is this page&apos;s address. Anyone with it can read this conversation, so
        keep it to yourself.
      </p>
      <Priv />
    </>
  );
}

export default function Page({ params }: { params: Promise<{ token: string }> }) {
  return (
    <Shell>
      <Suspense fallback={<p className="m center">Loading…</p>}>
        <ReportPage params={params} />
      </Suspense>
    </Shell>
  );
}
