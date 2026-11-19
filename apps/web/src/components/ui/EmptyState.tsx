import Link from "next/link";
import type { ReactNode } from "react";
import { Icon } from "./Sprite";

/** Empty states (e-tags, e-inbox, e-orders in the prototype). */
export function EmptyState({
  title,
  children,
  action,
}: {
  title: string;
  children: ReactNode;
  action?: { href: string; label: string };
}) {
  return (
    <>
      <div className="sp" />
      <div className="hero">
        <span className="bell">
          <Icon name="mark" size={52} />
        </span>
      </div>
      <h1 className="center">{title}</h1>
      <p className="m center">{children}</p>
      {action ? (
        <Link className="btn pri" href={action.href}>
          {action.label}
        </Link>
      ) : null}
      <div className="sp" />
    </>
  );
}
