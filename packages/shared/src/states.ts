/** Tag and order state machines (SYSTEM-LOGIC 3). Mirrored by Postgres functions. */

export const TAG_STATES = [
  "unclaimed",
  "unlinked",
  "normal",
  "lost",
  "return_active",
  "retired",
] as const;
export type TagState = (typeof TAG_STATES)[number];

export type TagEvent =
  | "activate" // unclaimed → normal (PIN)
  | "set_up" // unlinked → normal (blank tag)
  | "mark_lost"
  | "found_it_myself"
  | "finder_report"
  | "mark_returned"
  | "auto_close" // 14 days without messages
  | "retire";

const T: Record<TagEvent, Partial<Record<TagState, TagState>>> = {
  activate: { unclaimed: "normal" },
  set_up: { unlinked: "normal" },
  mark_lost: { normal: "lost" },
  found_it_myself: { lost: "normal" },
  finder_report: { normal: "return_active", lost: "return_active", return_active: "return_active" },
  mark_returned: { return_active: "normal" },
  auto_close: { return_active: "normal" },
  retire: {
    unclaimed: "retired",
    unlinked: "retired",
    normal: "retired",
    lost: "retired",
    return_active: "retired",
  },
};

/** Next state, or null when the event is not allowed in this state. */
export function nextTagState(state: TagState, event: TagEvent): TagState | null {
  return T[event][state] ?? null;
}

/** Name, photo and description: editable in normal and lost, locked during a return (rule 4.4). */
export function canEditItem(state: TagState): boolean {
  return state === "normal" || state === "lost";
}

export const ORDER_STAGES = [
  "pending_payment",
  "paid",
  "sent_to_partner",
  "in_production",
  "quality_check",
  "shipped",
  "out_for_delivery",
  "delivered",
] as const;
export type OrderStage = (typeof ORDER_STAGES)[number];

export const ORDER_EXCEPTIONS = [
  "reprint",
  "delayed",
  "delivery_failed",
  "problem_reported",
] as const;
export type OrderException = (typeof ORDER_EXCEPTIONS)[number];

const idx = (s: OrderStage) => ORDER_STAGES.indexOf(s);

/** Cancel with a full refund until printing starts (rule 3d.2). */
export function canCancelOrder(stage: OrderStage): boolean {
  return stage === "paid" || stage === "sent_to_partner";
}

/** Address can change until the order ships (rule 3d.3). */
export function canChangeAddress(stage: OrderStage): boolean {
  return idx(stage) >= idx("paid") && idx(stage) < idx("shipped");
}

/** Problems are reported after delivery (rule 3d.6). */
export function canReportProblem(stage: OrderStage): boolean {
  return stage === "delivered";
}
