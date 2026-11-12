"use client";

import { useEffect, useRef, useState } from "react";

type Msg = { from: "owner" | "finder" | "system"; body: string; at: string };
const time = (iso: string) =>
  new Date(iso).toLocaleString([], {
    hour: "2-digit",
    minute: "2-digit",
    day: "numeric",
    month: "short",
  });
const SUGGESTED = [
  "Thank you so much!",
  "I'll pick it up today",
  "Please hand it to staff",
  "Where exactly is it?",
];

/** The owner's live conversation with the finder (polls every 4 s). */
export function OwnerThread({
  code,
  initial,
  reply,
}: {
  code: string;
  initial: Msg[];
  reply: (f: FormData) => Promise<void>;
}) {
  const [messages, setMessages] = useState(initial);
  const input = useRef<HTMLInputElement>(null);
  const refresh = async () => {
    const r = await fetch(`/api/owner/${code}`, { cache: "no-store" });
    if (r.ok) setMessages((await r.json()).messages);
  };
  useEffect(() => {
    const id = setInterval(() => void refresh().catch(() => {}), 4000);
    return () => clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [code]);
  return (
    <>
      <div className="thread" aria-live="polite">
        {messages.map((m, i) => (
          <div key={i} className={m.from === "owner" ? "bub me" : "bub them"}>
            {m.from === "finder" && (
              <b>
                Finder
                <br />
              </b>
            )}
            {m.body}
            <small>{time(m.at)}</small>
          </div>
        ))}
      </div>
      <div className="chips">
        {SUGGESTED.map((s) => (
          <button
            key={s}
            type="button"
            className="badge"
            style={{ border: 0, cursor: "pointer" }}
            onClick={() => input.current && (input.current.value = s)}
          >
            {s}
          </button>
        ))}
      </div>
      <form
        className="row"
        action={async (f) => {
          await reply(f);
          if (input.current) input.current.value = "";
          await refresh();
        }}
      >
        <input
          ref={input}
          className="in"
          name="body"
          placeholder="Reply to the finder"
          aria-label="Reply"
          maxLength={1000}
          required
        />
        <button className="btn btn-pri" style={{ width: "auto" }}>
          Send
        </button>
      </form>
      <p className="xs">
        Your reply reaches the finder on their report page. Your email and number stay hidden.
      </p>
    </>
  );
}
