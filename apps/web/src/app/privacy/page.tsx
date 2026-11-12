import { Shell, IMPRESSUM_URL } from "@/components/Shell";

export const metadata = { title: "Privacy · Tagkin" };

export default function Privacy() {
  return (
    <Shell>
      <h1>Privacy</h1>
      <p className="m">
        Tagkin is built to be private by default. This page explains what we store and why.
      </p>
      <div className="card">
        <h2>Finders</h2>
        <p className="m">
          When you report a tag we store where the item is, your note and, only if you add it, your
          email so the owner&apos;s replies can reach you. The owner never sees your email or number
          unless you write it in a message yourself.
        </p>
      </div>
      <div className="card">
        <h2>Owners</h2>
        <p className="m">
          Your email (to sign in with a code), your tags, item details and your conversations with
          finders. For each tag view we keep the time and an approximate city, never an exact
          location unless a finder shares it.
        </p>
      </div>
      <div className="card">
        <h2>Security and abuse protection</h2>
        <p className="m">
          To stop code guessing and spam we keep short-lived counters keyed on a salted hash of your
          connection, never your IP address. No advertising, no tracking cookies.
        </p>
      </div>
      <div className="card">
        <h2>Where data is kept</h2>
        <p className="m">
          Database in Frankfurt (Supabase), website and server functions in Frankfurt (Vercel),
          sign-in emails through Brevo in the EU.
        </p>
      </div>
      <div className="card">
        <h2>Your rights</h2>
        <p className="m">To see, correct or delete your data, write to hello@tagkin.app.</p>
      </div>
      <p className="xs">
        Responsible: see the <a href={IMPRESSUM_URL}>Impressum</a>.
      </p>
    </Shell>
  );
}
