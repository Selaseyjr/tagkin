import { notFound } from "next/navigation";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag } from "@/lib/owner";
import { markLost } from "../actions";

async function ConfirmLost({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { tag } = await loadTag(code);
  if (!tag) notFound();
  return (
    <AppScreen back={{ href: `/my-tags/${code}` }}>
      <h1>Mark {tag.name} as lost?</h1>
      <p className="m">
        Finders see an urgent page. You get an alert with the city every time it is scanned.
      </p>
      <p className="note info">
        🔓 Everything stays editable while it&apos;s lost. Name and photo lock only once a finder
        reports it.
      </p>
      <p className="note info">
        No reward amount is shown. You can thank the finder privately later.
      </p>
      <div className="sp" />
      <form action={markLost.bind(null, code)}>
        <button className="btn lostb">Mark as lost</button>
      </form>
      <a className="btn sec" href={`/my-tags/${code}`}>
        Cancel
      </a>
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <ConfirmLost params={params} />
    </Suspense>
  );
}
