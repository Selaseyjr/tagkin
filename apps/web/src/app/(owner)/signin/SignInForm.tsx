"use client";

import { startTransition, useActionState } from "react";
import { sendCode, verifyCode, type SignInState } from "./actions";

const Lock = () => (
  <svg
    width="14"
    height="14"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    aria-hidden="true"
  >
    <rect x="5" y="11" width="14" height="10" rx="2" />
    <path d="M8 11V8a4 4 0 0 1 8 0v3" />
  </svg>
);

export function SignInForm() {
  const [state, send, sending] = useActionState<SignInState, FormData>(sendCode, { step: "email" });
  const [vstate, verify, verifying] = useActionState<SignInState, FormData>(verifyCode, state);
  const submit = (fn: (f: FormData) => void) => (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    startTransition(() => fn(data));
  };
  if (state.step === "code") {
    return (
      <form onSubmit={submit(verify)} className="grp" style={{ flex: 1 }}>
        <h1>Check your email</h1>
        <p className="m">We sent a 6-digit code to {state.email}</p>
        <input type="hidden" name="email" value={state.email} />
        <input
          className="in code-in"
          name="code"
          inputMode="numeric"
          autoComplete="one-time-code"
          maxLength={6}
          aria-label="6-digit code"
          required
          autoFocus
        />
        {vstate.error && (
          <p className="note err" role="alert">
            {vstate.error}
          </p>
        )}
        <button className="btn pri" disabled={verifying}>
          {verifying ? "Checking…" : "Continue"}
        </button>
        <p className="xs">Not there? Check spam, or wait 30 seconds and try again.</p>
      </form>
    );
  }
  return (
    <form onSubmit={submit(send)} className="grp" style={{ flex: 1 }}>
      <div className="sp" />
      <h1 className="big">Sign in</h1>
      <p className="m">Enter your email. No password: we send you a code.</p>
      <input
        className="in"
        type="email"
        name="email"
        autoComplete="email"
        placeholder="you@example.com"
        aria-label="Email"
        defaultValue={state.email}
        required
      />
      {state.error && (
        <p className="note err" role="alert">
          {state.error}
        </p>
      )}
      <button className="btn pri" disabled={sending}>
        {sending ? "Sending…" : "Send code"}
      </button>
      <div className="sp" />
      <p className="xs" style={{ display: "flex", gap: 8 }}>
        <Lock /> Your contact is never shown. Finders message you through Tagkin.
      </p>
    </form>
  );
}
