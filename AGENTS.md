# Automation Platform Instructions

## Scope

These instructions apply to every automation workspace located under this platform.

The platform uses a three-level capability model:

1. **COMMON** — reusable across domains:
   `.agents/skills/`
2. **DOMAIN** — reusable inside one business domain:
   `domains/<domain>/.agents/skills/`
3. **LOCAL** — specific to one automation:
   `<automation>/.agents/skills/`

Use inherited capabilities before creating new ones.

---

## Local-first development

When designing or generating a new automation:

- create new skills and agent specifications locally first;
- test them in the current automation workspace;
- do not modify, move, replace, or overwrite a shared DOMAIN or COMMON component unless explicitly requested;
- after testing, a local component may be proposed for promotion to DOMAIN or COMMON;
- promotion must remain explicit and reviewable.

Never create a shared component merely because it appears reusable before it has been tested locally.

---

## Skill portability

Reusable skills should use the standard structure:

```text
.agents/skills/<skill-name>/
└── SKILL.md
```

A skill may also contain:

```text
scripts/
references/
templates/
assets/
```

For reusable skills:

- prefer harness-neutral business language;
- avoid hard-coding Pi-specific tool names when the requirement can be expressed as a generic capability;
- isolate Pi-, Hermes-, or runtime-specific adapters from portable business instructions;
- avoid absolute paths tied to one workstation;
- document runtime/tool dependencies when portability is incomplete.

---

## Reuse before creation

Before creating a new skill:

1. inspect skills already available locally;
2. inspect inherited DOMAIN skills;
3. inspect inherited COMMON skills;
4. reuse an existing capability when it sufficiently covers the need;
5. create a new local skill only when the capability is genuinely missing or an existing shared skill must not yet be changed.

Do not create near-duplicate skills under different names.

---

## Shared component safety

Shared assets are considered controlled platform assets.

While working inside an automation workspace:

- treat parent-level `.agents/skills/` as read-only unless the user explicitly requests a shared change;
- do not silently update a DOMAIN or COMMON skill;
- do not keep two divergent copies of the same promoted skill;
- record proposed promotions or shared changes before applying them.

---

## Pi runtime configuration boundary

Do not inspect, search, read, modify, or enumerate the Pi user configuration directory:

`~/.pi/agent/`
or
`Users/xxx/.pi/`

unless the user explicitly requests a Pi administration or debugging task.

All reusable platform skills required by automation workspaces must be discovered from:

- `pi-workspace/.agents/skills/`
- the current domain `.agents/skills/`
- the current workspace `.agents/skills/`

Do not search `~/.pi` to discover skills, bootstrap files, agents, prompts, or automation resources.

Assume already-loaded Pi extensions and globally configured runtime resources are available through Pi without inspecting their installation directories.

---

## Workspace boundaries

Operate primarily inside the current automation workspace.

Do not inspect sibling automation workspaces unless required by the current task.

Directories containing benchmark references or ground truth are not execution inputs.

If an automation contains:

```text
workspace/
evaluator/
```

then:

- `workspace/` is the execution area for the business agent;
- `evaluator/` is reserved for evaluation and must not be used as a source by the business agent unless the user explicitly starts an evaluation task.

---

## Existing data first

Before generating sample, synthetic, or replacement data:

1. inspect the inputs already present;
2. reuse existing suitable data;
3. preserve existing source files;
4. generate only missing data when generation is permitted.

Never overwrite an existing test corpus merely to simplify generation.

---

## Source preservation

Input/source material should be treated as read-only unless the task explicitly requires modification.

Prefer writing derived state and outputs into dedicated locations such as:

```text
workspace/data/
workspace/output/
```

Do not modify source documents merely to make them easier for an agent to process.

---

## Persistent and resumable work

For long-running, multi-step, or data-heavy automations:

- persist meaningful progress;
- use structured storage when appropriate;
- design work so it can resume after interruption;
- avoid regenerating already validated work;
- use stable identifiers for persistent records.

DuckDB is a preferred local option when relational queries, structured state, or resumability are useful, but automation-specific requirements take precedence.

---

## Large outputs

Avoid very large monolithic `write` or `edit` operations.

For large outputs:

- persist structured information first where appropriate;
- generate in bounded batches;
- use fragments such as `output/.parts/`;
- validate fragments;
- assemble them deterministically;
- do not retry the same oversized write unchanged after failure.

---

## Human authority

Agents may automate analysis and preparation, but business authority remains defined by the automation's own rules.

Never infer permission to:

- make an externally binding decision;
- alter authoritative source data;
- bypass an approval gate;
- disclose restricted information.

If the automation defines a human validation point, preserve it.

---

## Simplicity

Prefer the smallest architecture that can satisfy the process.

Use:

```text
one primary agent
+ reusable skills
+ tools
+ persistent state when needed
```

unless multiple agents provide a clear benefit such as isolation, permissions, context separation, or useful parallelism.

Do not add agents, skills, databases, or infrastructure solely for architectural sophistication.


## Temporary files

Do not use `/tmp`, `%TEMP%`, or other system-wide temporary directories for agent-created intermediate files.

Use only:

`workspace/.tmp/`

for temporary extraction, conversion, unpacking, and intermediate processing.

Create subdirectories under `workspace/.tmp/` as needed and clean them up when safe.