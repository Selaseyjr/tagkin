import "server-only";
import { z } from "zod";

const schema = z.object({
  NEXT_PUBLIC_SUPABASE_URL: z.url(),
  NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY: z.string().min(10),
  SUPABASE_SECRET_KEY: z.string().min(10),
});

let cached: z.infer<typeof schema> | null = null;

/** Server environment, checked on first use (fails loudly instead of misbehaving). */
export function serverEnv() {
  cached ??= schema.parse(process.env);
  return cached;
}
