# Contract Management Domain Instructions

## Scope

These instructions apply to all automation workspaces under the Contract Management domain.

Automation-specific `AGENTS.md`, `TASK.md`, and skills may add more precise rules. More specific process rules should be followed when they do not conflict with explicit safety or source-preservation requirements.

---

## Contractual evidence first

Contract analysis must remain traceable to the contractual corpus.

For every material contractual finding, preserve enough information to identify its source, such as:

- document;
- clause, section, table, row, or other locator;
- relevant party;
- triggering event;
- applicable deadline or periodicity when present.

Do not present unsupported domain knowledge or customary practice as a contractual obligation.

---

## Distinguish fact from interpretation

Always distinguish:

- **contractual fact** — directly supported by a source;
- **interpretation** — a reasoned reading not stated verbatim;
- **ambiguity** — multiple reasonable readings remain possible;
- **conflict** — contractual sources contain incompatible requirements;
- **missing information** — the available corpus is insufficient.

Do not silently resolve ambiguity.

When an interpretation is required, preserve the supporting sources and state that it is an interpretation.

---

## Parties and responsibility

When extracting obligations or responsibilities, explicitly identify the responsible party whenever the source permits it.

Common categories include:

- Titulaire;
- Autorité Contractante;
- obligation conjointe;
- autre partie explicitly named in the contract.

Do not assume that an obligation belongs to the Titulaire merely because it appears in a contractor-facing document.

---

## Document precedence

When contractual documents conflict:

1. identify both sources;
2. identify any applicable order-of-precedence rule;
3. apply that rule when it clearly resolves the conflict;
4. preserve the existence of the conflict as a traceable issue;
5. require human review when precedence does not produce a defensible result.

Never hide a conflict simply because one source prevails.

---

## Dates and deadlines

Distinguish carefully between:

- fixed contractual dates;
- dates relative to contract effectiveness;
- dates relative to an event or milestone;
- calendar-day delays;
- business-day delays;
- recurring obligations;
- target/planned dates;
- actual/effective dates.

Do not replace an event-based contractual trigger with a planning target without clearly marking the distinction.

If a business-day calculation depends on a holiday calendar that is unavailable, preserve the contractual rule rather than inventing an exact date.

---

## Source immutability

Contractual source documents are authoritative inputs and should be treated as read-only.

Do not:

- rewrite contract clauses;
- silently correct apparent errors;
- normalize away conflicting wording;
- alter source spreadsheets to simplify analysis.

Derived data, indexes, normalized tables, and reports should be written separately.

---

## Human-in-the-loop

Unless an automation-specific rule explicitly grants more authority:

### May be automated
- document inventory;
- extraction;
- indexing;
- cross-document comparison;
- calculation based on explicit contractual rules;
- preparation of registers and draft reports;
- identification of potential conflicts and ambiguities.

### Require human validation
- unresolved contractual ambiguity;
- selection between competing interpretations when precedence is insufficient;
- conclusions that may materially affect an external contractual position;
- recommendations intended to become an official commitment.

### Not authorized by default
- final legal qualification;
- modification of authoritative contract sources;
- sending binding contractual communications;
- changing an approved contractual baseline.

---

## Traceability over fluency

Prefer a precise, sourced, possibly incomplete result over a polished but unsupported conclusion.

When information is missing, say what is missing and what consequence that has for the analysis.

Do not fabricate:

- clauses;
- dates;
- parties;
- approvals;
- acceptance events;
- deliverables;
- correspondence;
- contractual precedence.

---

## Structured contract data

For large registers, schedules, CDRLs, responsibility matrices, or other structured contractual data:

- prefer structured storage and queries over loading whole datasets into model context;
- use targeted projections, filters, counts, joins, and pagination;
- persist progress when processing can be interrupted;
- preserve links back to original contractual sources.

The business-facing report is a derived view; it should not be the sole source of truth for a large analysis.

---

## Evaluation separation

Ground truth, scoring rubrics, and benchmark answers must remain separate from business-agent execution.

A business agent must not use evaluator material to produce its answers.

Evaluation material may be accessed only when the user explicitly performs an evaluation or benchmark step.

---

## Reusable domain skills

Skills that encode broadly reusable Contract Management capabilities should eventually live in:

```text
domains/contract-management/.agents/skills/
```

Examples may include:

```text
contract-obligation-analysis
contract-document-traceability
contract-change-analysis
contract-correspondence-analysis
```

New capabilities should still be created and tested locally first, then proposed for promotion.

Do not promote project-specific rules, names, datasets, or program assumptions into a domain skill.
