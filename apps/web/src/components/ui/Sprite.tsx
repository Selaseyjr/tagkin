/** The prototype's icon sprite (docs/design/build_screens.py SVG), rendered once per page. */
export function Sprite() {
  return (
    <svg width="0" height="0" style={{ position: "absolute" }} aria-hidden="true">
      <defs>
        <mask id="mk" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="64">
          <rect width="64" height="64" fill="#fff" />
          <circle cx="22" cy="32" r="5" fill="#000" />
          <path d="M31 14 h5 v20 l8 -8 h7 l-9 9 l10 13 h-7 l-7 -9 l-2 2 v7 h-5 Z" fill="#000" />
        </mask>
        <symbol id="mark" viewBox="0 0 64 64">
          <g mask="url(#mk)">
            <path fill="currentColor" stroke="currentColor" strokeWidth="4" strokeLinejoin="round" d="M8 23 L23 9 H56 V55 H23 L8 41 Z" />
          </g>
        </symbol>
        <symbol id="i-tag" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" d="M3 9 8 4h13v16H8l-5-5Z" />
          <circle cx="9" cy="12" r="1.6" fill="currentColor" />
        </symbol>
        <symbol id="i-chat" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" d="M4 5h16v11H9l-5 4Z" />
        </symbol>
        <symbol id="i-box" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5Z M3 7.5 12 12l9-4.5 M12 12v9" />
        </symbol>
        <symbol id="i-user" viewBox="0 0 24 24">
          <circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" strokeWidth="2" />
          <path fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6" />
        </symbol>
        <symbol id="i-sun" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="4.5" fill="none" stroke="currentColor" strokeWidth="2" />
          <path stroke="currentColor" strokeWidth="2" strokeLinecap="round" d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" />
        </symbol>
        <symbol id="i-moon" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" strokeWidth="2" strokeLinejoin="round" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z" />
        </symbol>
        <symbol id="i-auto" viewBox="0 0 24 24">
          <circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" strokeWidth="2" />
          <path fill="currentColor" d="M12 3.5a8.5 8.5 0 0 1 0 17Z" />
        </symbol>
        <symbol id="i-qr" viewBox="0 0 24 24">
          <path fill="none" stroke="currentColor" strokeWidth="2" d="M4 4h6v6H4ZM14 4h6v6h-6ZM4 14h6v6H4Z" />
          <path fill="currentColor" d="M14 14h3v3h-3ZM17 17h3v3h-3ZM14 19h2v1h-2ZM19 14h1v2h-1Z" />
        </symbol>
        <symbol id="lock" viewBox="0 0 16 16">
          <path fill="currentColor" d="M5 7V5a3 3 0 1 1 6 0v2h.5A1.5 1.5 0 0 1 13 8.5v5A1.5 1.5 0 0 1 11.5 15h-7A1.5 1.5 0 0 1 3 13.5v-5A1.5 1.5 0 0 1 4.5 7H5Zm1.5 0h3V5a1.5 1.5 0 1 0-3 0v2Z" />
        </symbol>
      </defs>
    </svg>
  );
}

export type IconName = "mark" | "i-tag" | "i-chat" | "i-box" | "i-user" | "i-sun" | "i-moon" | "i-auto" | "i-qr" | "lock";

export function Icon({ name, size = 24 }: { name: IconName; size?: number }) {
  return (
    <svg width={size} height={size} aria-hidden="true">
      <use href={`#${name}`} />
    </svg>
  );
}
