import { useCallback, useContext, useEffect, useState } from "react";
import Menu from "./Menu";
import Table from "./Table";
import apiClient from "../utils/apiClient";
import classes from "./Visits.module.css";
import Button from "./UI/Button";
import AuthContext from "../store/auth-context";

const Visits = () => {
  const ctx = useContext(AuthContext);

  const logoutHandler = () => {
    ctx.onLogout();
  };

  const [group, setGroup] = useState("location");
  const [error, setError] = useState("");
  const [pageData, setPageData] = useState([]);

  const getData = useCallback(async (url) => {
    return await apiClient(url, "GET", null);
  }, []);

  useEffect(() => {
    const url = `visits_group/?group=${group}`;
    getData(url)
      .then((data) => {
        setPageData(data);
        setError("");
      })
      .catch((err) => {
        setError(err.message);
      });
  }, [group, getData]);

  const changeGroup = (newGroup) => {
    setGroup(newGroup);
  };

  return !error ? (
    <div className={classes.visits}>
      <Menu changeGroup={changeGroup} group={group} />
      <Table group={group} data={pageData} />
      {ctx.isAuthenticated && <Button text="Log out" onClick={logoutHandler} />}
    </div>
  ) : (
    <p>{error}</p>
  );
};

export default Visits;
