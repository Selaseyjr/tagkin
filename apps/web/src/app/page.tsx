import Link from "next/link";
import { Shell } from "@/components/Shell";

const DEMO = [
  { code: "TK-D3M7-BKPB", label: "Black backpack", note: "Everyday item" },
  { code: "TK-D3M7-PTGR", label: "Milo the dog", note: "Marked as lost" },
  { code: "TK-D3M7-TRVS", label: "Blue suitcase", note: "Travelling to Accra" },
  { code: "TK-D3M7-KYC4", label: "Blank keychain", note: "Not set up yet" },
];

// Day 1 landing; the full landing and case study arrive on day 3 (docs/sprints/DEMO-SPRINT.md).
export default function Home() {
  return (
    <Shell>
      <h1>Protect what you value.</h1>
      <p className="m">
        Tagkin puts a QR tag on your bags, keys and pets. Whoever finds them scans the tag and tells
        you where they are, privately, without an app.
      </p>
      <h2>Try it as a finder</h2>
      <div className="opts">
        {DEMO.map((d) => (
          <Link
            key={d.code}
            className="opt"
            href={`/${d.code}`}
            style={{ justifyContent: "space-between", textDecoration: "none", color: "inherit" }}
          >
            <span>
              <b>{d.label}</b>
              <br />
              <span className="xs">{d.note}</span>
            </span>
            <span className="xs">{d.code}</span>
          </Link>
        ))}
      </div>
      <h2>Try it as the owner</h2>
      <p className="m">See the reports, answer the finder and close the return.</p>
      <Link className="btn btn-pri" href="/signin">
        Try the owner side
      </Link>
      <Link className="btn btn-sec" href="/find">
        Type a code
      </Link>
    </Shell>
  );
}
