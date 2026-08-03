/**
 * AIEBOK reading progress — persisted locally in the browser (localStorage + cookies).
 * No server; safe for static GitHub Pages hosting.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "aiebok-progress-v1";
  var COOKIE_DONE = "aiebok_done";
  var COOKIE_LAST = "aiebok_last";
  var COOKIE_MAX_AGE = 60 * 60 * 24 * 365;
  var DWELL_MS = 6000;

  function manifestUrl() {
    var script = document.querySelector('script[src*="progress-tracker.js"]');
    if (script && script.src) {
      return script.src.replace(/javascripts\/progress-tracker\.js(\?.*)?$/, "progress-manifest.json");
    }
    return "/assets/progress-manifest.json";
  }

  function readCookie(name) {
    var match = document.cookie.match(new RegExp("(?:^|; )" + name + "=([^;]*)"));
    return match ? decodeURIComponent(match[1]) : "";
  }

  function writeCookie(name, value) {
    document.cookie =
      name +
      "=" +
      encodeURIComponent(value) +
      ";path=/;max-age=" +
      COOKIE_MAX_AGE +
      ";SameSite=Lax";
  }

  function defaultState() {
    return { version: 1, completed: [], lastPath: "", lastTitle: "", updatedAt: 0 };
  }

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        return JSON.parse(raw);
      }
    } catch (e) {
      /* ignore */
    }
    var done = readCookie(COOKIE_DONE);
    var last = readCookie(COOKIE_LAST);
    var fallback = defaultState();
    if (done) {
      fallback.completed = done.split(",").filter(Boolean);
    }
    if (last) {
      fallback.lastPath = last;
    }
    return fallback;
  }

  function saveState() {
    state.updatedAt = Date.now();
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {
      /* ignore quota errors */
    }
    writeCookie(COOKIE_DONE, state.completed.join(","));
    writeCookie(COOKIE_LAST, state.lastPath || "");
    renderBar();
  }

  function normalizeContentPath(path) {
    if (!path) {
      return "";
    }
    return path
      .replace(/^\//, "")
      .replace(/index\.html$/, "")
      .replace(/\.html$/, "")
      .replace(/\/$/, "")
      .replace(/\.md$/, "");
  }

  function pathFromLocation() {
    var path = window.location.pathname;
    var base = document.querySelector("base");
    if (base && base.getAttribute("href") && base.getAttribute("href") !== "/") {
      var basePath = base.getAttribute("href").replace(/^\//, "").replace(/\/$/, "");
      if (basePath && path.indexOf("/" + basePath + "/") === 0) {
        path = path.slice(basePath.length + 1);
      }
    }
    return normalizeContentPath(path);
  }

  function itemUrl(item) {
    if (!item.path) {
      return null;
    }
    return item.path.replace(/\.md$/, "/");
  }

  function findItemByPath(path) {
    if (!manifest || !path) {
      return null;
    }
    var norm = normalizeContentPath(path);
    for (var i = 0; i < manifest.items.length; i++) {
      var item = manifest.items[i];
      if (normalizeContentPath(item.path) === norm) {
        return item;
      }
    }
    return null;
  }

  function findItemById(id) {
    if (!manifest) {
      return null;
    }
    for (var i = 0; i < manifest.items.length; i++) {
      if (manifest.items[i].id === id) {
        return manifest.items[i];
      }
    }
    return null;
  }

  function isCompleted(id) {
    return state.completed.indexOf(id) !== -1;
  }

  function markComplete(id, title, path) {
    if (!id || isCompleted(id)) {
      return;
    }
    state.completed.push(id);
    if (path) {
      state.lastPath = path;
    }
    if (title) {
      state.lastTitle = title;
    }
    saveState();
  }

  function markIncomplete(id) {
    state.completed = state.completed.filter(function (x) {
      return x !== id;
    });
    saveState();
  }

  function activeItems() {
    if (!manifest) {
      return [];
    }
    return manifest.items;
  }

  function progressStats() {
    var items = activeItems();
    var total = items.length;
    var done = 0;
    items.forEach(function (item) {
      if (isCompleted(item.id)) {
        done += 1;
      }
    });
    var pct = total ? Math.round((done / total) * 100) : 0;
    return { done: done, total: total, pct: pct };
  }

  function nextItem() {
    var items = activeItems();
    for (var i = 0; i < items.length; i++) {
      if (!isCompleted(items[i].id)) {
        return items[i];
      }
    }
    return null;
  }

  function trackBreakdown() {
    var tracks = manifest ? manifest.tracks : {};
    var out = {};
    Object.keys(tracks).forEach(function (track) {
      out[track] = { done: 0, total: 0, label: tracks[track] };
    });
    activeItems().forEach(function (item) {
      if (!out[item.track]) {
        out[item.track] = { done: 0, total: 0, label: item.track };
      }
      out[item.track].total += 1;
      if (isCompleted(item.id)) {
        out[item.track].done += 1;
      }
    });
    return out;
  }

  function createBar() {
    if (document.getElementById("aiebok-progress")) {
      return;
    }
    var bar = document.createElement("div");
    bar.id = "aiebok-progress";
    bar.className = "aiebok-progress";
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", "Reading progress");
    bar.innerHTML =
      '<div class="aiebok-progress__inner">' +
      '<div class="aiebok-progress__track" aria-hidden="true"><div class="aiebok-progress__fill"></div></div>' +
      '<div class="aiebok-progress__row">' +
      '<span class="aiebok-progress__stat"></span>' +
      '<a class="aiebok-progress__continue" href="#"></a>' +
      '<button type="button" class="aiebok-progress__details-btn" aria-expanded="false" aria-controls="aiebok-progress-panel">Details</button>' +
      "</div>" +
      '<div id="aiebok-progress-panel" class="aiebok-progress__panel" hidden></div>' +
      "</div>";
    var header = document.querySelector(".md-header");
    if (header && header.parentNode) {
      header.parentNode.insertBefore(bar, header.nextSibling);
    } else {
      document.body.prepend(bar);
    }
    bar.querySelector(".aiebok-progress__details-btn").addEventListener("click", togglePanel);
    document.addEventListener("click", function (ev) {
      if (!bar.contains(ev.target)) {
        closePanel();
      }
    });
  }

  function renderBar() {
    var bar = document.getElementById("aiebok-progress");
    if (!bar || !manifest) {
      return;
    }
    var stats = progressStats();
    var fill = bar.querySelector(".aiebok-progress__fill");
    var stat = bar.querySelector(".aiebok-progress__stat");
    var cont = bar.querySelector(".aiebok-progress__continue");
    fill.style.width = stats.pct + "%";
    stat.textContent = stats.done + " / " + stats.total + " complete · " + stats.pct + "%";

    var next = nextItem();
    if (next && itemUrl(next)) {
      cont.href = itemUrl(next);
      cont.textContent = "Continue: " + next.title;
      cont.hidden = false;
    } else if (state.lastPath && itemUrl(findItemByPath(state.lastPath) || { path: state.lastPath })) {
      cont.href = itemUrl(findItemByPath(state.lastPath) || { path: state.lastPath });
      cont.textContent = "Resume: " + (state.lastTitle || "last page");
      cont.hidden = false;
    } else {
      cont.hidden = true;
    }

    renderPanel();
    renderPageActions();
  }

  function renderPanel() {
    var panel = document.getElementById("aiebok-progress-panel");
    if (!panel) {
      return;
    }
    var breakdown = trackBreakdown();
    var lines = ['<p class="aiebok-progress__hint">Saved in this browser only (localStorage + cookies). No account required.</p>'];
    Object.keys(breakdown).forEach(function (track) {
      var b = breakdown[track];
      var trackPct = b.total ? Math.round((b.done / b.total) * 100) : 0;
      lines.push(
        "<div class=\"aiebok-progress__trackline\"><strong>" +
          b.label +
          "</strong> — " +
          b.done +
          "/" +
          b.total +
          " (" +
          trackPct +
          "%)</div>"
      );
    });

    var current = findItemByPath(pathFromLocation());
    if (current) {
      var checked = isCompleted(current.id) ? " checked" : "";
      lines.push(
        '<label class="aiebok-progress__mark"><input type="checkbox" id="aiebok-mark-current"' +
          checked +
          "> Mark current page complete</label>"
      );
    }

    lines.push(
      '<button type="button" class="aiebok-progress__reset">Reset all progress</button>'
    );
    panel.innerHTML = lines.join("");

    var markCurrent = panel.querySelector("#aiebok-mark-current");
    if (markCurrent) {
      markCurrent.addEventListener("change", function (ev) {
        if (ev.target.checked) {
          markComplete(current.id, current.title, current.path);
        } else {
          markIncomplete(current.id);
        }
      });
    }

    var reset = panel.querySelector(".aiebok-progress__reset");
    if (reset) {
      reset.addEventListener("click", function () {
        if (window.confirm("Clear all reading progress on this device?")) {
          state = defaultState();
          saveState();
        }
      });
    }
  }

  function togglePanel() {
    var panel = document.getElementById("aiebok-progress-panel");
    var btn = document.querySelector(".aiebok-progress__details-btn");
    if (!panel || !btn) {
      return;
    }
    var open = panel.hasAttribute("hidden");
    if (open) {
      panel.removeAttribute("hidden");
      btn.setAttribute("aria-expanded", "true");
    } else {
      panel.setAttribute("hidden", "");
      btn.setAttribute("aria-expanded", "false");
    }
  }

  function closePanel() {
    var panel = document.getElementById("aiebok-progress-panel");
    var btn = document.querySelector(".aiebok-progress__details-btn");
    if (panel && btn) {
      panel.setAttribute("hidden", "");
      btn.setAttribute("aria-expanded", "false");
    }
  }

  function renderPageActions() {
    var article = document.querySelector(".md-content__inner");
    if (!article) {
      return;
    }
    var current = findItemByPath(pathFromLocation());
    var existing = document.getElementById("aiebok-page-actions");
    if (!current) {
      if (existing) {
        existing.remove();
      }
      return;
    }
    if (!existing) {
      existing = document.createElement("div");
      existing.id = "aiebok-page-actions";
      existing.className = "aiebok-page-actions";
      article.appendChild(existing);
    }
    var done = isCompleted(current.id);
    existing.innerHTML =
      '<button type="button" class="md-button md-button--primary aiebok-complete-btn">' +
      (done ? "Completed ✓" : "Mark chapter complete") +
      "</button>" +
      (done ? ' <button type="button" class="md-button aiebok-uncomplete-btn">Mark incomplete</button>' : "");
    var completeBtn = existing.querySelector(".aiebok-complete-btn");
    completeBtn.addEventListener("click", function () {
      markComplete(current.id, current.title, current.path);
    });
    var uncompleteBtn = existing.querySelector(".aiebok-uncomplete-btn");
    if (uncompleteBtn) {
      uncompleteBtn.addEventListener("click", function () {
        markIncomplete(current.id);
      });
    }
  }

  function scheduleAutoComplete(item) {
    if (!item || isCompleted(item.id)) {
      return;
    }
    clearTimeout(dwellTimer);
    dwellTimer = setTimeout(function () {
      if (document.visibilityState === "visible") {
        markComplete(item.id, item.title, item.path);
      }
    }, DWELL_MS);
  }

  function onPageReady() {
    var path = pathFromLocation();
    var item = findItemByPath(path);
    if (item) {
      state.lastPath = item.path;
      state.lastTitle = item.title;
      saveState();
      scheduleAutoComplete(item);
    }
    renderBar();
  }

  function fetchManifest() {
    return fetch(manifestUrl())
      .then(function (res) {
        if (!res.ok) {
          throw new Error("manifest load failed");
        }
        return res.json();
      })
      .then(function (data) {
        manifest = data;
        state = loadState();
        createBar();
        onPageReady();
      })
      .catch(function () {
        /* tracker optional — fail silently */
      });
  }

  document.addEventListener("DOMContentLoaded", fetchManifest);

  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") {
      clearTimeout(dwellTimer);
    }
  });

  /* MkDocs Material instant navigation */
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(function () {
      if (manifest) {
        clearTimeout(dwellTimer);
        onPageReady();
      }
    });
  } else {
    var _push = history.pushState;
    history.pushState = function () {
      _push.apply(this, arguments);
      setTimeout(function () {
        if (manifest) {
          clearTimeout(dwellTimer);
          onPageReady();
        }
      }, 0);
    };
    window.addEventListener("popstate", function () {
      if (manifest) {
        clearTimeout(dwellTimer);
        onPageReady();
      }
    });
  }
})();
