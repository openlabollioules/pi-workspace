# Pi Workspace Automation Platform

This repository is a shared workspace for designing, testing, and evolving business-process automations powered by agent harnesses such as Pi.

The goal is to build reusable automation assets around business domains while keeping the technical agent layer hidden from end users. Business users should ultimately interact with domain-specific applications, workflows, dashboards, and actions rather than with prompts, tools, models, or agent internals.

## Objectives

This repository is intended to support:

- business-process automation discovery and design;
- reusable agent skills and domain capabilities;
- local-first development of new automations;
- progressive promotion of reusable skills from local to domain to common scope;
- reproducible test workspaces and synthetic datasets;
- evaluation and benchmarking of generated automations;
- portability of skills across compatible agent harnesses when possible.

## Repository Structure

```text
pi-workspace/
├── AGENTS.md
├── README.md
│
├── .agents/
│   └── skills/                         # Common reusable skills
│
└── domains/
    ├── contract-management/
    │   ├── AGENTS.md                   # Shared Contract Management rules
    │   ├── .agents/
    │   │   └── skills/                 # Reusable Contract Management skills
    │   │
    │   ├── obligations/                # One automation workspace
    │   ├── changes/
    │   └── correspondence/
    │
    ├── quality/
    │   ├── AGENTS.md
    │   ├── .agents/
    │   │   └── skills/
    │   └── ...
    │
    └── ivvq/
        ├── AGENTS.md
        ├── .agents/
        │   └── skills/
        └── ...
```

## Skill Scope Model

Skills follow a three-level scope model.

### Common

Reusable across business domains:

```text
pi-workspace/.agents/skills/
```

Examples:

- process automation bootstrap;
- structured data handling;
- document ingestion;
- generic large-output handling.

### Domain

Reusable within one business domain:

```text
pi-workspace/domains/<domain>/.agents/skills/
```

Examples for Contract Management:

- contract obligation analysis;
- contract document traceability;
- change impact analysis;
- correspondence analysis.

### Local

Specific to one automation and created inside its workspace:

```text
pi-workspace/domains/<domain>/<automation>/.agents/skills/
```

New skills should normally start as local skills.

The preferred lifecycle is:

```text
LOCAL
  ↓
tested and reused
  ↓
DOMAIN
  ↓
validated across domains
  ↓
COMMON
```

Promotion is explicit. Shared skills should not be modified or moved automatically without review.

## Automation Workspace

A typical automation workspace may contain:

```text
<automation>/
├── PROCESS_AUTOMATION.md
├── BOOTSTRAP_TASK.md
├── AUTOMATION_SPEC.md
├── README.md
├── AGENTS.md
├── TASK.md
│
├── .agents/
│   └── skills/
│
├── agents/
│
├── workspace/
│   ├── input/
│   ├── data/
│   └── output/
│
├── test-data/
├── evaluator/
│
└── .bootstrap/
    ├── READINESS.md
    ├── DECISIONS.md
    ├── ASSUMPTIONS.md
    ├── OPEN_QUESTIONS.md
    └── PROMOTION_CANDIDATES.md
```

Not every automation needs every directory. The preferred architecture is the smallest one that satisfies the process.

## Process Automation Bootstrap

The common `process-automation-bootstrap` skill is used to turn a business-process description into a testable automation.

It can start from:

- a `PROCESS_AUTOMATION.md` file;
- existing process documentation;
- an interview with a business expert;
- a combination of all three.

The bootstrap evaluates a small readiness checklist before generating the automation.

Typical readiness dimensions include:

1. business objective;
2. trigger;
3. actors and responsibilities;
4. inputs;
5. nominal process;
6. decision rules and critical exceptions;
7. outputs;
8. human validation points and prohibited actions;
9. technical, data, and permission constraints;
10. acceptance criteria and test scenarios.

The bootstrap should ask only for information that is still missing or ambiguous.

