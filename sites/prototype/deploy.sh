#!/usr/bin/env bash
# Publishes the clickable design prototype to prototype.tagkin.app (Vercel project tagkin-prototype).
# The prototypes are built in docs/design; this copies them next to the landing page and deploys.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
design="$here/../../docs/design"
out="$(mktemp -d)"
cp "$here/index.html" "$here/vercel.json" "$out/"
cp "$design/owner-prototype.html" "$out/owner.html"
cp "$design/finder-prototype.html" "$out/finder.html"
cp "$design/desktop-prototype.html" "$out/desktop.html"
mkdir -p "$out/media"
cp "$here/../../media/"tagkin-*-experience.{mp4,jpg} "$here/../../media/"tagkin-teaser{.mp4,-silent.mp4,.jpg} "$out/media/"
[ -d "$here/.vercel" ] && cp -R "$here/.vercel" "$out/"
cd "$out"
pnpm dlx vercel@latest deploy --prod --yes --scope selasey
[ -d "$out/.vercel" ] && cp -R "$out/.vercel" "$here/"
