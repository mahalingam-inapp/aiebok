const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const html = fs.readFileSync(path.join(__dirname, "../docs/assets/workbooks/harborlink.html"), "utf8");
const manifest = JSON.parse(html.match(/<script id="curriculum-data" type="application\/json">([^]*?)<\/script>/)[1]);
const runtime = html.match(/<script>([^]*?)<\/script>/)[1];
const ui = fs.readFileSync(path.join(__dirname, "interactive_workbook/ui.js"), "utf8");
assert.ok(runtime.endsWith(ui));
assert.doesNotMatch(html, /<(?:script|link)\b[^>]*(?:src|href)=/i);
new vm.Script(runtime);
const { cells, createRun, register } = vm.runInNewContext(
  runtime.slice(0, -ui.length) + "\n({ cells, createRun, register });"
);

const request = { question: "What is the fare refund deadline?", date: "2026-11-21",
  role: "public", ranking: "hybrid", budget: 80, approved: false, outage: false };
const solve = (changes = {}) => createRun({ ...request, ...changes }).run("serve");
const result = solve();
assert.equal(result.citations[0].id, "fare-v2");
assert.match(result.text, /14 days/);
assert.equal(solve({ date: "2026-03-01" }).citations[0].id, "fare-v1");
assert.equal(solve({ budget: 10 }).status, "handoff");
assert.equal(solve({ outage: true }).withFallback, true);

const restricted = { question: "ledger reconciliation" };
assert.equal(solve(restricted).status, "handoff");
assert.equal(solve({ ...restricted, role: "staff" }).citations[0].id, "staff-review");
const approved = { ...request, question: "weather forecast", role: "staff", approved: true };
const workflow = createRun(approved).run("workflow");
assert.equal(workflow.effects.length, 1);
assert.equal(workflow.replay, "replay ignored");
assert.equal(createRun({ ...approved, outage: true }).run("workflow").effects.length, 0);

const run = createRun(request);
for (const id of [...cells.keys()].reverse()) assert.notEqual(run.run(id), undefined, id);
assert.equal(run.run("serve").text, result.text);
const experts = run.run("experts");
assert.ok(Math.abs(experts.mixed - 3) < 1e-12);
assert.equal(experts.topOneBatch.overflow, 2);
assert.equal(run.run("budgets").budgets.cascade.spend, 12);
assert.equal(run.run("budgets").greedyCheck.committed.join(" "), "within 14 calendar");
assert.equal(run.run("decisions").preferred, "review");
assert.equal(run.run("decisions").optimalPlan.value, 12);
const evaluation = run.run("evaluate");
assert.equal(evaluation.hybrid.passRate, 1);
assert.equal(evaluation.hybrid.criticalPass, true);
assert.ok(evaluation.hybrid.passRate > evaluation.lexical.passRate);
const ids = [...cells.keys()];
const selections = [[], ids, ...ids.map((id) => [id]), ...ids.map((id) => ids.filter((other) => other !== id))];
for (const active of selections) {
  const modular = createRun(request, active);
  for (const id of active) assert.notEqual(modular.run(id), null, id);
  assert.equal(modular.run("serve").citations[0].id, "fare-v2");
  assert.ok([...modular.executed].every((id) => active.includes(id)), active.join(","));
  const runRequest = (changes) => createRun({ ...request, ...changes }, active).run("serve");
  assert.equal(runRequest({ ...restricted }).citations.length, 0);
  assert.equal(runRequest({ ...restricted, role: "staff" }).citations[0].id, "staff-review");
  assert.equal(runRequest({ date: "2026-03-01" }).citations[0].id, "fare-v1");
  assert.equal(runRequest({ budget: 10 }).status, "handoff");
  assert.equal(runRequest({ outage: true, approved: true, role: "staff" }).withFallback, true);
}
assert.equal(createRun(approved, []).run("serve").review, "manual review");
assert.equal(createRun(approved, ["workflow"]).run("serve").review, "local note recorded");
const lookupOnly = createRun(request, ["evaluate"]).run("evaluate");
assert.equal(lookupOnly.hybrid, undefined);
assert.equal(lookupOnly.topicLookup.passRate, 1);
assert.equal(createRun(request, ["delivery"]).run("delivery").releaseEvidenceReady, false);
const indexed = [...manifest.knowledgeAreas, ...manifest.courses.flatMap((course) => course.lessons),
  ...Object.values(manifest.references).flat().filter(({ cell }) => cell)];
for (const { cell, title } of indexed) assert.ok(cells.has(cell), title);
assert.ok(manifest.courses.every(({ lessons }) => lessons.length && lessons.every(({ description }) => description)));

assert.throws(() => run.run("missing"), /Unknown cell/);
register("cycle", "Cycle regression fixture", "", ["cycle"], () => {});
assert.throws(() => createRun(request).run("cycle"), /Circular dependency/);
cells.clear();
assert.equal(createRun(request).run("serve").citations[0].id, "fare-v2");
assert.equal(createRun({ ...request, ...restricted }).run("serve").citations.length, 0);
console.log(`Checked ${ids.length} cells, ${selections.length} module selections, ${indexed.length} curriculum mappings, and the service with the module registry empty.`);
