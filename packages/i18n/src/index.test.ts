import { describe, expect, it } from "vitest";
import { createI18n, isRtl, pickLanguage } from "./index";

describe("i18n", () => {
  it("translates with English fallback", async () => {
    const t = (await createI18n("de")).t;
    expect(t("app.tagline")).toBe("Protect what you value.");
  });
  it("picks a core language", () => {
    expect(pickLanguage(["de-DE", "en"])).toBe("de");
    expect(pickLanguage(["tw-GH"])).toBe("en");
  });
  it("detects right-to-left", () => {
    expect(isRtl("ar-EG")).toBe(true);
    expect(isRtl("de")).toBe(false);
  });
});
