// Lint rules for the shared packages. Apps use their own framework configs
// (apps/web: eslint-config-next, apps/mobile: eslint-config-expo).
import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  { ignores: ["**/node_modules/**", "**/dist/**", "apps/**", "docs/**"] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    // Build scripts run in Node.
    files: ["**/scripts/**/*.mjs"],
    languageOptions: { globals: { process: "readonly", console: "readonly" } },
  },
);
