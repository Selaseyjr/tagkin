// Generates packages/tokens/src/generated.ts and src/tokens.css from docs/brand/tokens.css,
// the single source of truth. Run: pnpm --filter @tagkin/tokens generate
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
export const SOURCE = resolve(here, "../../../docs/brand/tokens.css");

function vars(block) {
  const out = {};
  for (const m of block.matchAll(/--tk-([a-z0-9-]+)\s*:\s*([^;]+);/g)) out[m[1]] = m[2].trim();
  return out;
}
const camel = (s) => s.replace(/-([a-z0-9])/g, (_, c) => c.toUpperCase());
const px = (v) => (/^\d+(\.\d+)?px$/.test(v) ? Number(v.slice(0, -2)) : v);
const ms = (v) => (/^\d+ms$/.test(v) ? Number(v.slice(0, -2)) : v);

export function build(css) {
  const clean = css.replace(/\/\*[\s\S]*?\*\//g, "");
  const light = vars(clean.match(/:root\s*\{([\s\S]*?)\}/)[1]);
  const dark = vars(clean.match(/:root\[data-theme="dark"\]\s*\{([\s\S]*?)\}/)[1]);
  const colorKeys = Object.keys(dark).filter((k) => k !== "shadow");
  const pick = (src, prefix, f = (v) => v) =>
    Object.fromEntries(
      Object.entries(src)
        .filter(([k]) => k.startsWith(prefix))
        .map(([k, v]) => [camel(k.slice(prefix.length)), f(v)]),
    );
  const tokens = {
    color: {
      light: Object.fromEntries(colorKeys.map((k) => [camel(k), light[k]])),
      dark: Object.fromEntries(colorKeys.map((k) => [camel(k), dark[k]])),
    },
    shadow: { light: light.shadow, dark: dark.shadow },
    font: pick(light, "font-"),
    text: pick(light, "text-", px),
    space: pick(light, "space-", px),
    radius: pick(light, "radius-", px),
    motion: { ease: light.ease, fast: ms(light.fast), slow: ms(light.slow) },
    tap: px(light.tap),
  };
  const ts =
    "// Generated from docs/brand/tokens.css by scripts/generate.mjs. Do not edit.\n" +
    `export const tokens = ${JSON.stringify(tokens, null, 2)} as const;\n\n` +
    "export type Tokens = typeof tokens;\nexport type ColorScheme = keyof typeof tokens.color;\nexport type ColorToken = keyof typeof tokens.color.light;\n";
  return {
    ts,
    css: "/* Copied from docs/brand/tokens.css by scripts/generate.mjs. Do not edit. */\n" + css,
  };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const out = build(readFileSync(SOURCE, "utf8"));
  writeFileSync(resolve(here, "../src/generated.ts"), out.ts);
  writeFileSync(resolve(here, "../src/tokens.css"), out.css);
  console.log("tokens generated");
}
