import { notFound } from "next/navigation";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag } from "@/lib/owner";
import { markReturned, ownerReply } from "../actions";

async function finish(code: string, form: FormData) {
  "use server";
  if (String(form.get("body") ?? "").trim()) await ownerReply(code, form);
  await markReturned(code);
}

async function Returned({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { tag } = await loadTag(code);
  if (!tag) notFound();
  return (
    <AppScreen
      back={{ href: `/my-tags/${code}/conversation` }}
      right={<span className="badge b-r">Return active</span>}
    >
      <h1>Got it back?</h1>
      <p className="m">
        Locks lift and the tag goes back to Active. The return also closes on its own after 14 days
        with no messages.
      </p>
      <form action={finish.bind(null, code)} className="grp" style={{ flex: 1 }}>
        <textarea
          className="in"
          name="body"
          maxLength={1000}
          placeholder="Private thank-you (optional)"
          aria-label="Private thank-you"
        />
        <div className="sp" />
        <button className="btn pri">Mark as returned</button>
      </form>
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <Returned params={params} />
    </Suspense>
  );
}
