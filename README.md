# Tagkin

QR tags for bags, keys, gear and pets. Whoever finds something scans the tag and alerts the owner, privately. No app needed for finders.

**Status:** design, specification, backlog and technical design done (print partner after samples). Build started: Sprint 0.

- [Product brief](docs/PRODUCT-BRIEF.md) · [Business rules](docs/BUSINESS-RULES.md) · [System logic](docs/SYSTEM-LOGIC.md)
- [Roadmap and product owner flow](docs/ROADMAP.md) · [Backlog](docs/BACKLOG.md) · [Technical design](docs/TECH-DESIGN.md) · [Decisions](docs/adr/README.md)
- Design: `docs/design/tagkin-screens.html` (hand-off), `tagkin-showcase.html`, prototypes

## Develop

Node 24 (see `.nvmrc`) and pnpm through Corepack.

```bash
fnm use            # or any Node version manager
corepack enable
pnpm install
pnpm check         # lint, typecheck, tests
pnpm build
```

| Path | What |
|---|---|
| `apps/web` | Next.js: finder pages, website, owner web, API routes |
| `apps/mobile` | Expo app for owners (bundle id `app.tagkin`, scheme `tagkin://`) |
| `packages/shared` | Rules shared everywhere: code alphabet, limits, shape fit, schemas |
| `packages/tokens` | Design tokens from `docs/brand/tokens.css` |
| `packages/i18n` | Core languages and translation files |
