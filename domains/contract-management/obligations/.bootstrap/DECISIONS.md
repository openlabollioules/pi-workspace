# Décisions du bootstrap

## D1 — Corpus existant, aucune génération de données
Le corpus synthétique complet (5 documents) est déjà présent dans `workspace/contract/`.
Décision : le traiter comme source en lecture seule, ne rien régénérer ni modifier.
(Conforme PROCESS_AUTOMATION §13 — le corpus y était annoncé comme à générer, mais il existe déjà : règle EXISTING DATA → REUSE.)

## D2 — Readiness complète sans interview
PROCESS_AUTOMATION.md + AGENTS.md plateforme/domaine couvrent R1–R10.
Aucune question bloquante n'a été posée.

## D3 — AUTOMATION_READY
Readiness R1–R10 CONFIRMED (voir READINESS.md). Génération du POC dans le workspace courant.

## D4 — Architecture minimale
Un seul agent principal (AGENTS.md + TASK.md au niveau du workspace).
Deux skills locaux :
- `contract-obligation-extraction` (méthodologie d'extraction et de qualification) ;
- `obligation-register-duckdb` (état persistant DuckDB + génération des livrables par fragments).
Réutilisation : skills communs `structured-data-duckdb` et `office` (pi-office) — aucun skill partagé modifié.

## D5 — État persistant
Base DuckDB dans `workspace/data/obligations.duckdb` (tables : documents, milestones, obligations, conflicts, ambiguities, progress).
Traitement par document, reprise possible depuis `progress`.

## D6 — Evaluator
Aucun evaluator existant dans le workspace. Création de `evaluator/ground-truth.md` + `evaluator/scoring-rubric.md`
à partir d'une lecture de référence du corpus. L'evaluator est isolé hors `workspace/` :
l'agent métier ne doit jamais y avoir accès pendant l'exécution.

## D7 — Livrables générés par fragments
Les 4 rapports markdown sont produits par fragments (`.parts/`) puis assemblés,
pour éviter les gros appels `write` monolithiques.
