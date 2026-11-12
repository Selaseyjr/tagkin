"use server";

import { redirect } from "next/navigation";
import { z } from "zod";
import { adminClient } from "@/lib/supabase/admin";
import { ownerClient } from "@/lib/supabase/server";
import { clientKey } from "@/lib/request";
import { DEMO_EMAIL } from "@/lib/owner";

export type SignInState = { step: "email" | "code"; email?: string; error?: string };

export async function sendCode(_prev: SignInState, form: FormData): Promise<SignInState> {
  const email = z.email().safeParse(
    String(form.get("email") ?? "")
      .trim()
      .toLowerCase(),
  );
  if (!email.success) return { step: "email", error: "Enter a valid email." };
  if (email.data === DEMO_EMAIL)
    return { step: "email", error: "Use “Try the owner side” for the demo account." };
  const db = await ownerClient();
  // Invite-only demo: no new accounts are created here.
  const { error } = await db.auth.signInWithOtp({
    email: email.data,
    options: { shouldCreateUser: false },
  });
  if (error)
    return {
      step: "email",
      email: email.data,
      error: "We couldn't send a code to that email. Is it invited to the demo?",
    };
  return { step: "code", email: email.data };
}

export async function verifyCode(prev: SignInState, form: FormData): Promise<SignInState> {
  const email = String(form.get("email") ?? prev.email ?? "");
  const code = String(form.get("code") ?? "").replace(/\D/g, "");
  if (code.length !== 6 || !email)
    return { step: "code", email, error: "Enter the 6-digit code from the email." };
  const db = await ownerClient();
  const { error } = await db.auth.verifyOtp({ email, token: code, type: "email" });
  if (error)
    return { step: "code", email, error: "That code didn't work. Check it or ask for a new one." };
  redirect("/my-tags");
}

/** Sample account sign-in for tagkin.app/preview (unlisted; docs/sprints/DEMO-SPRINT.md). */
export async function signInSample() {
  const admin = adminClient();
  const { data: allowed } = await admin.rpc("check_rate_limit", {
    p_key: await clientKey("demo"),
    p_max: 30,
    p_window_seconds: 3600,
  });
  if (!allowed) redirect("/signin");
  const { data, error } = await admin.auth.admin.generateLink({
    type: "magiclink",
    email: DEMO_EMAIL,
  });
  if (error || !data.properties?.hashed_token) redirect("/signin");
  const db = await ownerClient();
  const res = await db.auth.verifyOtp({
    type: "magiclink",
    token_hash: data.properties.hashed_token,
  });
  if (res.error) redirect("/signin");
  redirect("/my-tags");
}

export async function signOut() {
  const db = await ownerClient();
  await db.auth.signOut();
  redirect("/");
}
