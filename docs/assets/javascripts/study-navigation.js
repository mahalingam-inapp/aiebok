(() => {
  const pathLinks = [...document.querySelectorAll(".study-path-course")];
  const position = document.querySelector(".study-position[data-course]");
  const start = document.querySelector(".study-start[data-course]");
  const activePath = "aiebok:study-path";

  function get(storage, key) {
    try {
      return window[storage].getItem(key);
    } catch {
      return null;
    }
  }

  function set(storage, key, value) {
    try {
      window[storage].setItem(key, value);
    } catch {
      // The static links still work when browser storage is unavailable.
    }
  }

  const resumeKey = (course) => `aiebok:last-lecture:${course}`;
  if (position) set("localStorage", resumeKey(position.dataset.course), position.dataset.lecture);

  if (pathLinks.length) {
    const courses = [...new Set(pathLinks.map((link) => link.pathname))];
    const title = document.querySelector("article h1")?.textContent.trim();
    const path = JSON.stringify({ url: location.pathname, courses, title });
    pathLinks.forEach((link) => link.addEventListener("click", () => set("sessionStorage", activePath, path)));
  }

  function addLink(container, url, label, className = "") {
    if (!container) return;
    const link = document.createElement("a");
    link.href = url;
    link.textContent = label;
    link.className = className;
    container.append(link);
  }

  if (start) {
    const last = get("localStorage", resumeKey(start.dataset.course));
    const lecture = [...document.querySelectorAll(".study-lecture")].find((link) => link.dataset.lecture === last);
    if (lecture && lecture.href !== start.href) {
      addLink(start.parentElement, lecture.href, "Resume last opened lecture", "md-button study-resume");
    }
  }

  const overview = document.querySelector(".study-overview");
  if (!start && !overview) return;

  let path;
  try {
    path = JSON.parse(get("sessionStorage", activePath));
  } catch {
    return;
  }
  const isLocalPath = (url) => typeof url === "string" && /^\/(?!\/)[A-Za-z0-9._/-]+$/.test(url);
  if (!path || typeof path.title !== "string" || !isLocalPath(path.url)
      || !path.url.includes("/getting-started/learning-paths/")
      || !Array.isArray(path.courses) || !path.courses.every(isLocalPath)) return;

  const course = overview ? overview.pathname : location.pathname;
  const positionInPath = path.courses.indexOf(course);
  if (positionInPath === -1) return;

  const links = document.createElement("p");
  links.className = "study-path-return";
  addLink(links, path.url, `← ${path.title}`);
  (position || start.parentElement).before(links);
  const next = path.courses[positionInPath + 1];
  const project = document.querySelector("#course-project");
  if (start && next && project) {
    const nextLink = document.createElement("p");
    nextLink.className = "study-path-return";
    addLink(nextLink, next, "Next course in this path →");
    document.querySelector("article").append(nextLink);
  }
})();
