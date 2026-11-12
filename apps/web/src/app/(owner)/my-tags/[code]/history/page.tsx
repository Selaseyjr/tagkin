import { notFound } from "next/navigation";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag, when } from "@/lib/owner";

async function History({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { db, tag } = await loadTag(code);
  if (!tag) notFound();
  const { data: scans } = await db
    .from("scans")
    .select("at, city, is_test, report_id")
    .eq("tag_code", code)
    .order("at", { ascending: false })
    .limit(30);
  return (
    <AppScreen back={{ href: `/my-tags/${code}`, label: tag.name }}>
      <h1>Scan history</h1>
      <p className="m">
        {tag.name} · {tag.code}
      </p>
      <div>
        {(scans ?? []).map((s, i) => (
          <div key={i} className="li">
            <span>
              {when(s.at)}
              <br />
              <small className="xs">
                {s.report_id ? "Report sent" : s.is_test ? "Test scan" : "Viewed, no report"}
              </small>
            </span>
            <span>{s.city ?? "Location unknown"}</span>
          </div>
        ))}
        {(scans ?? []).length === 0 && (
          <p className="note info">
            No scans yet. Open the QR code and scan it with another phone to test it.
          </p>
        )}
      </div>
      <p className="xs">
        City only, unless a finder shared the item location. History is deleted with the tag.
      </p>
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <History params={params} />
    </Suspense>
  );
}
