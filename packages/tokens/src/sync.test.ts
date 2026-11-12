import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";
// @ts-expect-error plain JS build script
import { SOURCE, build } from "../scripts/generate.mjs";
import { tokens } from "./generated";

describe("tokens", () => {
  it("are in sync with docs/brand/tokens.css (run: pnpm --filter @tagkin/tokens generate)", () => {
    const out = build(readFileSync(SOURCE, "utf8"));
    expect(readFileSync(resolve(__dirname, "generated.ts"), "utf8")).toBe(out.ts);
    expect(readFileSync(resolve(__dirname, "tokens.css"), "utf8")).toBe(out.css);
  });
  it("have light and dark colours for the same keys", () => {
    expect(Object.keys(tokens.color.dark).sort()).toEqual(Object.keys(tokens.color.light).sort());
    expect(tokens.color.light.brand).toBe("#00c48c");
    expect(tokens.text.md).toBe(16);
    expect(tokens.tap).toBe(52);
  });
});
