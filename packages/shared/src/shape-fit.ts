/** Shape fit (BUSINESS-RULES 3c). Every screen and the database read this table. */

export const PRODUCTS = ["sticker", "keychain", "pet_tag", "luggage_label", "lock_screen"] as const;
export type Product = (typeof PRODUCTS)[number];

export const TAG_TYPES = ["item", "travel", "pet"] as const;
export type TagType = (typeof TAG_TYPES)[number];

/** Printed products; the lock-screen tag is digital (BUSINESS-RULES 3b). */
export const PRINTED_PRODUCTS = PRODUCTS.filter((p) => p !== "lock_screen") as Exclude<
  Product,
  "lock_screen"
>[];

export const SHAPE_FIT: Readonly<Record<Product, readonly TagType[]>> = {
  sticker: ["item", "travel"],
  keychain: ["item"],
  luggage_label: ["travel"],
  pet_tag: ["pet"],
  lock_screen: ["item"], // the phone only
};

export function fits(product: Product, type: TagType): boolean {
  return SHAPE_FIT[product].includes(type);
}

/** Types offered after choosing a shape. One type → the type step is skipped. */
export function typesFor(product: Product): readonly TagType[] {
  return SHAPE_FIT[product];
}

/** Printed shapes offered on Customise for a type. One shape → no shape choice. */
export function shapesFor(type: TagType): Product[] {
  return PRINTED_PRODUCTS.filter((p) => fits(p, type));
}

/** Blank tags and gifts: printed products only. */
export function canBeBlank(product: Product): boolean {
  return product !== "lock_screen";
}
export const canBeGifted = canBeBlank;
