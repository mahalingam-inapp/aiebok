(() => {
  const catalog = JSON.parse(document.querySelector("#curriculum-data").textContent);
  const form = document.querySelector("#request-form");
  const fields = form.elements;
  const cellHost = document.querySelector("#cells");
  const workOutput = new Map();
  const sections = new Map();

  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }

  const lessonCount = catalog.courses.reduce((sum, entry) => sum + entry.lessons.length, 0);
  const counts = document.querySelector("#coverage-counts");
  [cells.size + " runnable cells", lessonCount + " lectures mapped", catalog.knowledgeAreas.length + " knowledge areas"]
    .forEach((item) => counts.append(element("span", item)));

  const presets = {
    current: ["What is the fare refund deadline?", "public", "2026-11-21", false],
    historic: ["What is the fare refund deadline?", "public", "2026-03-01", false],
    lift: ["Where is the elevator?", "public", "2026-11-21", false],
    ledger: ["How do I submit a ledger reconciliation?", "public", "2026-11-21", false],
    missing: ["What is the weather forecast?", "public", "2026-11-21", false],
    audio: ["Where do I get lost property?", "public", "2026-11-21", false],
    incident: ["What is the fare refund deadline?", "public", "2026-11-21", true],
  };

  function request() {
    return {
      question: fields.question.value.trim(),
      role: fields.role.value,
      date: fields.date.value,
      ranking: fields.ranking.value,
      budget: fields.budget.valueAsNumber,
      approved: fields.approved.checked,
      outage: fields.outage.checked,
    };
  }

  function inspect(value) {
    return JSON.stringify(value, (key, item) => typeof item === "function" ? "[function " + (item.name || key) + "]" :
      typeof item === "number" && Number.isFinite(item) ? Number(item.toFixed(6)) : item, 2);
  }

  function detailsBlock(label) {
    const section = element("details");
    section.append(element("summary", label));
    return section;
  }

  function writeResponse(result, evaluated) {
    document.querySelector("#response-status").textContent = result.status === "answered" ? "Grounded answer" : "Staff handoff";
    document.querySelector("#response-text").textContent = result.text;
    const meta = document.querySelector("#response-facts");
    meta.replaceChildren();
    function row(label, value) { meta.append(element("dt", label), element("dd", value)); }
    row("Next step", result.next);
    if (result.review) row("Review state", result.review);
    result.citations.forEach((citation) => row("Evidence",
      citation.id + " · " + citation.source + " · " + citation.kind + " · effective " + citation.effective));
    if (evaluated) {
      const checks = currentChecks(evaluated);
      const hits = checks.results.filter(({ pass }) => pass).length;
      row(evaluated.hybrid ? "Fixed hybrid checks" : "Fixed topic lookup checks", hits + " / " + checks.results.length);
    }
  }

  function openModules() {
    return [...sections].filter(([, section]) => section.open).map(([id]) => id);
  }

  function showRun(scope, evaluateOpen = false) {
    const result = scope.run("serve");
    writeResponse(result, evaluateOpen ? scope.run("evaluate") : null);
    const meta = document.querySelector("#response-facts");
    meta.append(element("dt", "Retrieval in use"), element("dd", sections.get("retrieve").open ? fields.ranking.value : "Built-in topic lookup"));
  }

  function executeAll() {
    if (!form.reportValidity()) return;
    const active = openModules();
    const scope = createRun(request(), active);
    const status = document.querySelector("#run-status");
    let passed = 0;
    for (const id of active) {
      const output = workOutput.get(id);
      try {
        output.textContent = inspect(scope.run(id));
        passed += 1;
      } catch (error) {
        output.textContent = "Cell error: " + error.message;
      }
    }
    try {
      showRun(scope, active.includes("evaluate"));
    } catch (error) {
      status.textContent = error.message;
      return;
    }
    status.textContent = active.length ? passed + " / " + active.length + " open cells ran for the current request." : "The built-in service ran. All modules are closed.";
  }

  function executeSolution() {
    if (!form.reportValidity()) return;
    const status = document.querySelector("#run-status");
    try {
      showRun(createRun(request(), openModules()));
      status.textContent = "Solution ran for the current request.";
    } catch (error) {
      status.textContent = "Solution error: " + error.message;
    }
  }

  for (const [id, descriptor] of cells) {
    const section = detailsBlock(descriptor.title);
    section.id = "cell-" + id;
    const body = element("div", undefined, "cell-body");
    body.append(element("p", descriptor.description));
    if (descriptor.requires.length) {
      const line = element("p", "Module inputs when available · ", "dependencies");
      descriptor.requires.forEach((dependency, index) => {
        if (index > 0) line.append(", ");
        const anchor = element("a", cells.get(dependency).title.split(" · ")[1]);
        anchor.href = "#cell-" + dependency;
        line.append(anchor);
      });
      body.append(line);
    }
    const source = element("pre");
    source.append(element("code", descriptor.run.toString()));
    source.setAttribute("tabindex", "0");
    const runButton = element("button", "Run cell");
    runButton.type = "button";
    runButton.setAttribute("aria-label", "Run cell — " + descriptor.title);
    const output = element("pre", "Run this cell to see its output.", "output");
    output.setAttribute("tabindex", "0");
    output.setAttribute("aria-label", "Cell output");
    output.setAttribute("role", "status");
    runButton.addEventListener("click", () => {
      if (!form.reportValidity()) return;
      try {
        output.textContent = inspect(createRun(request(), openModules()).run(id));
      } catch (error) {
        output.textContent = "Cell error: " + error.message;
      }
    });
    workOutput.set(id, output);
    sections.set(id, section);
    body.append(source, runButton, output);
    section.append(body);
    cellHost.append(section);
  }

  let lastSelection;
  let updateQueued = false;
  function refreshModules() {
    const active = openModules();
    const selection = active.join(",");
    if (selection === lastSelection) return;
    lastSelection = selection;
    fields.ranking.disabled = !active.includes("retrieve");
    fields.approved.disabled = !active.includes("workflow");
    document.querySelector("#module-status").textContent = active.length + " of " + cells.size + " modules enabled.";
    for (const [id, output] of workOutput) {
      output.textContent = sections.get(id).open ? "Run this cell with the current modules." : "Module closed.";
    }
    executeSolution();
  }

  for (const section of sections.values()) section.addEventListener("toggle", () => {
    if (updateQueued) return;
    updateQueued = true;
    requestAnimationFrame(() => { updateQueued = false; refreshModules(); });
  });

  const catalogHost = document.querySelector("#catalog");
  const filterables = [];
  function appendGroup(title, entries) {
    const section = detailsBlock(title + " · " + entries.length);
    const list = element("ul", undefined, "catalog-list");
    const items = entries.map((entry) => {
      const item = element("li");
      if (entry.cell) {
        const anchor = element("a", entry.title);
        anchor.href = "#cell-" + entry.cell;
        item.append(anchor);
      } else {
        item.append(element("strong", entry.title));
      }
      if (entry.description) item.append(element("span", " — " + entry.description));
      if (entry.topics?.length) item.append(element("span", " (" + entry.topics.join(", ") + ")"));
      list.append(item);
      return item;
    });
    section.append(list);
    catalogHost.append(section);
    filterables.push({ section, items, title: title.toLowerCase() });
  }

  appendGroup("Knowledge areas", catalog.knowledgeAreas);
  for (const course of catalog.courses) appendGroup(course.title, course.lessons);
  for (const [title, entries] of Object.entries(catalog.references)) appendGroup(title, entries);
  document.querySelector("#find-topic").addEventListener("input", (event) => {
    const query = event.target.value.trim().toLowerCase();
    let matches = 0;
    for (const { section, items, title } of filterables) {
      let visible = false;
      for (const item of items) {
        item.hidden = Boolean(query && !title.includes(query) && !item.textContent.toLowerCase().includes(query));
        visible ||= !item.hidden;
        if (!item.hidden) matches += 1;
      }
      section.hidden = !visible;
      if (query && visible) section.open = true;
    }
    document.querySelector("#match-status").textContent = query ? matches + (matches === 1 ? " match" : " matches") : "";
  });

  function revealHash() {
    const target = /^#cell-[a-z]+$/.test(location.hash) && document.getElementById(location.hash.slice(1));
    if (target) target.open = true;
  }

  document.addEventListener("click", (event) => {
    const link = event.target.closest("a[href^='#cell-']");
    if (link) {
      const target = document.getElementById(link.hash.slice(1));
      if (target) target.open = true;
    }
  });
  window.addEventListener("hashchange", revealHash);
  revealHash();
  function setAll(open) {
    for (const section of sections.values()) section.open = open;
    refreshModules();
  }
  document.querySelector("#expand-cells").onclick = () => setAll(true);
  document.querySelector("#collapse-cells").onclick = () => setAll(false);
  document.querySelector("#run-all").onclick = executeAll;
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    executeSolution();
  });
  fields.scenario.addEventListener("change", () => {
    const [question, role, date, outage] = presets[fields.scenario.value];
    fields.question.value = question;
    fields.role.value = role;
    fields.date.value = date;
    fields.outage.checked = outage;
    fields.approved.checked = false;
    fields.ranking.value = "hybrid";
    fields.budget.value = "80";
    executeSolution();
  });
  refreshModules();
})();
