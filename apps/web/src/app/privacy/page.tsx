import { Shell, IMPRESSUM_URL } from "@/components/Shell";

export const metadata = { title: "Privacy · Tagkin demo" };

export default function Privacy() {
  return (
    <Shell>
      <h1>Privacy in the Tagkin demo</h1>
      <p className="m">
        This is a portfolio demo by Selasey Gbeddy. Nothing is sold or shipped, and all demo data is
        deleted every night.
      </p>
      <div className="card">
        <h2>What the demo stores</h2>
        <p className="m">
          When you report a demo tag: where the item is, your note and, only if you add it, your
          email. When the owner side is used: the replies. An approximate city of each tag view,
          from your connection, never an exact location. A hashed, salted key of your connection for
          rate limiting, never your IP address.
        </p>
      </div>
      <div className="card">
        <h2>Where it is stored</h2>
        <p className="m">
          Supabase (database, Frankfurt), Vercel (hosting, functions in Frankfurt), Brevo (sign-in
          emails, EU). No tracking cookies, no advertising, no analytics in the demo.
        </p>
      </div>
      <div className="card">
        <h2>Your rights</h2>
        <p className="m">
          Demo data is deleted nightly. To ask about or delete anything sooner, write to
          hello@tagkin.app.
        </p>
      </div>
      <p className="xs">
        Responsible person: see the <a href={IMPRESSUM_URL}>Impressum</a>.
      </p>
    </Shell>
  );
}