Once the automation is ready, it generates the local automation structure and proposes which components could later be promoted to domain or common scope.

## Existing Test Data

Existing data always takes precedence over synthetic generation.

If a workspace already contains the required test inputs, the bootstrap must:

- reuse them as-is;
- avoid regenerating equivalent data;
- avoid overwriting or modifying source files;
- generate only missing inputs when explicitly allowed.

Source documents should normally be treated as read-only.

Derived data should be written to dedicated locations such as:

```text
workspace/data/
workspace/output/
```

## Evaluation and Ground Truth

Evaluation material must remain separate from the execution workspace.

Recommended structure:

```text
<automation>/
├── workspace/       # visible to the business agent
└── evaluator/       # reserved for benchmarking
```

Ground truth, scoring rubrics, and expected answers must not be used by the business agent during normal execution.

This separation makes it possible to measure:

- coverage;
- precision;
- false positives;
- traceability;
- exception handling;
- recovery after interruption;
- adherence to business rules.

## Local-First Development

When creating a new automation:

1. create new skills locally;
2. test the automation;
3. identify reusable components;
4. classify them as:
   - `LOCAL`
   - `DOMAIN_CANDIDATE`
   - `COMMON_CANDIDATE`
5. review promotion proposals;
6. promote only after explicit approval.

This prevents experimental automation logic from immediately becoming shared platform logic.

## Portability

Reusable skills should preferably follow the Agent Skills directory convention:

```text
.agents/skills/<skill-name>/SKILL.md
```

Supporting files may be placed alongside the skill:

```text
scripts/
references/
templates/
assets/
```

Business skills should remain harness-neutral whenever practical.

Harness-specific details such as:

- Pi extensions;
- Hermes configuration;
- runtime-specific tools;
- provider/model settings;

should be isolated from portable business instructions.

A portable `SKILL.md` does not automatically make all of its tools portable, so runtime dependencies should be documented explicitly.

## Pi Configuration

Pi's user-level configuration remains outside this repository in its normal configuration directory, typically:

```text
~/.pi/agent/
```

This repository is not a replacement for Pi's user configuration directory.

Pi can be configured to discover the common skills in this repository through its settings, while domain and local skills can be inherited from their project hierarchy.

Typical responsibilities are therefore separated as follows:

```text
~/.pi/agent/
    Pi user/runtime configuration

pi-workspace/
    shared automation assets, domains, skills, and automation workspaces
```

## AGENTS.md Inheritance

`AGENTS.md` files are used to provide layered instructions.

Typical hierarchy:

```text
pi-workspace/AGENTS.md
    ↓
domains/<domain>/AGENTS.md
    ↓
domains/<domain>/<automation>/AGENTS.md
```

This allows:

- platform-wide rules at the root;
- domain rules at the business-domain level;
- automation-specific rules inside each workspace.

## Recommended Workflow

### 1. Create or select a domain

Example:

```text
domains/contract-management/
```

### 2. Create an automation workspace

Example:

```text
domains/contract-management/obligations/
```

### 3. Add a process description

Create:

```text
PROCESS_AUTOMATION.md
```

Optionally add:

```text
BOOTSTRAP_TASK.md
```

to keep the bootstrap launch instructions versioned with the automation.

### 4. Run the bootstrap

Open the automation workspace in Pi and run the `process-automation-bootstrap` skill.

The bootstrap should:

- inspect existing process documentation;
- inspect existing test data;
- evaluate readiness;
- ask only blocking questions;
- generate the automation locally;
- create evaluation assets when needed;
- propose reusable components for promotion.

### 5. Review generated assets

Before running the business automation, review:

```text
AUTOMATION_SPEC.md
AGENTS.md
TASK.md
.agents/skills/
.bootstrap/PROMOTION_CANDIDATES.md
```

### 6. Run the business automation

For evaluation, open only the execution workspace when possible:

```text
<automation>/workspace/
```

This helps keep benchmark material isolated.

