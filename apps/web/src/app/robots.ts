import type { MetadataRoute } from "next";

// Until the Demo release nothing is indexed. Tag pages (/TK-…) are never indexed (audit B12).
export default function robots(): MetadataRoute.Robots {
  if (process.env.TAGKIN_ALLOW_INDEXING === "true") {
    return {
      rules: [{ userAgent: "*", allow: "/", disallow: ["/TK-", "/r/", "/o/", "/my-tags"] }],
    };
  }
  return { rules: [{ userAgent: "*", disallow: "/" }] };
}
