import { describe, expect, it } from "vitest";
import {
  finderMessageSchema,
  itemNameSchema,
  labelSchema,
  productTypeSchema,
  statusUpdateSchema,
  tagCodeSchema,
} from "./schemas";
import { generateCode } from "./codes";

describe("schemas", () => {
  it("item name 2 to 40 characters", () => {
    expect(itemNameSchema.safeParse(" A ").success).toBe(false);
    expect(itemNameSchema.safeParse("Black backpack").success).toBe(true);
    expect(itemNameSchema.safeParse("x".repeat(41)).success).toBe(false);
  });
  it("finder message blocks links", () => {
    expect(finderMessageSchema.safeParse("Found me? Thank you!").success).toBe(true);
    expect(finderMessageSchema.safeParse("Visit www.evil.example").success).toBe(false);
    expect(finderMessageSchema.safeParse("Go to claim-prize.com now").success).toBe(false);
  });
  it("label blocks contact details", () => {
    expect(labelSchema.safeParse("MILO").success).toBe(true);
    expect(labelSchema.safeParse("0151 234567").success).toBe(false);
    expect(labelSchema.safeParse("a@b.de").success).toBe(false);
  });
  it("status update rejects dates and times", () => {
    expect(statusUpdateSchema.safeParse("Arrived in Dubai").success).toBe(true);
    for (const t of [
      "Back on 20.11",
      "Landing 14:30",
      "Home tomorrow",
      "Ab Montag zurück",
      "Until Nov",
    ]) {
      expect(statusUpdateSchema.safeParse(t).success).toBe(false);
    }
  });
  it("tag code normalises and reports typos", () => {
    const code = generateCode();
    expect(tagCodeSchema.parse(code.toLowerCase())).toBe(code);
    const r = tagCodeSchema.safeParse("TK-ABCD-EFG2");
    expect(r.success).toBe(false);
  });
  it("product and type must fit", () => {
    expect(productTypeSchema.safeParse({ product: "sticker", type: "travel" }).success).toBe(true);
    expect(productTypeSchema.safeParse({ product: "lock_screen", type: "pet" }).success).toBe(
      false,
    );
  });
});
