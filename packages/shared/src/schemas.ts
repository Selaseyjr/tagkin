import { z } from "zod";
import { LIMITS } from "./limits";
import { parseCode } from "./codes";
import { PRODUCTS, TAG_TYPES, fits } from "./shape-fit";

const URL_PATTERN =
  /(https?:\/\/|www\.)\S+|\b[a-z0-9-]+\.(com|de|net|org|io|app|me|link|ly|co|info|xyz)\b/i;
const EMAIL_PATTERN = /[^\s@]+@[^\s@]+\.[^\s@]+/;
const LONG_NUMBER = /\d[\d\s\-/()]{4,}\d/;
const DATE_OR_TIME =
  /\b\d{1,2}[./-]\d{1,2}([./-]\d{2,4})?\b|\b\d{1,2}:\d{2}\b|\b(today|tomorrow|tonight|yesterday|heute|morgen|gestern|monday|tuesday|wednesday|thursday|friday|saturday|sunday|montag|dienstag|mittwoch|donnerstag|freitag|samstag|sonntag|jan(uary|uar)?|feb(ruary|ruar)?|mar(ch)?|märz|apr(il)?|may|mai|june?|juni|july?|juli|aug(ust)?|sep(t|tember)?|oct(ober)?|okt(ober)?|nov(ember)?|dec(ember)?|dez(ember)?)\b/i;

/** Links are never allowed in public text on finder pages (audit C2). */
export function containsUrl(text: string): boolean {
  return URL_PATTERN.test(text);
}

const trimmed = (min: number, max: number) => z.string().trim().min(min).max(max);

export const itemNameSchema = trimmed(LIMITS.itemName.min, LIMITS.itemName.max);
export const descriptionSchema = z.string().trim().max(LIMITS.description.max);
export const finderMessageSchema = trimmed(
  LIMITS.finderMessage.min,
  LIMITS.finderMessage.max,
).refine((t) => !containsUrl(t), { message: "links_not_allowed" });
export const labelSchema = z
  .string()
  .trim()
  .max(LIMITS.label.max)
  .refine((t) => !EMAIL_PATTERN.test(t) && !LONG_NUMBER.test(t) && !containsUrl(t), {
    message: "no_contact_details",
  });
export const statusUpdateSchema = z
  .string()
  .trim()
  .min(1)
  .max(LIMITS.statusUpdate.max)
  .refine((t) => !DATE_OR_TIME.test(t), { message: "no_dates_or_times" });
export const careNotesSchema = z.string().trim().max(LIMITS.careNotes.max);
export const chatMessageSchema = trimmed(LIMITS.chatMessage.min, LIMITS.chatMessage.max);

export const tagCodeSchema = z.string().transform((v, ctx) => {
  const p = parseCode(v);
  if (!p.ok) {
    ctx.addIssue({
      code: "custom",
      message: p.reason === "check" ? "check_the_code" : "not_a_code",
    });
    return z.NEVER;
  }
  return p.code;
});

export const productSchema = z.enum(PRODUCTS);
export const tagTypeSchema = z.enum(TAG_TYPES);

/** A product and type pair must fit (BUSINESS-RULES 3c). */
export const productTypeSchema = z
  .object({ product: productSchema, type: tagTypeSchema })
  .refine((v) => fits(v.product, v.type), { message: "shape_does_not_fit_type" });
