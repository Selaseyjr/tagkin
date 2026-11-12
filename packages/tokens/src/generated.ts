// Generated from docs/brand/tokens.css by scripts/generate.mjs. Do not edit.
export const tokens = {
  "color": {
    "light": {
      "bg": "#f6f8f7",
      "surface": "#ffffff",
      "sunken": "#edf1ef",
      "line": "#dbe3df",
      "ink": "#0b1712",
      "ink2": "#4f5e57",
      "brand": "#00c48c",
      "brandPress": "#00ab7a",
      "onBrand": "#03261a",
      "brandSoft": "#d9f7ec",
      "brandText": "#007a57",
      "lost": "#e02a17",
      "lostSoft": "#ffe5e1",
      "onLost": "#ffffff",
      "lostText": "#c62d1b",
      "warn": "#8a5a00",
      "warnSoft": "#fdf1d6",
      "ok": "#007a57"
    },
    "dark": {
      "bg": "#07110d",
      "surface": "#0f1b16",
      "sunken": "#16251f",
      "line": "#24372f",
      "ink": "#eefaf5",
      "ink2": "#9db3aa",
      "brand": "#1fe0a6",
      "brandPress": "#5cebc0",
      "onBrand": "#03261a",
      "brandSoft": "#0f3a2c",
      "brandText": "#1fe0a6",
      "lost": "#ff6b57",
      "lostSoft": "#3a1712",
      "onLost": "#1f0703",
      "lostText": "#ff8a7a",
      "warn": "#f2c66b",
      "warnSoft": "#3a2f16",
      "ok": "#1fe0a6"
    }
  },
  "shadow": {
    "light": "0 1px 2px rgb(20 32 28 / .06), 0 6px 20px rgb(20 32 28 / .06)",
    "dark": "0 1px 2px rgb(0 0 0 / .4), 0 8px 24px rgb(0 0 0 / .35)"
  },
  "font": {
    "brand": "\"Bricolage Grotesque\", system-ui, sans-serif",
    "display": "\"Geist\", system-ui, -apple-system, sans-serif",
    "body": "\"Geist\", system-ui, -apple-system, \"Segoe UI\", sans-serif"
  },
  "text": {
    "xs": 12,
    "sm": 14,
    "md": 16,
    "lg": 20,
    "xl": 26,
    "2xl": 34
  },
  "space": {
    "1": 4,
    "2": 8,
    "3": 12,
    "4": 16,
    "5": 24,
    "6": 32,
    "7": 48
  },
  "radius": {
    "sm": 8,
    "md": 14,
    "lg": 22
  },
  "motion": {
    "ease": "cubic-bezier(.2, .8, .2, 1)",
    "fast": 140,
    "slow": 280
  },
  "tap": 52
} as const;

export type Tokens = typeof tokens;
export type ColorScheme = keyof typeof tokens.color;
export type ColorToken = keyof typeof tokens.color.light;
