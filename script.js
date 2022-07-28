function sendInfo(activity) {
  $.post("http://127.0.0.1:5000/" + activity, {
    message: activity,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
  });
}

const startTime = performance.now()
let isScrolled = false;
let isRead = false;

sendInfo("view")

$(window).scroll(function() {

  function elementScrolled(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();
    var elemTop = $(elem).offset().top;
    return ((elemTop <= docViewBottom) && (elemTop >= docViewTop));
  }

  if (elementScrolled('.last-papaj') & !isScrolled) {
    isScrolled = true
  }

  if (isScrolled & (performance.now() - startTime > 30000) & !isRead) {
    sendInfo("read")
    isRead = true;
  }
});
