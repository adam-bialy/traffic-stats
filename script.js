// Collecting anonymous user data.
let isConsent = false;

function sendInfo(activity) {
  $.post("https://agstats.herokuapp.com/" + activity, {
    message: activity,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
  });
}

const startTime = performance.now()
let isScrolled = false;
let isRead = false;

$(".consent-button").on("click", function() {
  if (this.name === "accept") {
    isConsent = true;
    sendInfo("view")
  }
  $(".consent").remove();
});

$(window).scroll(function() {

  function elementScrolled(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();
    var elemTop = $(elem).offset().top;
    return ((elemTop <= docViewBottom) && (elemTop >= docViewTop));
  }

  if (elementScrolled(".footer") & !isScrolled) {
    isScrolled = true
  }

  if (isScrolled & (performance.now() - startTime > 30000) & !isRead & isConsent) {
    sendInfo("read")
    isRead = true;
  }
});