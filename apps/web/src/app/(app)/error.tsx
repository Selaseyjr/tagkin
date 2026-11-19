"use client";

import { Screen, Spacer } from "@/components/ui/Screen";

export default function AppError({ reset }: { error: Error; reset: () => void }) {
  return (
    <Screen>
      <Spacer />
      <h1 className="center">Something went wrong</h1>
      <p className="m center">Your tags still work for finders. Try again in a moment.</p>
      <button type="button" className="btn pri" onClick={reset}>
        Try again
      </button>
      <Spacer />
    </Screen>
  );
}
