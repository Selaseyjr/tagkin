# Working on this project with Claude

Read docs/PRODUCT-BRIEF.md first. It is the single source of truth: add every decision and a change-log line in the same turn it is made.

## About the owner
- Selasey Gbeddy, Technical Product Owner & Analyst (AI & Automation), Darmstadt. Building this as a portfolio product, run like a real product owner, step by step.
- Public copy (READMEs, captions, store text): minimal, confident, captivating. No long explanations.
- No AI co-author lines in commits.
- Check every build against professional standards before handover; verify, don't assume.
- Suggest better options and flag risks proactively; ask when a wording or decision is unclear.

## Where things are
- GitHub: Selaseyjr/tagkin (private while building). gh has two accounts; switch to Selaseyjr to push, then back to adensa-admin.
- Figma: account selaseygbeddy@gmail.com, Starter plan (MCP tool-call limit was hit on 6 Nov; Chrome export works when signed in).
- Portfolio: ~/Documents/career-workspace/portfolio/site (Vercel project selasey-gbeddy).

## Code
- Monorepo: pnpm workspaces + Turborepo; Node 24 via fnm (`eval "$(fnm env)" && fnm use 24` in each shell); pnpm through Corepack.
- Before any handover: `pnpm check` and `pnpm build` must pass; add Expo packages with `pnpm expo install` in apps/mobile.
- Merge only with every check green: `gh pr checks <n> --watch && gh pr merge ...` (the && stops the merge on any failure). Build without local env files before handing over (`mv apps/web/.env.local /tmp` while building).
- One branch and pull request per Sprint item (`s0/...`, later `tk-<n>-...`); never push to main directly.

## Business rules
docs/BUSINESS-RULES.md lists the rules Tagkin runs by. Check new features against it, and update it in the same turn as any rule change.

## How to check work
- Walk every journey as the user, including the moments a provider handles (payment, email, maps, translation, push), before calling a design or build done.
- Whenever a rule changes, search all screens and documents for text that contradicts it.
- docs/SYSTEM-LOGIC.md is the engineering view (data, states, events, providers); keep it in step with the screens and rules.

## Roadmap
docs/ROADMAP.md lists every open item by stage with its trigger. At the start of each task, check which stage is active and tell Selasey when a stage's trigger is reached.

## Product owner flow
Follow the 10-step flow in docs/ROADMAP.md (discover, validate, design, specify, backlog, technical design, build, test, launch, measure). Name the current step when proposing work.

## Phase status
1 Define: done. 2 Validate: done (3 conversations; owner prototype tested by Eli on 12 Nov, 5-person round skipped). Product owner flow steps 1 to 5 done (discover, validate, design, specify, backlog). Step 6 (technical design): 11 of 12 decided (print partner after samples). Step 7 (build) started: M1 Ready, Sprint 0 in docs/sprints. Target: App Store and Google Play.
