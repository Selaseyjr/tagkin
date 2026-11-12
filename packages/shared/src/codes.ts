/**
 * Tag codes (BUSINESS-RULES 4.1, SYSTEM-LOGIC 6).
 * Format TK-XXXX-XXXX: 7 random characters + 1 check character (Luhn mod 30).
 * The QR address is permanent: HTTPS://TAGKIN.APP/TK-XXXX-XXXX in capitals.
 */

/** No 0, 1, I, L, O or U: reads aloud and types cleanly. 30 characters. */
export const CODE_ALPHABET = "23456789ABCDEFGHJKMNPQRSTVWXYZ";
export const CODE_PREFIX = "TK";
export const CODE_BODY_LENGTH = 8; // 7 random + 1 check
const N = CODE_ALPHABET.length;

/** Starter blocklist, checked on the 8 characters without dashes. Extending it never affects issued codes. */
export const BLOCKED_SEQUENCES = [
  "SEX",
  "ASS",
  "XXX",
  "KKK",
  "FCK",
  "FKK",
  "WTF",
  "TWAT",
  "DCK",
  "ARSCH",
  "KACK",
  "NAZ",
  "NGGR",
  "SS",
  "HH",
  "88",
] as const;

function value(ch: string): number {
  const v = CODE_ALPHABET.indexOf(ch);
  if (v < 0) throw new Error(`Character not in the code alphabet: ${ch}`);
  return v;
}

/** Luhn mod N check character for a body of random characters. */
export function checkCharacter(random: string): string {
  let factor = 2;
  let sum = 0;
  for (let i = random.length - 1; i >= 0; i--) {
    let addend = factor * value(random[i]!);
    factor = factor === 2 ? 1 : 2;
    addend = Math.floor(addend / N) + (addend % N);
    sum += addend;
  }
  return CODE_ALPHABET[(N - (sum % N)) % N]!;
}

/** True when the last character is the correct check character. */
export function hasValidCheck(body: string): boolean {
  let factor = 1;
  let sum = 0;
  for (let i = body.length - 1; i >= 0; i--) {
    const v = CODE_ALPHABET.indexOf(body[i]!);
    if (v < 0) return false;
    let addend = factor * v;
    factor = factor === 2 ? 1 : 2;
    addend = Math.floor(addend / N) + (addend % N);
    sum += addend;
  }
  return sum % N === 0;
}

export function isBlocked(body: string): boolean {
  return BLOCKED_SEQUENCES.some((w) => body.includes(w));
}

/** "7Q4M9XRA" → "TK-7Q4M-9XRA" */
export function formatCode(body: string): string {
  return `${CODE_PREFIX}-${body.slice(0, 4)}-${body.slice(4, 8)}`;
}

type WithCrypto = { crypto: { getRandomValues(array: Uint8Array): Uint8Array } };

export type RandomInt = (maxExclusive: number) => number;

/** Uniform random integer using Web Crypto (Node 24, browsers). Server-side code generation only. */
export const cryptoRandomInt: RandomInt = (max) => {
  const limit = 256 - (256 % max);
  const buf = new Uint8Array(1);
  for (;;) {
    (globalThis as unknown as WithCrypto).crypto.getRandomValues(buf);
    if (buf[0]! < limit) return buf[0]! % max;
  }
};

/** New code, never containing a blocked sequence. Uniqueness is enforced by the database. */
export function generateCode(randomInt: RandomInt = cryptoRandomInt): string {
  for (;;) {
    let random = "";
    for (let i = 0; i < CODE_BODY_LENGTH - 1; i++) random += CODE_ALPHABET[randomInt(N)];
    const body = random + checkCharacter(random);
    if (!isBlocked(body)) return formatCode(body);
  }
}

export type ParsedCode = { ok: true; code: string } | { ok: false; reason: "format" | "check" };

/**
 * Accepts what a finder types or a scanned URL: any case, spaces, dashes,
 * with or without TK- or the tagkin.app address.
 */
export function parseCode(input: string): ParsedCode {
  let s = input.trim().toUpperCase();
  s = s.replace(/^(HTTPS?:\/\/)?(WWW\.)?TAGKIN\.APP\/?/, "");
  s = s.replace(/[\s\-_.]/g, "");
  if (s.startsWith(CODE_PREFIX) && s.length === CODE_BODY_LENGTH + CODE_PREFIX.length) {
    s = s.slice(CODE_PREFIX.length);
  }
  if (s.length !== CODE_BODY_LENGTH || [...s].some((c) => !CODE_ALPHABET.includes(c))) {
    return { ok: false, reason: "format" };
  }
  if (!hasValidCheck(s)) return { ok: false, reason: "check" };
  return { ok: true, code: formatCode(s) };
}

/** What the QR encodes. Capitals keep the QR in compact alphanumeric mode. Never change. */
export function qrUrl(code: string): string {
  return `HTTPS://TAGKIN.APP/${code}`;
}

/** What people read (printed under the QR, shown on pages). */
export function displayUrl(code: string): string {
  return `tagkin.app/${code}`;
}
