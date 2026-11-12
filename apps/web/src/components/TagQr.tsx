import QRCode from "qrcode";
import { displayUrl, qrUrl } from "@tagkin/shared";

/** The tag's QR, exactly as printed: permanent capitalised address (rule 4.1). */
export async function TagQr({ code }: { code: string }) {
  const svg = await QRCode.toString(qrUrl(code), {
    type: "svg",
    errorCorrectionLevel: "Q",
    margin: 2,
  });
  const download = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
  return (
    <div className="card">
      <h2>QR code</h2>
      <div className="qr" dangerouslySetInnerHTML={{ __html: svg }} />
      <p className="xs center">{displayUrl(code)}</p>
      <a className="btn btn-sec" href={download} download={`${code}.svg`}>
        Save QR image
      </a>
      <p className="xs">Scan it with another phone to see exactly what a finder sees.</p>
    </div>
  );
}
