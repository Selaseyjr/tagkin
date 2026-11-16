import Link from "next/link";
import { Screen, Spacer } from "@/components/ui/Screen";

export default function NotFound() {
  return (
    <Screen>
      <Spacer />
      <h1 className="center">Page not found</h1>
      <p className="m center">This page doesn&apos;t exist or has moved.</p>
      <Link className="btn pri" href="/tags">Go to My tags</Link>
      <Spacer />
    </Screen>
  );
}
