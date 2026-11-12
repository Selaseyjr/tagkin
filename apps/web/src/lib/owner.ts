import "server-only";
import { redirect } from "next/navigation";
import { ownerClient } from "./supabase/server";

export const DEMO_EMAIL = "demo@tagkin.app";

/** Signed-in owner or a redirect to sign-in. */
export async function requireOwner() {
  const db = await ownerClient();
  const { data } = await db.auth.getUser();
  if (!data.user) redirect("/signin");
  return { db, user: data.user, isDemo: data.user.email === DEMO_EMAIL };
}

export const STATE_LABEL: Record<string, { text: string; cls: string }> = {
  normal: { text: "Active", cls: "badge" },
  lost: { text: "Lost", cls: "badge lost" },
  return_active: { text: "Return active", cls: "badge ret" },
  unlinked: { text: "Set up", cls: "badge set" },
  unclaimed: { text: "Unclaimed", cls: "badge" },
  retired: { text: "Retired", cls: "badge" },
};
