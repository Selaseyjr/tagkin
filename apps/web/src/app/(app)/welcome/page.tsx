import Link from "next/link";
import { Icon } from "@/components/ui/Sprite";
import { Screen, Spacer } from "@/components/ui/Screen";

export default function Welcome() {
  return (
    <Screen header={false}>
      <Spacer />
      <div className="hero">
        <Icon name="mark" size={96} />
      </div>
      <h1 className="big center">Protect what you value.</h1>
      <p className="m center">
        Tag your bags, keys, gear and pets. If one ever goes missing, whoever finds it can scan the
        tag and alert you, privately and in many languages.
      </p>
      <Spacer />
      <div className="pager" aria-label="Page 1 of 2">
        <i className="on" />
        <i />
      </div>
      <Link className="btn pri" href="/welcome/private">
        Next
      </Link>
      <Link className="btn ghost" href="/sign-in">
        I have an account
      </Link>
    </Screen>
  );
}
