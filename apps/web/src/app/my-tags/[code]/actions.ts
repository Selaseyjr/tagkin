"use server";

import { revalidatePath } from "next/cache";
import { fits, type TagType } from "@tagkin/shared";
import { requireOwner } from "@/lib/owner";

async function call(fn: "mark_lost" | "mark_found" | "mark_returned", code: string) {
  const { db } = await requireOwner();
  await db.rpc(fn, { p_code: code });
  revalidatePath(`/my-tags/${code}`);
  revalidatePath("/my-tags");
}

export async function markLost(code: string) {
  await call("mark_lost", code);
}
export async function markFound(code: string) {
  await call("mark_found", code);
}
export async function markReturned(code: string) {
  await call("mark_returned", code);
}

export async function ownerReply(code: string, form: FormData) {
  const body = String(form.get("body") ?? "").trim();
  if (!body) return;
  const { db } = await requireOwner();
  await db.rpc("owner_reply", { p_code: code, p_body: body.slice(0, 1000) });
  revalidatePath(`/my-tags/${code}`);
}

export async function setUpBlank(
  code: string,
  product: string,
  form: FormData,
): Promise<{ error?: string }> {
  const type = String(form.get("type") ?? "") as TagType;
  const name = String(form.get("name") ?? "").trim();
  const message =
    String(form.get("message") ?? "").trim() ||
    "Found me? Thank you! Tap below to tell my owner where I am.";
  if (!fits(product as never, type)) return { error: "Choose what the tag goes on." };
  if (name.length < 2 || name.length > 40) return { error: "Give it a name, 2 to 40 characters." };
  const { db } = await requireOwner();
  const { error } = await db.rpc("setup_blank_tag", {
    p_code: code,
    p_type: type,
    p_name: name,
    p_finder_message: message,
  });
  if (error) return { error: "That didn't work. Check the details and try again." };
  revalidatePath(`/my-tags/${code}`);
  revalidatePath("/my-tags");
  return {};
}
