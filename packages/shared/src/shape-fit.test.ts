import { describe, expect, it } from "vitest";
import { SHAPE_FIT, canBeBlank, fits, shapesFor, typesFor } from "./shape-fit";

describe("shape fit (BUSINESS-RULES 3c)", () => {
  it("matches the rules table exactly", () => {
    expect(SHAPE_FIT).toEqual({
      sticker: ["item", "travel"],
      keychain: ["item"],
      luggage_label: ["travel"],
      pet_tag: ["pet"],
      lock_screen: ["item"],
    });
  });
  it("offers printed shapes per type", () => {
    expect(shapesFor("item")).toEqual(["sticker", "keychain"]);
    expect(shapesFor("travel")).toEqual(["sticker", "luggage_label"]);
    expect(shapesFor("pet")).toEqual(["pet_tag"]);
  });
  it("skips the type step when one type fits", () => {
    expect(typesFor("keychain")).toHaveLength(1);
    expect(typesFor("sticker")).toHaveLength(2);
  });
  it("never offers the lock screen as blank or gift, nor on a pet", () => {
    expect(canBeBlank("lock_screen")).toBe(false);
    expect(fits("lock_screen", "pet")).toBe(false);
    expect(fits("pet_tag", "item")).toBe(false);
  });
});
