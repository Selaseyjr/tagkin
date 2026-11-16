"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";

export function SplashForward({ to, ms = 1200 }: { to: string; ms?: number }) {
  const router = useRouter();
  useEffect(() => {
    const t = setTimeout(() => router.replace(to), ms);
    return () => clearTimeout(t);
  }, [router, to, ms]);
  return null;
}
