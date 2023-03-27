import { useContext, useState } from "react";
import AuthContext from "../store/auth-context";
import classes from "./LoginForm.module.css";
import Button from "./UI/Button";

const LoginForm = () => {
  const ctx = useContext(AuthContext);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    ctx.onLogin(email, password);
    setEmail("");
    setPassword("");
  };

  return (
    <div className={classes.loginForm}>
      <h3>Please enter username and password to access</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={email}
          onChange={handleEmailChange}
          placeholder="username"
        />
        <input
          type="password"
          value={password}
          onChange={handlePasswordChange}
          placeholder="password"
        />
        <Button text="Log in" />
      </form>
      {ctx.loginError && <p>{ctx.loginError}</p>}
    </div>
  );
};

export default LoginForm;
