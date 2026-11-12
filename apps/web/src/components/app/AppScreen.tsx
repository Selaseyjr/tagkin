import Link from "next/link";
import type { ReactNode } from "react";
import { Mark } from "../Mark";

type Tab = "tags" | "messages" | "orders" | "account";

const ICON: Record<Tab, ReactNode> = {
  tags: <path d="M3 9 8 4h13v16H8l-5-5Z M9 13.6a1.6 1.6 0 1 0 0-3.2 1.6 1.6 0 0 0 0 3.2Z" />,
  messages: <path d="M4 5h16v11H9l-5 4Z" />,
  orders: <path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5Z M3 7.5 12 12l9-4.5 M12 12v9" />,
  account: <path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Z M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6" />,
};
const TABS: [Tab, string, string][] = [
  ["tags", "My tags", "/my-tags"],
  ["messages", "Messages", "/messages"],
  ["orders", "Orders", "/orders"],
  ["account", "Account", "/account"],
];

/** Phone app frame from the prototype: header (back or logo, right slot), content, bottom tabs. */
export function AppScreen({
  back,
  right,
  tab,
  unread,
  children,
}: {
  back?: { href: string; label?: string };
  right?: ReactNode;
  tab?: Tab;
  unread?: boolean;
  children: ReactNode;
}) {
  return (
    <div className="app">
      <div className="hdr">
        {back ? (
          <Link className="back" href={back.href}>
            ‹ {back.label ?? "Back"}
          </Link>
        ) : (
          <Link className="logo" href="/">
            <Mark size={22} /> tagkin
          </Link>
        )}
        <span>{right}</span>
      </div>
      {children}
      {tab && (
        <nav className="tabs" aria-label="Main">
          {TABS.map(([key, label, href]) => (
            <Link
              key={key}
              href={href}
              className={key === tab ? "tab on" : "tab"}
              aria-current={key === tab ? "page" : undefined}
            >
              <svg
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinejoin="round"
                strokeLinecap="round"
                aria-hidden="true"
              >
                {ICON[key]}
              </svg>
              {label}
              {key === "messages" && unread && tab !== "messages" && (
                <b className="dot2" aria-label="New message" />
              )}
            </Link>
          ))}
        </nav>
      )}
    </div>
  );
}

export function QrIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true">
      <path
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        d="M4 4h6v6H4ZM14 4h6v6h-6ZM4 14h6v6H4Z"
      />
      <path fill="currentColor" d="M14 14h3v3h-3ZM17 17h3v3h-3ZM14 18h2v2h-2ZM18 14h2v2h-2Z" />
    </svg>
  );
}
