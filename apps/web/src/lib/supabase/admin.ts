import "server-only";
import { createClient } from "@supabase/supabase-js";
import type { Database } from "@tagkin/shared";
import { serverEnv } from "../env";

/** Service-role client for finder-side functions. Server only; never sent to browsers. */
export function adminClient() {
  const env = serverEnv();
  return createClient<Database>(env.NEXT_PUBLIC_SUPABASE_URL, env.SUPABASE_SECRET_KEY, {
    auth: { persistSession: false, autoRefreshToken: false },
  });
}
