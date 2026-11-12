import i18next, { type i18n } from "i18next";
import enCommon from "./locales/en/common.json";

/** Core languages (BUSINESS-RULES 8.3). Translations arrive with TK-92; English is the source. */
export const CORE_LANGUAGES = ["en", "de", "fr", "nl", "pl", "es", "it"] as const;
export type CoreLanguage = (typeof CORE_LANGUAGES)[number];
export const DEFAULT_LANGUAGE: CoreLanguage = "en";
export const NAMESPACES = ["common"] as const;

export const resources = { en: { common: enCommon } } as const;

const RTL = ["ar", "he", "fa", "ur"];
export function isRtl(language: string): boolean {
  return RTL.includes(language.split("-")[0]!.toLowerCase());
}

/** Best supported language for a list like navigator.languages or Accept-Language order. */
export function pickLanguage(preferred: readonly string[]): CoreLanguage {
  for (const p of preferred) {
    const base = p.split("-")[0]!.toLowerCase();
    if ((CORE_LANGUAGES as readonly string[]).includes(base)) return base as CoreLanguage;
  }
  return DEFAULT_LANGUAGE;
}

/** A fresh i18next instance per request (web) or per app (mobile). */
export async function createI18n(language: string = DEFAULT_LANGUAGE): Promise<i18n> {
  const instance = i18next.createInstance();
  await instance.init({
    lng: language,
    fallbackLng: DEFAULT_LANGUAGE,
    ns: NAMESPACES,
    defaultNS: "common",
    resources,
    interpolation: { escapeValue: false },
    returnNull: false,
  });
  return instance;
}
