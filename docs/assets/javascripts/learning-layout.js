(() => {
  const catalog = document.querySelector("[data-catalog]");
  if (catalog) {
    const filters = catalog.querySelector(".learning-filters");
    const input = filters.querySelector("input");
    const buttons = [...filters.querySelectorAll("[data-category]")];
    const cards = [...catalog.querySelectorAll("[data-card]")];
    const status = catalog.querySelector("[role=status]");
    let category = "";
    function filterCards() {
      const words = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
      let count = 0;
      for (const card of cards) {
        const text = card.dataset.search.toLocaleLowerCase();
        card.hidden = Boolean(category && card.dataset.card !== category) || !words.every((word) => text.includes(word));
        if (!card.hidden) count += 1;
      }
      const noun = catalog.dataset.noun;
      status.textContent = count ? count + " " + noun + (count === 1 ? "" : "s") : "No matches. Try another search or category.";
    }
    filters.hidden = false;
    input.addEventListener("input", filterCards);
    for (const button of buttons) {
      button.addEventListener("click", () => {
        category = button.dataset.category;
        for (const choice of buttons) choice.setAttribute("aria-pressed", String(choice === button));
        filterCards();
      });
    }
  }

  const outline = document.querySelector("[data-course-progress]");
  if (!outline) return;
  const key = (lecture) => "aiebok:completed:" + lecture;
  const progress = outline.querySelector("progress");
  const label = outline.querySelector("[data-progress-label]");
  const links = [...outline.querySelectorAll("[data-lecture]")];
  const button = document.querySelector("[data-complete]");
  const completed = new Set();
  try {
    for (const link of links) {
      const lecture = link.dataset.lecture;
      if (localStorage.getItem(key(lecture)) === "true") completed.add(lecture);
    }
  } catch {
    // Completion is available for this page when browser storage is blocked.
  }

  function renderProgress() {
    let count = 0;
    for (const link of links) {
      const done = completed.has(link.dataset.lecture);
      link.classList.toggle("is-complete", done);
      if (done) {
        count += 1;
        link.setAttribute("aria-label", link.children[1].textContent + ", completed");
      } else {
        link.removeAttribute("aria-label");
      }
    }
    progress.value = count;
    label.textContent = count + " of " + outline.dataset.total + " lectures complete";
    if (button) {
      const done = completed.has(button.dataset.complete);
      button.textContent = done ? "Mark lecture incomplete" : "Mark lecture complete";
    }
  }

  outline.querySelector(".learning-progress").hidden = false;
  renderProgress();
  if (button) {
    button.parentElement.hidden = false;
    button.addEventListener("click", () => {
      const id = button.dataset.complete;
      if (completed.has(id)) completed.delete(id);
      else completed.add(id);
      try {
        if (completed.has(id)) localStorage.setItem(key(id), "true");
        else localStorage.removeItem(key(id));
      } catch {
        // Keep the current page state usable.
      }
      renderProgress();
    });
  }
})();
