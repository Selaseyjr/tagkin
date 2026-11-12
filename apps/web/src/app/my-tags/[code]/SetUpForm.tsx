"use client";

import { useState, useTransition } from "react";

const LABEL = {
  item: "Item · keys, bag, laptop",
  travel: "Travel · luggage on a journey",
  pet: "Pet · collar tag",
} as const;

export function SetUpForm({
  types,
  action,
}: {
  types: readonly ("item" | "travel" | "pet")[];
  action: (f: FormData) => Promise<{ error?: string }>;
}) {
  const [error, setError] = useState<string>();
  const [pending, start] = useTransition();
  return (
    <form
      className="opts"
      onSubmit={(e) => {
        e.preventDefault();
        const data = new FormData(e.currentTarget);
        start(async () => setError((await action(data)).error));
      }}
    >
      <fieldset className="opts" style={{ border: 0, padding: 0, margin: 0 }}>
        <legend style={{ fontWeight: 650, marginBottom: 8 }}>What is it for?</legend>
        {types.map((t, i) => (
          <label key={t} className="opt">
            <input type="radio" name="type" value={t} defaultChecked={i === 0} /> {LABEL[t]}
          </label>
        ))}
      </fieldset>
      <label className="field">
        Name
        <input className="in" name="name" maxLength={40} placeholder="e.g. House keys" required />
      </label>
      <label className="field">
        Finder message <span className="xs">Optional</span>
        <input
          className="in"
          name="message"
          maxLength={160}
          placeholder="Found me? Thank you! Tap below to tell my owner where I am."
        />
      </label>
      {error && (
        <p className="note err" role="alert">
          {error}
        </p>
      )}
      <button className="btn btn-pri" disabled={pending}>
        {pending ? "Saving…" : "Make it live"}
      </button>
    </form>
  );
}
