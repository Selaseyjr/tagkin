import { redirect } from "next/navigation";
import { Suspense } from "react";
import { Priv, Shell } from "@/components/Shell";
import { loadFinderPage } from "@/lib/finder";
import { ReportForm } from "./ReportForm";

async function Report({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const page = await loadFinderPage(code, false);
  if (page.result !== "ok") redirect(`/${code}`);
  return (
    <>
      <h1>Tell the owner where it is</h1>
      <ReportForm code={page.code} name={page.name} />
      <Priv />
    </>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Shell>
      <Suspense fallback={<p className="m center">Loading…</p>}>
        <Report params={params} />
      </Suspense>
    </Shell>
  );
}
