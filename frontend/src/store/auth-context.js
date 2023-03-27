import React, { useEffect, useState } from "react";

const AuthContext = React.createContext({
  isAuthenticated: false,
  loginError: "",
  onLogout: () => {},
  onLogin: () => {},
});

export const AuthContextProvider = (props) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [loginError, setLoginError] = useState("");

  useEffect(() => {
    const storedLoginInfo = localStorage.getItem("apitoken");
    if (storedLoginInfo) {
      setIsLoggedIn(true);
    }
  }, []);

  const logoutHandler = () => {
    localStorage.removeItem("apitoken");
    setIsLoggedIn(false);
  };

  const loginHandler = async (username, password) => {
    const headers = new Headers({ "Content-Type": "application/json" });
    const body = { username: username, password: password };
    try {
      const response = await fetch("http://localhost:8000/api_token/", {
        method: "POST",
        body: JSON.stringify(body),
        headers: headers,
      });
      const data = await response.json();
      if (response.ok) {
        localStorage.setItem("apitoken", data.token);
        setIsLoggedIn(true);
        setLoginError("");
      } else {
        setLoginError("Login failed - wrong credentials provided.");
      }
    } catch (err) {
      setLoginError("An error occured.");
    }
  };

  return (
    <AuthContext.Provider
      value={{
        isAuthenticated: isLoggedIn,
        loginError: loginError,
        onLogout: logoutHandler,
        onLogin: loginHandler,
      }}
    >
      {" "}
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
