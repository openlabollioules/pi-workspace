# POC — Registre des obligations contractuelles (FNG-01 / FNG-02)

Automatisation agentique : extraction d'un registre consolidé des obligations
contractuelles à partir du corpus FNG-01, avec planification des échéances,
détection des conflits documentaires et gestion des ambiguïtés.

## Périmètre

- **Corpus** (lecture seule) : `workspace/contract/` — 5 documents
  (contrat principal, annexe A spécification technique, annexe B CDRL,
  annexe C responsabilités, annexe D planning).
- **Livrables agent** : `workspace/output/` (4 rapports Markdown) et
  `workspace/data/` (DuckDB `obligations.duckdb`).
- **Évaluation** : `evaluator/` — **interdit à l'agent** pendant l'exécution.

## Structure

```
obligations/
├── BOOTSTRAP_TASK.md          # Mission de génération de ce POC
├── PROCESS_AUTOMATION.md      # Description métier de référence
├── AUTOMATION_SPEC.md         # Spécification de l'automatisation
├── AGENTS.md                  # Rôle, scope et règles de l'agent
├── TASK.md                    # Mission d'exécution (5 étapes)
├── .bootstrap/                # Prêt-à-partir (R1-R10, décisions, hypothèses)
├── .agents/skills/
│   ├── contract-obligation-extraction/SKILL.md   # Méthode d'extraction
│   └── obligation-register-duckdb/SKILL.md       # Schéma DuckDB + rapports
├── workspace/
│   ├── contract/              # Corpus source (READ-ONLY)
│   ├── data/                  # obligations.duckdb (état persistant)
│   └── output/                # Rapports générés
└── evaluator/
    ├── ground-truth.md        # 135 obligations de référence + conflits/ambiguïtés
    ├── scoring-rubric.md      # Barème 100 pts, seuil de passage 80 %
    └── .parts/                # Fragments de rédaction (travail)
```

## Exécution

1. L'agent lit `TASK.md` et exécute les 5 étapes (reprise → ingestion →
   extraction → planification → conflits/rapports) en s'appuyant sur les deux
   skills locaux et les skills communs `office` et `structured-data-duckdb`.
2. L'état persiste dans `workspace/data/obligations.duckdb` (tables :
   documents, milestones, obligations, conflicts, ambiguities, progress) ;
   l'exécution est reprendre en cours et idempotente.
3. Les rapports sont générés par fragments puis assemblés (pas de write
   monolithique).

## Contraintes durables (rappel)

- Sources non modifiables ; aucune réécriture des clauses.
- Délais en JO : conserver la règle contractuelle, ne jamais produire de date
  exacte (pas de calendrier de jours fériés).
- A1/A2 = dates d'acceptation **cible** ; les obligations se déclenchent sur
  l'acceptation effective.
- Préséance : contrat > A > B > C > D ; tout conflit est consigné même tranché.
- L'agent n'accède jamais à `evaluator/`.

## Évaluation

Voir `evaluator/scoring-rubric.md` : 50 pts couverture (135 GT), 15 pts
traçabilité, 20 pts conflits/ambiguïtés, 10 pts qualité des données, 5 pts
livrables/robustesse. PASS ≥ 80 pts et couverture ≥ 80 %.
