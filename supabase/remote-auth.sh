#!/usr/bin/env bash
# Applies Tagkin's auth settings and sign-in email to the hosted project through the
# Supabase Management API. SMTP credentials are not touched (they live only in the dashboard).
# Needs SUPABASE_ACCESS_TOKEN (token with Auth Config read-write) and PROJECT_REF.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
body="$(python3 - "$here/templates/sign-in-code.html" <<'PY'
import json, sys
html = open(sys.argv[1]).read()
print(json.dumps({
  "site_url": "https://tagkin.app",
  "uri_allow_list": "https://tagkin.app/**,https://*-selasey.vercel.app/**",
  "mailer_otp_length": 6,
  "mailer_otp_exp": 600,
  "smtp_max_frequency": 30,
  "mailer_subjects_magic_link": "Your Tagkin sign-in code",
  "mailer_templates_magic_link_content": html,
  "mailer_subjects_confirmation": "Your Tagkin sign-in code",
  "mailer_templates_confirmation_content": html,
}))
PY
)"
if [ "${DRY_RUN:-false}" = "true" ]; then
  curl -sf -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
    "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" -o /dev/null
  echo "Auth config readable; would apply: $(echo "$body" | python3 -c 'import json,sys;print(sorted(json.load(sys.stdin)))')"
else
  code=$(curl -s -X PATCH -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" -H "Content-Type: application/json" \
    "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" -d "$body" -o /tmp/auth-response.json -w "%{http_code}")
  if [ "$code" -ge 300 ]; then
    echo "Auth config update failed (HTTP $code):"; head -c 600 /tmp/auth-response.json; echo; exit 1
  fi
  echo "Auth config applied."
fi
