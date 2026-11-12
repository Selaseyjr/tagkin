import QRCode from "qrcode";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { displayUrl, qrUrl } from "@tagkin/shared";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag } from "@/lib/owner";
import { ShareButton } from "./ShareButton";

async function Qr({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { tag } = await loadTag(code);
  if (!tag) notFound();
  const svg = await QRCode.toString(qrUrl(tag.code), {
    type: "svg",
    errorCorrectionLevel: "Q",
    margin: 1,
  });
  return (
    <AppScreen back={{ href: `/my-tags/${code}`, label: tag.name }}>
      <h1>{tag.name}</h1>
      <div className="bigqr">
        <div dangerouslySetInnerHTML={{ __html: svg }} />
        <small>{displayUrl(tag.code).replace("/", " · ")}</small>
      </div>
      <p className="m center">Scan it with another phone to see exactly what a finder sees.</p>
      <div className="sp" />
      <div className="two">
        <a
          className="btn sec"
          href={`data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`}
          download={`${tag.code}.svg`}
        >
          Save image
        </a>
        <ShareButton url={`https://${displayUrl(tag.code)}`} title={tag.name} />
      </div>
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <Qr params={params} />
    </Suspense>
  );
}
