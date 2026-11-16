import Link from "next/link";
import { Icon } from "@/components/ui/Sprite";
import { Screen, Spacer } from "@/components/ui/Screen";

export default function PrivateByDefault() {
  return (
    <Screen header={false}>
      <Spacer />
      <div className="hero lockh">
        <Icon name="lock" size={64} />
      </div>
      <h1 className="big center">Private by default.</h1>
      <p className="m center">Finders message you through Tagkin. Nobody sees your number or email unless you choose to share it.</p>
      <Spacer />
      <div className="pager" aria-label="Page 2 of 2">
        <i />
        <i className="on" />
      </div>
      <Link className="btn pri" href="/start">Start exploring</Link>
    </Screen>
  );
}
