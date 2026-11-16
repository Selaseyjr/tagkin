import "@/styles/proto.css";
import "@/styles/app.css";
import { Sprite } from "@/components/ui/Sprite";

export default function AppLayout({ children }: LayoutProps<"/">) {
  return (
    <>
      <Sprite />
      {children}
    </>
  );
}
