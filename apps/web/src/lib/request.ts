import "server-only";
import { createHash, randomBytes } from "node:crypto";
import { headers } from "next/headers";
import { serverEnv } from "./env";

const BOT =
  /bot|crawl|spider|slurp|preview|facebookexternalhit|whatsapp|telegram|slack|discord|skype|curl|wget|python|headless|lighthouse|monitor/i;

/** Hashed client key for rate limits: no raw IP addresses are stored (privacy). */
export async function clientKey(scope: string) {
  const h = await headers();
  const ip = (h.get("x-forwarded-for") ?? h.get("x-real-ip") ?? "local").split(",")[0]!.trim();
  const salt = createHash("sha256").update(serverEnv().SUPABASE_SECRET_KEY).digest("hex");
  return `${scope}:${createHash("sha256")
    .update(salt + ip)
    .digest("hex")
    .slice(0, 32)}`;
}

/** A person's browser, not a link previewer or crawler (audit B13). */
export async function isPerson() {
  const ua = (await headers()).get("user-agent") ?? "";
  return ua.length > 0 && !BOT.test(ua);
}

/** City from Vercel's edge (approximate; never stored with more precision). */
export async function approximateCity() {
  const city = (await headers()).get("x-vercel-ip-city");
  return city ? decodeURIComponent(city) : null;
}

export function newToken() {
  return randomBytes(24).toString("base64url");
}

export function hashToken(token: string) {
  return createHash("sha256").update(token).digest("hex");
}
