import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  cacheComponents: true,
  partialPrefetching: true,
  // Workspace packages ship TypeScript source; Next compiles them.
  transpilePackages: ["@tagkin/shared", "@tagkin/tokens", "@tagkin/i18n"],
};

export default nextConfig;