### 7. Evaluate and improve

Compare generated outputs against:

```text
<automation>/evaluator/
```

Use the results to improve the local automation before promoting reusable components.

## Design Principles

The platform follows a few core principles:

- business intent first;
- hidden technical complexity for end users;
- local-first development;
- reuse before creation;
- explicit promotion;
- source traceability;
- persistent and resumable work;
- minimal agent architecture;
- structured state for large or multi-step workflows;
- no unnecessary regeneration of existing data;
- separation between execution and evaluation;
- portability where practical.

## Current Focus

The first reference domain is Contract Management.

The initial proof of concept focuses on building a traceable contractual obligation register from a mixed corpus such as PDF contracts, annexes, CDRLs, responsibility matrices, and contractual schedules.

The same platform structure is intended to support additional domains and automations over time.

## Repository Status

This repository is currently an experimental automation platform and POC environment.

Interfaces, conventions, skill boundaries, and runtime adapters may evolve as more business processes are implemented and tested.


# Pi configuration

## Install Git Bash

A bash is used by Pi. Download and install Git Bash on windows.

## Extensions we've installed

With pi install :
- npm:@mammothb/pi-office
- npm:@nqbao/pi-alchemy
- npm:@bacnh85/pi-obsidian
- npm:pi-mcp-adapter
- npm:pi-subagents
- npm:@gotgenes/pi-permission-system
- npm:pi-file-permissions
- npm:@firstpick/pi-extension-grill-me
- npm:@siva-sub/pi-docparser

## settings.json

Under ~/.pi/agent

```
{
  "shellPath": "C:\\Program Files\\Git\\bin\\bash.exe",
  "defaultThinkingLevel": "medium",
  "alchemy": {
    "dbPath": "./data/contract.duckdb",
    "maxRows": 500
  },
  "packages": [
    "npm:@mammothb/pi-office",
    "npm:@nqbao/pi-alchemy",
    "npm:@bacnh85/pi-obsidian",
    "npm:pi-mcp-adapter",
    "npm:pi-subagents",
    "npm:@gotgenes/pi-permission-system",
    "npm:pi-file-permissions",
    "npm:@firstpick/pi-extension-grill-me",
    "npm:@siva-sub/pi-docparser"
  ],
"skills": [
    "G:\\pi-workspace\\.agents\\skills"
  ]
}
```

## Permissions

Content of our .pi\agent\extensions\pi-permission-system\config.json :

```
{
  "$schema": "https://raw.githubusercontent.com/gotgenes/pi-packages/main/packages/pi-permission-system/schemas/permissions.schema.json",

  "debugLog": true,
  "permissionReviewLog": true,
  "yoloMode": false,

  "toolInputPreviewMaxLength": 400,
  "toolTextSummaryMaxLength": 120,

  "piInfrastructureReadPaths": [
    "G:/pi-workspace",
    "C:/Users/xxx/AppData/Roaming/pi-desktop/tmp"
  ],

  "permission": {
    "*": "allow",

    "read": "allow",
    "write": "allow",
    "edit": "allow",
    "grep": "allow",
    "find": "allow",
    "ls": "allow",

    "path": {
      "*": "allow",
      "*.env": "deny",
      "*.env.*": "deny",
      "*.env.example": "allow"
    },

    "external_directory": {
      "*": "ask",

      "G:/pi-workspace": "allow",
      "G:/pi-workspace/*": "allow",
      "G:/pi-workspace/**": "allow",

      "C:/Users/xxx/AppData/Roaming/pi-desktop/tmp": "allow",
      "C:/Users/xxx/AppData/Roaming/pi-desktop/tmp/*": "allow",
      "C:/Users/xxx/AppData/Roaming/pi-desktop/tmp/**": "allow"
    },

    "bash": {
      "*": "allow",
      "rm -rf *": "deny",
      "sudo *": "ask"
    },

    "skill": {
      "*": "allow"
    }
  }
}
```