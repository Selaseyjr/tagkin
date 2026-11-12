"use client";

import { startTransition, useActionState } from "react";
import { submitReport, type ReportState } from "./actions";

export function ReportForm({ code, name }: { code: string; name: string }) {
  const [state, action, pending] = useActionState<ReportState, FormData>(submitReport, {});
  const v = state.values ?? {};
  return (
    <form
      onSubmit={(e) => {
        // Submit without React's automatic form reset, so entered text survives a warning.
        e.preventDefault();
        const data = new FormData(e.currentTarget);
        startTransition(() => action(data));
      }}
      className="opts"
      style={{ gap: 16 }}
    >
      <input type="hidden" name="code" value={code} />
      <fieldset className="opts" style={{ border: 0, padding: 0, margin: 0 }}>
        <legend style={{ fontWeight: 650, marginBottom: 8 }}>Where is {name} now?</legend>
        <label className="opt">
          <input
            type="radio"
            name="where"
            value="with_me"
            defaultChecked={v.where === "with_me"}
            required
          />{" "}
          With me
        </label>
        <label className="opt">
          <input type="radio" name="where" value="staff" defaultChecked={v.where === "staff"} />{" "}
          Handed to staff
        </label>
        <label className="opt">
          <input
            type="radio"
            name="where"
            value="safe_place"
            defaultChecked={v.where === "safe_place"}
          />{" "}
          Left it in a safe place
        </label>
      </fieldset>
      <label className="field">
        Where exactly?
        <input
          className="in"
          name="place"
          defaultValue={v.place}
          placeholder="e.g. Darmstadt Hbf, Lost & Found desk"
          required
          minLength={2}
          maxLength={200}
        />
      </label>
      <label className="field">
        Anything else? <span className="xs">Optional</span>
        <textarea
          className="in"
          name="note"
          defaultValue={v.note}
          maxLength={500}
          placeholder="e.g. Left it with the staff at counter 2"
        />
      </label>
      {state.needsShareOk && (
        <label className="opt">
          <input type="checkbox" name="shareOk" value="yes" required /> Share my number or email
          with the owner
        </label>
      )}
      <label className="field">
        Want a reply by email? <span className="xs">Optional, kept hidden from the owner</span>
        <input
          className="in"
          type="email"
          name="email"
          defaultValue={v.email}
          placeholder="you@example.com"
          autoComplete="email"
        />
      </label>
      <p className="xs">
        Without an email, keep the next page open (or save its link) to see the owner&apos;s reply.
      </p>
      {state.error && (
        <p className="note err" role="alert">
          {state.error}
        </p>
      )}
      <button className="btn btn-pri" type="submit" disabled={pending}>
        {pending ? "Sending…" : "Send to owner"}
      </button>
    </form>
  );
}
