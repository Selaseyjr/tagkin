import { describe, expect, it } from "vitest";
import {
  canCancelOrder,
  canChangeAddress,
  canEditItem,
  canReportProblem,
  nextTagState,
} from "./states";

describe("tag state machine", () => {
  it("follows SYSTEM-LOGIC 3", () => {
    expect(nextTagState("unlinked", "set_up")).toBe("normal");
    expect(nextTagState("normal", "mark_lost")).toBe("lost");
    expect(nextTagState("lost", "finder_report")).toBe("return_active");
    expect(nextTagState("return_active", "mark_returned")).toBe("normal");
    expect(nextTagState("normal", "retire")).toBe("retired");
  });
  it("rejects illegal moves", () => {
    expect(nextTagState("retired", "retire")).toBeNull();
    expect(nextTagState("normal", "found_it_myself")).toBeNull();
    expect(nextTagState("unclaimed", "mark_lost")).toBeNull();
    expect(nextTagState("retired", "activate")).toBeNull();
  });
  it("locks item details only during a return", () => {
    expect(canEditItem("normal")).toBe(true);
    expect(canEditItem("lost")).toBe(true);
    expect(canEditItem("return_active")).toBe(false);
  });
});

describe("order rules (BUSINESS-RULES 3d)", () => {
  it("cancel before printing, address until shipped, problems after delivery", () => {
    expect(canCancelOrder("sent_to_partner")).toBe(true);
    expect(canCancelOrder("in_production")).toBe(false);
    expect(canChangeAddress("quality_check")).toBe(true);
    expect(canChangeAddress("shipped")).toBe(false);
    expect(canChangeAddress("pending_payment")).toBe(false);
    expect(canReportProblem("delivered")).toBe(true);
  });
});
