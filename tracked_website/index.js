// Script for collecting anonymous user data

// Define here API URL
const apiUrl = "http://localhost:8000/api/v1/visits/";

// Function for sending POST requests to the API
const sendToApi = (data) => {
  let headers = new Headers();
  headers.set("Content-Type", "application/json");
  fetch(apiUrl, {
    method: "POST",
    body: JSON.stringify(data),
    headers: headers,
  });
};

// Function for sending data with location data (timezone)
const sendInfoLocale = (activity) => {
  const dataToSend = {
    interaction_type: activity,
    location: Intl.DateTimeFormat().resolvedOptions().timeZone,
  };
  sendToApi(dataToSend);
};

// Function for sending date without location data
const sendInfoAnon = (activity) => {
  const dataToSend = {
    interaction_type: activity,
  };
  sendToApi(dataToSend);
};

// Initialize time counter and boolean variables
const startTime = performance.now();
let isConsent = false;
let isViewed = false;
let isRead = false;

// Use buttons in the consent modal to determine whether the user consented
const consentButtons = document.querySelectorAll(".consent-button");
consentButtons.forEach((button) =>
  button.addEventListener("click", (event) => {
    if (event.target.name === "accept") {
      isConsent = true;
    }
    document.querySelector(".consent").remove();
  }),
);

// Determine whether the user viewed and read the site
document.addEventListener("scroll", () => {
  function elementScrolled(elem) {
    const elementPosition = document
      .querySelector(elem)
      .getBoundingClientRect();
    return (
      elementPosition.top >= 0 &&
      elementPosition.left >= 0 &&
      elementPosition.bottom <=
        (window.innerHeight || document.documentElement.clientHeight) &&
      elementPosition.right <=
        (window.innerWidth || document.documentElement.clientWidth)
    );
  }

  // Check if user scrolled to element with class `.footer`. Can be changed for anything else.
  if (elementScrolled("footer") && !isViewed) {
    isViewed = true;
  }

  if (isViewed && performance.now() - startTime > 30000 && !isRead) {
    isRead = true;
  }
});

// Send requests when the user closes the website
addEventListener("beforeunload", () => {
  let sender;
  if (isConsent) {
    sender = sendInfoLocale;
  } else {
    sender = sendInfoAnon;
  }

  sender("open");

  if (isViewed) {
    sender("view");
  }

  if (isRead) {
    sender("read");
  }
});
