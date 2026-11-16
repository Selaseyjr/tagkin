import Link from "next/link";
import type { ReactNode } from "react";
import { OfflineNote } from "./OfflineNote";
import { Icon } from "./Sprite";

/** The prototype's `.logo` (LOGO in build_screens.py). */
export function Logo() {
  return (
    <span className="logo">
      <Icon name="mark" size={20} />
      tagkin
    </span>
  );
}

/** `‹ Back` link (backto() in the prototype). */
export function Back({ href, label = "Back" }: { href: string; label?: string }) {
  return (
    <Link className="back" href={href}>
      ‹ {label}
    </Link>
  );
}

/** Privacy line (PRIV in the prototype). */
export function Priv({ children = "Your details stay private unless you choose to share them." }: { children?: ReactNode }) {
  return (
    <p className="priv">
      <Icon name="lock" size={14} />
      {children}
    </p>
  );
}

export type Tab = "tags" | "inbox" | "orders" | "account";

const TABS: { key: Tab; href: string; icon: "i-tag" | "i-chat" | "i-box" | "i-user"; label: string }[] = [
  { key: "tags", href: "/tags", icon: "i-tag", label: "My tags" },
  { key: "inbox", href: "/messages", icon: "i-chat", label: "Messages" },
  { key: "orders", href: "/orders", icon: "i-box", label: "Orders" },
  { key: "account", href: "/account", icon: "i-user", label: "Account" },
];

export function Tabs({ active, unread = false }: { active: Tab; unread?: boolean }) {
  return (
    <nav className="tabs" aria-label="Main">
      {TABS.map((t) => (
        <Link key={t.key} href={t.href} className={`tab${t.key === active ? " on" : ""}`} aria-current={t.key === active ? "page" : undefined}>
          <Icon name={t.icon} />
          {t.label}
          {t.key === "inbox" && unread && active !== "inbox" ? <b className="dot2" /> : null}
        </Link>
      ))}
    </nav>
  );
}

/**
 * One app screen (the prototype's `.scr`). `left`/`right` fill the header (hdr());
 * pass `header={false}` for full-bleed screens such as the splash.
 */
export function Screen({
  children,
  left = <Logo />,
  right,
  header = true,
  tabs,
  unread,
  className = "",
}: {
  children: ReactNode;
  left?: ReactNode;
  right?: ReactNode;
  header?: boolean;
  tabs?: Tab;
  unread?: boolean;
  className?: string;
}) {
  return (
    <main className={`scr${tabs ? " with-tabs" : ""}${className ? ` ${className}` : ""}`}>
      {header ? (
        <div className="hdr">
          {left}
          <span>{right}</span>
        </div>
      ) : null}
      {tabs ? <OfflineNote /> : null}
      {children}
      {tabs ? <Tabs active={tabs} unread={unread} /> : null}
    </main>
  );
}

export function Spacer() {
  return <div className="sp" />;
}
