const cells = new Map();

function register(id, title, description, requires, run) {
  if (cells.has(id)) throw new Error("Duplicate workbook cell: " + id);
  cells.set(id, { id, title, description, requires, run });
}

function createRun(input, activeIds = cells.keys()) {
  const snapshot = Object.freeze({ ...input });
  const active = new Set(activeIds);
  const completed = new Map();
  const visiting = new Set();
  const executed = new Set();
  const substituted = new Set();

  function run(id) {
    if (completed.has(id)) return completed.get(id);
    if (!cells.has(id) && !baseline.has(id)) throw new Error("Unknown cell: " + id);
    const enabled = active.has(id) && cells.has(id);
    const cell = enabled ? cells.get(id) : baseline.get(id);
    if (!cell) return null;
    if (visiting.has(id)) throw new Error("Circular dependency at " + id);
    visiting.add(id);
    try {
      const dependencies = Object.fromEntries(cell.requires.map((key) => [key, run(key)]));
      const result = cell.run({
        input: snapshot,
        dependencies,
        evaluate: (event, target) => createRun(event, active).run(target),
        isActive: (key) => active.has(key) && cells.has(key),
      });
      (enabled ? executed : substituted).add(id);
      completed.set(id, result);
      return result;
    } finally {
      visiting.delete(id);
    }
  }
  return { run, executed, substituted };
}
