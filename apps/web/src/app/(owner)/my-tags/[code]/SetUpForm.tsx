"use client";

import { useState, useTransition } from "react";

const OPTION = {
  item: { ic: "🎒", label: "Item", sub: "Keys, bag, laptop" },
  travel: { ic: "🧳", label: "Travel", sub: "Luggage on a journey" },
  pet: { ic: "🐾", label: "Pet", sub: "Collar tag" },
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
      className="grp"
      onSubmit={(e) => {
        e.preventDefault();
        const data = new FormData(e.currentTarget);
        start(async () => setError((await action(data))?.error));
      }}
    >
      <div className="grp" role="radiogroup" aria-label="What is it for?">
        {types.map((t, i) => (
          <label key={t} className="opt">
            <input type="radio" name="type" value={t} defaultChecked={i === 0} />
            <span className="ic">{OPTION[t].ic}</span>
            <span>
              {OPTION[t].label}
              <small>{OPTION[t].sub}</small>
            </span>
          </label>
        ))}
      </div>
      <p className="xs">You can&apos;t change the type later.</p>
      <input
        className="in"
        name="name"
        maxLength={40}
        placeholder="Name, e.g. House keys"
        aria-label="Name"
        required
      />
      <input
        className="in"
        name="message"
        maxLength={160}
        placeholder="Finder message (optional)"
        aria-label="Finder message"
      />
      {error && (
        <p className="note err" role="alert">
          {error}
        </p>
      )}
      <button className="btn pri" disabled={pending}>
        {pending ? "Saving…" : "Make it live"}
      </button>
    </form>
  );
}
