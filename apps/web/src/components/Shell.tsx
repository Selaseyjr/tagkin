import Link from "next/link";
import type { ReactNode } from "react";
import { Mark } from "./Mark";

export const IMPRESSUM_URL = "https://selasey-gbeddy.vercel.app/#impressum";

/** Page frame: demo notice, logo, content, legal footer. */
export function Shell({ children, wide = false }: { children: ReactNode; wide?: boolean }) {
  return (
    <>
      <p className="demo-bar">Demo · Data resets every night · Nothing is sold or shipped</p>
      <header className={wide ? "top wide" : "top"}>
        <Link href="/" className="logo" aria-label="Tagkin home">
          <Mark /> tagkin
        </Link>
      </header>
      <main className={wide ? "page wide" : "page"}>{children}</main>
      <footer className="legal">
        <Link href="/privacy">Privacy</Link> · <a href={IMPRESSUM_URL}>Impressum</a> ·{" "}
        <Link href="/case-study">Case study</Link>
      </footer>
    </>
  );
}

export function Priv() {
  return <p className="priv">🔒 Your details stay private unless you choose to share them.</p>;
}
