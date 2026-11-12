import { redirect } from "next/navigation";
import { Suspense } from "react";
import { parseCode } from "@tagkin/shared";
import { Priv, Shell } from "@/components/Shell";

const ERRORS: Record<string, string> = {
  not_a_code: "That doesn't look like a Tagkin code. Check the letters and numbers.",
  check_the_code: "Check the code: one character looks wrong.",
  not_found: "No tag with that code. Check the letters and numbers and try again.",
  rate_limited: "Too many tries. Please wait a few minutes.",
};

async function findTag(form: FormData) {
  "use server";
  const p = parseCode(String(form.get("code") ?? ""));
  if (!p.ok) redirect(`/find?e=${p.reason === "check" ? "check_the_code" : "not_a_code"}`);
  redirect(`/${p.code}`);
}

async function ErrorNote({ searchParams }: { searchParams: Promise<{ e?: string }> }) {
  const { e } = await searchParams;
  return e && ERRORS[e] ? (
    <p className="note err" role="alert">
      {ERRORS[e]}
    </p>
  ) : null;
}

export default function Find({ searchParams }: { searchParams: Promise<{ e?: string }> }) {
  return (
    <Shell>
      <h1>Found something with a Tagkin tag?</h1>
      <p className="m">Type the code printed under the QR.</p>
      <form action={findTag} className="opts">
        <Suspense>
          <ErrorNote searchParams={searchParams} />
        </Suspense>
        <input
          className="in code-in"
          name="code"
          placeholder="TK-XXXX-XXXX"
          autoComplete="off"
          aria-label="Tag code"
          required
        />
        <button className="btn btn-pri" type="submit">
          Find tag
        </button>
      </form>
      <Priv />
    </Shell>
  );
}
