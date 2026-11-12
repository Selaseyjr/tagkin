// Core languages (BUSINESS-RULES 8.3). Translation files arrive in M5 (TK-92).
export const CORE_LANGUAGES = ["en", "de", "fr", "nl", "pl", "es", "it"] as const;
export type CoreLanguage = (typeof CORE_LANGUAGES)[number];
