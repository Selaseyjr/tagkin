import Link from "next/link";
import { signOut } from "@/app/signin/actions";

export function OwnerBar({ isDemo }: { isDemo: boolean }) {
  return (
    <div className="row" style={{ justifyContent: "space-between" }}>
      <Link href="/my-tags" className="xs">
        My tags
      </Link>
      {isDemo && <span className="badge ret">Shared demo account</span>}
      <form action={signOut}>
        <button
          className="btn btn-ghost"
          style={{ minHeight: 36, padding: "0 8px", width: "auto" }}
        >
          Sign out
        </button>
      </form>
    </div>
  );
}
