import { Mark } from "@/components/Mark";

export default function Home() {
  return (
    <main className="hold">
      <span className="hold-logo">
        <Mark size={44} /> tagkin
      </span>
      <h1>Protect what you value.</h1>
      <p>Coming soon.</p>
      <footer>
        <a href="https://selasey-gbeddy.vercel.app/#impressum">Impressum</a> ·{" "}
        <a href="mailto:hello@tagkin.app">hello@tagkin.app</a>
      </footer>
    </main>
  );
}
