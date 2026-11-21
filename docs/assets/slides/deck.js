(() => {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const controls = document.querySelector(".deck-controls");
  const previous = document.querySelector("#previous");
  const next = document.querySelector("#next");
  const count = document.querySelector("#slide-count");
  const progress = document.querySelector("#slide-progress");
  const index = document.querySelector(".slide-index");
  const indexLinks = [...index.querySelectorAll("a")];
  const announcement = document.querySelector("#announcement");
  const fullscreen = document.querySelector("#fullscreen");
  let current = 0;

  function show(index, { updateUrl = true, focus = false } = {}) {
    current = Math.max(0, Math.min(index, slides.length - 1));
    slides.forEach((slide, i) => { slide.hidden = i !== current; });

    const slide = slides[current];
    const heading = slide.querySelector("h1, h2");
    const position = `${current + 1} / ${slides.length}`;
    count.textContent = position;
    progress.value = current + 1;
    indexLinks.forEach((link, i) => {
      if (i === current) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
    announcement.textContent = `Slide ${current + 1} of ${slides.length}. ${heading.textContent}`;
    previous.setAttribute("aria-disabled", String(current === 0));
    next.setAttribute("aria-disabled", String(current === slides.length - 1));

    if (updateUrl) history.replaceState(null, "", `#${slide.id}`);
    if (focus) heading.focus({ preventScroll: true });
    window.scrollTo(0, 0);
  }

  function readHash() {
    const index = slides.findIndex((slide) => location.hash === `#${slide.id}`);
    return index < 0 ? 0 : index;
  }

  previous.addEventListener("click", () => {
    if (current > 0) show(current - 1);
  });
  next.addEventListener("click", () => {
    if (current < slides.length - 1) show(current + 1);
  });
  indexLinks.forEach((link, number) => link.addEventListener("click", (event) => {
    event.preventDefault();
    index.open = false;
    show(number, { focus: true });
  }));
  window.addEventListener("hashchange", () => show(readHash(), { updateUrl: false, focus: true }));
  document.addEventListener("keydown", (event) => {
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey
        || event.target.closest?.("input, textarea, select, [contenteditable], summary")) return;
    const targets = {
      ArrowLeft: current - 1,
      ArrowRight: current + 1,
      PageUp: current - 1,
      PageDown: current + 1,
      Home: 0,
      End: slides.length - 1,
    };
    if (!Object.hasOwn(targets, event.key)) return;
    event.preventDefault();
    show(targets[event.key], { focus: true });
  });

  if (document.fullscreenEnabled) {
    fullscreen.hidden = false;
    fullscreen.addEventListener("click", async () => {
      try {
        if (document.fullscreenElement) await document.exitFullscreen();
        else await document.documentElement.requestFullscreen();
      } catch {
        fullscreen.hidden = true;
      }
    });
    document.addEventListener("fullscreenchange", () => {
      fullscreen.setAttribute("aria-pressed", String(Boolean(document.fullscreenElement)));
    });
  }

  controls.hidden = false;
  document.body.classList.add("deck-ready");
  show(readHash(), { updateUrl: false });
})();
