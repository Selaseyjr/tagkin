import { Suspense } from "react";
import { AppScreen } from "@/components/app/AppScreen";
import { hasOpenReturn } from "@/lib/owner";

async function Orders() {
  const unread = await hasOpenReturn();
  return (
    <AppScreen tab="orders" unread={unread}>
      <h1>Orders</h1>
      <div className="empty">
        <span className="bell">📦</span>
        <p className="m">
          No orders yet. Printed tags you order appear here, from payment to delivery.
        </p>
      </div>
    </AppScreen>
  );
}

export default function Page() {
  return (
    <Suspense fallback={<div className="app" />}>
      <Orders />
    </Suspense>
  );
}
