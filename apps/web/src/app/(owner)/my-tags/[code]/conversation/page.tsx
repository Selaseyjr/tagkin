import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { loadTag } from "@/lib/owner";
import { ownerReply } from "../actions";
import { Thread } from "./Thread";

async function Conversation({ params }: { params: Promise<{ code: string }> }) {
  const { code } = await params;
  const { db, tag } = await loadTag(code);
  if (!tag) notFound();
  const { data: ret } = await db
    .from("returns")
    .select("id")
    .eq("tag_code", code)
    .neq("state", "closed")
    .maybeSingle();
  const { data: msgs } = ret
    ? await db
        .from("messages")
        .select("sender, body, created_at")
        .eq("return_id", ret.id)
        .order("created_at")
    : { data: [] };
  return (
    <AppScreen
      back={{ href: `/my-tags/${code}`, label: tag.name }}
      right={<span className="badge b-r">Return active</span>}
    >
      {ret ? (
        <>
          <Thread
            code={code}
            initial={(msgs ?? []).map((m) => ({ from: m.sender, body: m.body, at: m.created_at }))}
            reply={ownerReply.bind(null, code)}
          />
          <Link className="btn sec" href={`/my-tags/${code}/returned`}>
            Got it back? Mark as returned
          </Link>
        </>
      ) : (
        <p className="note info">This return is closed.</p>
      )}
    </AppScreen>
  );
}

export default function Page({ params }: { params: Promise<{ code: string }> }) {
  return (
    <Suspense fallback={<div className="app" />}>
      <Conversation params={params} />
    </Suspense>
  );
}
