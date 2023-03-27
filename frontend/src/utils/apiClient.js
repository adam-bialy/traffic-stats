const apiUrl = `${process.env.REACT_APP_API_ROOT}/api/v1/`;

const apiClient = async (url, method = "GET", payload = {}) => {
  let headers = new Headers();
  const token = localStorage.getItem("apitoken");
  headers.append("Authorization", `Token ${token}`);
  const response = await fetch(`${apiUrl}${url}`, {
    method: method,
    body: payload,
    headers: headers,
  });
  if (response.ok) {
    return await response.json();
  } else if (response.status === 401) {
    throw new Error(
      "Wrong authentication credentials. Please log out and try logging in again.",
    );
  } else {
    throw new Error("An error occurred. Please try again later.");
  }
};

export default apiClient;
