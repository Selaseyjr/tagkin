import { Icon } from "@/components/ui/Sprite";
import { Screen, Spacer } from "@/components/ui/Screen";
import { SplashForward } from "./SplashForward";

/** App entry: the brand splash, then the first-launch screens. */
export default function Splash() {
  return (
    <Screen header={false}>
      <div className="splash">
        <Spacer />
        <Icon name="mark" size={120} />
        <b>tagkin</b>
        <Spacer />
      </div>
      <SplashForward to="/welcome" />
    </Screen>
  );
}
