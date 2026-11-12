export function Mark({ size = 28 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 64 64" aria-hidden="true">
      <path
        fill="currentColor"
        fillRule="evenodd"
        d="M23.0 9 H56 V55 H23 L8 41 V23 Z M22 27 a5 5 0 1 0 0.01 0 Z M31 14 h5 v20 l8 -8 h7 l-9 9 l10 13 h-7 l-7 -9 l-2 2 v7 h-5 Z"
      />
    </svg>
  );
}
