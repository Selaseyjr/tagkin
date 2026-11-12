import "server-only";
import { redirect } from "next/navigation";
import { ownerClient } from "./supabase/server";

export const DEMO_EMAIL = "demo@tagkin.app";

/** Signed-in owner or a redirect to sign-in. */
export async function requireOwner() {
  const db = await ownerClient();
  const { data } = await db.auth.getUser();
  if (!data.user) redirect("/signin");
  return { db, user: data.user };
}

export const STATE_BADGE: Record<string, { text: string; cls: string }> = {
  normal: { text: "Active", cls: "badge b-n" },
  lost: { text: "Lost", cls: "badge b-l" },
  return_active: { text: "Return active", cls: "badge b-r" },
  unlinked: { text: "Set up", cls: "badge b-w" },
  unclaimed: { text: "Unclaimed", cls: "badge b-n" },
  retired: { text: "Retired", cls: "badge b-n" },
};

export type OwnerTag = {
  code: string;
  state: string;
  product: string;
  type: "item" | "travel" | "pet" | null;
  name: string;
  photo: string | null;
};

type Row = {
  code: string;
  state: string;
  product: string;
  type: OwnerTag["type"];
  items:
    | { name: string; photo_path: string | null }
    | { name: string; photo_path: string | null }[]
    | null;
};

export function toTag(r: Row): OwnerTag {
  const item = Array.isArray(r.items) ? r.items[0] : r.items;
  return {
    code: r.code,
    state: r.state,
    product: r.product,
    type: r.type,
    name: item?.name ?? `Blank ${r.product.replace("_", " ")}`,
    photo: item?.photo_path ?? null,
  };
}

export async function loadTag(code: string) {
  const { db, user } = await requireOwner();
  const { data } = await db
    .from("tags")
    .select("code, state, product, type, items(name, photo_path)")
    .eq("code", code)
    .maybeSingle();
  return { db, user, tag: data ? toTag(data as Row) : null };
}

/** Owner has an open return (unread conversation) anywhere: drives the Messages dot. */
export async function hasOpenReturn() {
  const { db } = await requireOwner();
  const { count } = await db
    .from("returns")
    .select("id", { count: "exact", head: true })
    .neq("state", "closed");
  return (count ?? 0) > 0;
}

export const when = (iso: string) =>
  new Date(iso).toLocaleString("en-GB", {
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
