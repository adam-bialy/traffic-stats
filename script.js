// Collecting anonymous user data.
function sendInfoLocale(activity) {
  $.post("https://agstats.herokuapp.com/" + activity, {
    message: activity,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
  });
}

function sendInfoEmpty(activity) {
  $.post("https://agstats.herokuapp.com/" + activity, {
    message: activity,
    timezone: null
  });
}

const startTime = performance.now()
let isScrolled = false;
let isConsent = false;
let isRead = false;
let isViewed = false;

$(".consent-button").on("click", function() {
  if (this.name === "accept") {
    isConsent = true;
  }
  $(".consent").remove();
});

$(window).scroll(function() {

  if (!isViewed) {
    if (isConsent) {
      sendInfoLocale("view");
    } else {
      sendInfoEmpty("view");
    }
    isViewed = true;
  }

  function elementScrolled(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();
    var elemTop = $(elem).offset().top;
    return ((elemTop <= docViewBottom) && (elemTop >= docViewTop));
  }

  if (elementScrolled(".footer") & !isScrolled) {
    isScrolled = true
  }

  if (isScrolled & (performance.now() - startTime > 30000) & !isRead) {
    if (isConsent) {
      sendInfoLocale("read");
    } else {
      sendInfoEmpty("read");
    }
    isRead = true;
  }
});
