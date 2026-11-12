import { Shell } from "@/components/Shell";
import { SignInForm } from "./SignInForm";

export default function SignIn() {
  return (
    <Shell>
      <h1>Sign in</h1>
      <p className="m">No password: we email you a 6-digit code.</p>
      <SignInForm />
    </Shell>
  );
}
