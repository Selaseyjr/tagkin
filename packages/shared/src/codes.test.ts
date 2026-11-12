import { describe, expect, it } from "vitest";
import {
  CODE_ALPHABET,
  checkCharacter,
  generateCode,
  hasValidCheck,
  isBlocked,
  parseCode,
  qrUrl,
  displayUrl,
} from "./codes";

const seeded = (seed: number) => (max: number) => {
  seed = (seed * 1103515245 + 12345) % 2147483648;
  return seed % max;
};

describe("alphabet", () => {
  it("has 30 characters and no look-alikes", () => {
    expect(CODE_ALPHABET).toHaveLength(30);
    for (const c of "01ILOU") expect(CODE_ALPHABET).not.toContain(c);
  });
});

describe("generateCode", () => {
  it("produces TK-XXXX-XXXX with a valid check character and no blocked words", () => {
    const rnd = seeded(42);
    for (let i = 0; i < 5000; i++) {
      const code = generateCode(rnd);
      expect(code).toMatch(/^TK-[23456789A-HJKMNP-TV-Z]{4}-[23456789A-HJKMNP-TV-Z]{4}$/);
      const body = code.replace(/^TK-|-/g, "");
      expect(hasValidCheck(body)).toBe(true);
      expect(isBlocked(body)).toBe(false);
    }
  });
  it("works with the default crypto source", () => {
    expect(parseCode(generateCode()).ok).toBe(true);
  });
});

describe("check character", () => {
  const body7 = "7Q4M9XR";
  const body = body7 + checkCharacter(body7);
  it("catches every single-character typo", () => {
    for (let i = 0; i < 8; i++) {
      for (const c of CODE_ALPHABET) {
        if (c === body[i]) continue;
        const typo = body.slice(0, i) + c + body.slice(i + 1);
        expect(hasValidCheck(typo)).toBe(false);
      }
    }
  });
  it("catches most swaps of neighbouring characters", () => {
    let caught = 0,
      total = 0;
    for (let i = 0; i < 7; i++) {
      if (body[i] === body[i + 1]) continue;
      total++;
      const swapped = body.slice(0, i) + body[i + 1] + body[i] + body.slice(i + 2);
      if (!hasValidCheck(swapped)) caught++;
    }
    expect(caught).toBe(total);
  });
});

describe("parseCode", () => {
  const code = generateCode(seeded(7));
  const body = code.replace(/^TK-|-/g, "");
  it.each([
    code,
    code.toLowerCase(),
    body,
    body.toLowerCase(),
    ` tk ${body.slice(0, 4)} ${body.slice(4)} `,
    `https://tagkin.app/${code}`,
    qrUrl(code),
    `tagkin.app/${code.toLowerCase()}`,
  ])("accepts %s", (input) => {
    expect(parseCode(input)).toEqual({ ok: true, code });
  });
  it("rejects wrong length or characters as format", () => {
    expect(parseCode("TK-1234")).toEqual({ ok: false, reason: "format" });
    expect(parseCode("TK-7Q4M-9XRO")).toEqual({ ok: false, reason: "format" });
  });
  it("rejects a typo as check", () => {
    const typo = body.slice(0, 7) + (body[7] === "2" ? "3" : "2");
    expect(parseCode(typo)).toEqual({ ok: false, reason: "check" });
  });
});

describe("addresses", () => {
  it("QR address is upper case (alphanumeric QR mode) and stable", () => {
    expect(qrUrl("TK-7Q4M-9XRA")).toBe("HTTPS://TAGKIN.APP/TK-7Q4M-9XRA");
    expect(qrUrl("TK-7Q4M-9XRA")).toMatch(/^[0-9A-Z $%*+\-./:]+$/);
    expect(displayUrl("TK-7Q4M-9XRA")).toBe("tagkin.app/TK-7Q4M-9XRA");
  });
});
