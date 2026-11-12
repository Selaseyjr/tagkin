#!/usr/bin/env bash
# Read-only check that the hosted project's sign-in settings match the repo.
# Settings are applied once in the Supabase dashboard (changing them needs an admin-level token,
# which CI deliberately does not have). Needs SUPABASE_ACCESS_TOKEN (Auth Config read) and PROJECT_REF.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
curl -sf -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" -o /tmp/auth.json
python3 - "$here/templates/sign-in-code.html" <<'PY'
import json, re, sys
norm = lambda h: re.sub(r"\s+", " ", re.sub(r">\s+<", "><", h or "")).strip()
cfg = json.load(open("/tmp/auth.json"))
want = norm(open(sys.argv[1]).read())
checks = {
    "site_url is https://tagkin.app": cfg.get("site_url") == "https://tagkin.app",
    "code length 6": cfg.get("mailer_otp_length") == 6,
    "code valid 10 minutes": cfg.get("mailer_otp_exp") == 600,
    "sign-in subject": cfg.get("mailer_subjects_magic_link") == "Your Tagkin sign-in code",
    "sign-up subject": cfg.get("mailer_subjects_confirmation") == "Your Tagkin sign-in code",
    "sign-in template matches the repo": norm(cfg.get("mailer_templates_magic_link_content")) == want,
    "sign-up template matches the repo": norm(cfg.get("mailer_templates_confirmation_content")) == want,
    "custom SMTP is on (Brevo)": bool(cfg.get("smtp_host")),
}
for name, ok in checks.items():
    print(("ok    " if ok else "DRIFT ") + name)
if not all(checks.values()):
    print("\nHosted auth settings differ from the repo. Update them in the Supabase dashboard "
          "(Authentication → Emails, Sign In / Providers → Email, URL Configuration).")
    sys.exit(1)
PY
