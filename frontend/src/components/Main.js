import { useContext } from "react";
import AuthContext from "../store/auth-context";
import Visits from "./Visits";
import LoginForm from "./LoginForm";
import classes from "./Main.module.css";

const Main = () => {
  const ctx = useContext(AuthContext);

  return (
    <main className={classes.main}>
      {ctx.isAuthenticated ? <Visits /> : <LoginForm />}
    </main>
  );
};

export default Main;
