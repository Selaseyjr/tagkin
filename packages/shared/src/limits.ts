/** Validation limits (SYSTEM-LOGIC 6). */
export const LIMITS = {
  itemName: { min: 2, max: 40 },
  description: { max: 120 },
  finderMessage: { min: 1, max: 160 },
  giftNote: { min: 1, max: 160 },
  label: { max: 12 },
  statusUpdate: { max: 60 },
  careNotes: { max: 300 },
  chatMessage: { min: 1, max: 1000 },
  photo: {
    maxBytes: 10 * 1024 * 1024,
    maxEdge: 1600,
    types: ["image/jpeg", "image/png", "image/webp", "image/heic"],
  },
  emailCode: { length: 6, validMinutes: 10, attempts: 5 },
  activationPin: { length: 6, attempts: 5, lockMinutes: 15 },
  handoverCode: { length: 6, attempts: 5, lockMinutes: 15 },
  codeLookupsPerHourPerIp: 20,
  testModeMinutes: 10,
  undoSeconds: 5,
  returnAutoCloseDays: 14,
  freeShippingFromCents: 1500,
} as const;
