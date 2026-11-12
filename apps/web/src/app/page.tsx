import Link from "next/link";
import { Shell } from "@/components/Shell";

export default function Home() {
  return (
    <Shell>
      <h1 style={{ fontSize: 34 }}>Protect what you value.</h1>
      <p className="m">
        Put a Tagkin tag on your bags, keys, luggage and pets. Whoever finds them scans the tag and
        tells you where they are. No app needed for them, and nobody sees your number or email.
      </p>
      <ol className="steps">
        <li>
          <b className="n">1</b>
          <span>
            <b>Tag it.</b>{" "}
            <span className="m">
              Sticker, keychain, pet tag or luggage label, with your own message for the finder.
            </span>
          </span>
        </li>
        <li>
          <b className="n">2</b>
          <span>
            <b>Someone finds it.</b>{" "}
            <span className="m">They scan the QR and say where it is, in their own language.</span>
          </span>
        </li>
        <li>
          <b className="n">3</b>
          <span>
            <b>You get it back.</b>{" "}
            <span className="m">
              You reply privately and arrange the handover. Lost mode makes the page urgent.
            </span>
          </span>
        </li>
      </ol>
      <Link className="btn btn-pri" href="/my-tags">
        Sign in to My tags
      </Link>
      <Link className="btn btn-sec" href="/find">
        Found something? Enter its code
      </Link>
      <p className="priv">
        🔒 Private by default. Messages are relayed, never your contact details.
      </p>
    </Shell>
  );
}
