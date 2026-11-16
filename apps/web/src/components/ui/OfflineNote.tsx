"use client";

import { useSyncExternalStore } from "react";

function subscribe(cb: () => void) {
  window.addEventListener("online", cb);
  window.addEventListener("offline", cb);
  return () => {
    window.removeEventListener("online", cb);
    window.removeEventListener("offline", cb);
  };
}

/** State 4 · Offline (err-offline): shown above the content while the device has no connection. */
export function OfflineNote() {
  const offline = useSyncExternalStore(subscribe, () => !navigator.onLine, () => false);
  if (!offline) return null;
  return (
    <div className="note offl" role="status">
      You&apos;re offline. Your tags still work for finders. New messages appear when you&apos;re back online.
    </div>
  );
}
