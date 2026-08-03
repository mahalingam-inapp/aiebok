/* Open repository and other off-site links in a new tab. */
document.addEventListener("DOMContentLoaded", function () {
  var selectors = [
    'a[href^="https://github.com/"]',
    'a[href^="http://github.com/"]',
  ];
  document.querySelectorAll(selectors.join(",")).forEach(function (anchor) {
    if (anchor.hostname === window.location.hostname) {
      return;
    }
    anchor.setAttribute("target", "_blank");
    anchor.setAttribute("rel", "noopener noreferrer");
    anchor.classList.add("external-link");
  });
});
