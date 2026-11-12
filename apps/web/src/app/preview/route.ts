import { connection } from "next/server";
import { signInSample } from "@/app/(owner)/signin/actions";

// Unlisted entry shared by word of mouth: opens the sample owner account and lands on My tags.
// Not linked anywhere in the product; search engines are blocked by robots and noindex.
export async function GET() {
  await connection(); // per request, never prerendered
  await signInSample();
}
