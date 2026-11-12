import { Suspense } from "react";
import { Shell } from "@/components/Shell";
import { SignInForm } from "./SignInForm";
import { tryDemoOwner } from "./actions";

const ERRORS: Record<string, string> = {
  demo: "The demo account isn't available right now. Please try again in a minute.",
  busy: "Too many demo sign-ins from this connection. Please wait a little.",
};

async function DemoError({ searchParams }: { searchParams: Promise<{ e?: string }> }) {
  const { e } = await searchParams;
  return e && ERRORS[e] ? (
    <p className="note err" role="alert">
      {ERRORS[e]}
    </p>
  ) : null;
}

export default function SignIn({ searchParams }: { searchParams: Promise<{ e?: string }> }) {
  return (
    <Shell>
      <h1>Your tags</h1>
      <div className="card">
        <h2>Try the owner side</h2>
        <p className="m">
          Open a shared demo account with four tags. Report one of them as a finder in another tab,
          then answer here.
        </p>
        <Suspense>
          <DemoError searchParams={searchParams} />
        </Suspense>
        <form action={tryDemoOwner}>
          <button className="btn btn-pri">Try the owner side</button>
        </form>
      </div>
      <div className="card">
        <h2>Sign in with your email</h2>
        <p className="m">No password: we email you a 6-digit code. The demo is invite-only.</p>
        <SignInForm />
      </div>
    </Shell>
  );
}
