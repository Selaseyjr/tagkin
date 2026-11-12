import Link from "next/link";
import type { ReactNode } from "react";
import { Mark } from "./Mark";

export const IMPRESSUM_URL = "https://selasey-gbeddy.vercel.app/#impressum";

/** Page frame: logo, account link, content, legal footer. */
export function Shell({ children, wide = false }: { children: ReactNode; wide?: boolean }) {
  return (
    <>
      <header className={wide ? "top wide" : "top"}>
        <Link href="/" className="logo" aria-label="Tagkin home">
          <Mark /> tagkin
        </Link>
        <Link href="/my-tags" className="top-link">
          My tags
        </Link>
      </header>
      <main className={wide ? "page wide" : "page"}>{children}</main>
      <footer className="legal">
        <Link href="/privacy">Privacy</Link> · <a href={IMPRESSUM_URL}>Impressum</a> ·{" "}
        <a href="mailto:hello@tagkin.app">hello@tagkin.app</a>
      </footer>
    </>
  );
}

export function Priv() {
  return <p className="priv">🔒 Your details stay private unless you choose to share them.</p>;
}
