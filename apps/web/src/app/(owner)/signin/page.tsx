import { AppScreen } from "@/components/app/AppScreen";
import { SignInForm } from "./SignInForm";

export default function SignIn() {
  return (
    <AppScreen back={{ href: "/" }}>
      <SignInForm />
    </AppScreen>
  );
}
