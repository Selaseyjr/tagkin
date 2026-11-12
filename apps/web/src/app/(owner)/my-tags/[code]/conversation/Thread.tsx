"use client";

import { useEffect, useRef, useState } from "react";

type Msg = { from: "owner" | "finder" | "system"; body: string; at: string };
const time = (iso: string) =>
  new Date(iso).toLocaleTimeString("en-GB", { hour: "2-digit", minute: "2-digit" });
const SUGGESTED = [
  "Thank you so much!",
  "I'll pick it up today",
  "Please hand it to staff",
  "Where exactly is it?",
];

/** Owner ↔ finder conversation (prototype Owner 13), live every 4 s. */
export function Thread({
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
  const end = useRef<HTMLDivElement>(null);
  const refresh = async () => {
    const r = await fetch(`/api/owner/${code}`, { cache: "no-store" });
    if (r.ok) setMessages((await r.json()).messages);
  };
  useEffect(() => {
    const id = setInterval(() => void refresh().catch(() => {}), 4000);
    return () => clearInterval(id);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [code]);
  useEffect(() => end.current?.scrollIntoView({ block: "end" }), [messages.length]);
  return (
    <>
      <div className="thread" aria-live="polite">
        {messages.map((m, i) => (
          <div key={i} className={m.from === "owner" ? "bub out" : "bub in2"}>
            {m.body}
            <time>{time(m.at)}</time>
          </div>
        ))}
        <div ref={end} />
      </div>
      <div className="sp" />
      <div className="chips">
        {SUGGESTED.map((s) => (
          <button
            key={s}
            type="button"
            className="chip"
            onClick={() => input.current && ((input.current.value = s), input.current.focus())}
          >
            {s}
          </button>
        ))}
      </div>
      <form
        className="compose"
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
          placeholder="Write a reply"
          aria-label="Write a reply"
          maxLength={1000}
          required
          autoComplete="off"
        />
        <button className="send" aria-label="Send">
          ↑
        </button>
      </form>
      <p className="xs center">
        Your reply reaches the finder on their page. Your email and number stay hidden.
      </p>
    </>
  );
}
