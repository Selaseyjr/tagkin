"use client";

export function ShareButton({ url, title }: { url: string; title: string }) {
  return (
    <button
      type="button"
      className="btn sec"
      onClick={async () => {
        if (navigator.share) await navigator.share({ title, url }).catch(() => {});
        else await navigator.clipboard.writeText(url);
      }}
    >
      Share
    </button>
  );
}
