"use client";

import { useEffect, useRef, useState } from "react";
import type { ReportView } from "@/lib/report";

type Msg = ReportView["messages"][number];

const time = (iso: string) =>
  new Date(iso).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

/** Live thread: polls every 4 seconds while the page is open (TK-16). */
export function Thread({
  token,
  initial,
  reply,
}: {
  token: string;
  initial: Msg[];
  reply: (f: FormData) => Promise<void>;
}) {
  const [messages, setMessages] = useState(initial);
  const formRef = useRef<HTMLFormElement>(null);
  useEffect(() => {
    let stop = false;
    const tick = async () => {
      try {
        const r = await fetch(`/api/r/${token}`, { cache: "no-store" });
        if (r.ok && !stop) setMessages((await r.json()).messages);
      } catch {
        // offline for a moment; try again next tick
      }
    };
    const id = setInterval(tick, 4000);
    return () => {
      stop = true;
      clearInterval(id);
    };
  }, [token]);
  const waiting = !messages.some((m) => m.from === "owner");
  return (
    <>
      <div className="thread" aria-live="polite">
        {messages.map((m, i) => (
          <div key={i} className={m.from === "finder" ? "bub me" : "bub them"}>
            {m.from === "owner" && (
              <b>
                Owner
                <br />
              </b>
            )}
            {m.body}
            <small>{time(m.at)}</small>
          </div>
        ))}
        {waiting && (
          <p className="xs">Waiting for the owner&apos;s reply… This page updates on its own.</p>
        )}
      </div>
      <form
        ref={formRef}
        action={async (f) => {
          await reply(f);
          formRef.current?.reset();
          const r = await fetch(`/api/r/${token}`, { cache: "no-store" });
          if (r.ok) setMessages((await r.json()).messages);
        }}
        className="row"
      >
        <input
          className="in"
          name="body"
          placeholder="Reply to the owner"
          aria-label="Reply"
          maxLength={1000}
          required
        />
        <button className="btn btn-pri" style={{ width: "auto" }} type="submit">
          Send
        </button>
      </form>
    </>
  );
}
