import Link from "next/link";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { hasOpenReturn, requireOwner } from "@/lib/owner";
import { signOut } from "../signin/actions";

async function Account() {
  const { user } = await requireOwner();
  const unread = await hasOpenReturn();
  const email = user.email ?? "";
  const masked = email.replace(/^(.)[^@]*/, "$1•••");
  return (
    <AppScreen tab="account" unread={unread}>
      <h1>Account</h1>
      <div className="acct">
        <span className="av">{email.charAt(0).toUpperCase()}</span>
        <span>
          <b>Your account</b>
          <span className="xs">{masked}</span>
        </span>
      </div>
      <div>
        <div className="li">
          <span>Sign-in email</span>
          <span>{masked}</span>
        </div>
        <div className="li">
          <span>Language</span>
          <span>English</span>
        </div>
        <Link className="li" href="/privacy">
          <span>Privacy and data</span>
          <span>›</span>
        </Link>
        <a className="li" href="mailto:hello@tagkin.app">
          <span>Help</span>
          <span>›</span>
        </a>
      </div>
      <div className="sp" />
      <form action={signOut}>
        <button className="btn sec">Sign out</button>
      </form>
    </AppScreen>
  );
}

export default function Page() {
  return (
    <Suspense fallback={<div className="app" />}>
      <Account />
    </Suspense>
  );
}
