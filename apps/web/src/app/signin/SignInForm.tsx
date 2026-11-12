"use client";

import { startTransition, useActionState } from "react";
import { sendCode, verifyCode, type SignInState } from "./actions";

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
      <form onSubmit={submit(verify)} className="opts">
        <p className="m">
          We sent a 6-digit code to <b>{state.email}</b>. It works for 10 minutes.
        </p>
        <input type="hidden" name="email" value={state.email} />
        <input
          className="in code-in"
          name="code"
          inputMode="numeric"
          autoComplete="one-time-code"
          maxLength={6}
          placeholder="······"
          aria-label="6-digit code"
          required
        />
        {vstate.error && (
          <p className="note err" role="alert">
            {vstate.error}
          </p>
        )}
        <button className="btn btn-pri" disabled={verifying}>
          {verifying ? "Checking…" : "Sign in"}
        </button>
        <p className="xs">Not there? Check spam, or wait 30 seconds and try again.</p>
      </form>
    );
  }
  return (
    <form onSubmit={submit(send)} className="opts">
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
      <button className="btn btn-sec" disabled={sending}>
        {sending ? "Sending…" : "Send me a code"}
      </button>
    </form>
  );
}
