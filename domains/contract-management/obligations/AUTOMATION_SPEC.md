# AUTOMATION_SPEC — Registre des obligations contractuelles (POC)

## 1. Vue d'ensemble

Un agent principal lit le corpus contractuel de `workspace/contract/`, extrait les
obligations (Titulaire / AC / conjointes), les persiste dans DuckDB, croise les
échéances avec le planning contractuel, détecte conflits et ambiguïtés, puis génère
4 livrables markdown dans `workspace/output/`.

```
workspace/contract/ (LECTURE SEULE)          workspace/data/             workspace/output/
├── 01-contrat-principal.pdf       ──►      obligations.duckdb     ──►  data-ingestion-report.md
├── 02-annexe-a-specification-technique.pdf        (tables persistantes)      obligations-register.md
├── 03-annexe-b-livrables-cdrl.xlsx                (reprise possible)         ambiguities-and-conflicts.md
├── 04-annexe-c-responsabilites.xlsx                                   executive-summary.md
└── 05-planning-contractuel.xlsx
```

## 2. Composants

| Composant | Rôle | Emplacement |
|-----------|------|-------------|
| Agent principal | Exécute la mission de TASK.md | `AGENTS.md` + `TASK.md` |
| Skill extraction | Méthodologie d'extraction, qualification, conflits | `.agents/skills/contract-obligation-extraction/` |
| Skill registre DuckDB | Schéma, lots, reprise, fragments de rapports | `.agents/skills/obligation-register-duckdb/` |
| Skill commun (réutilisé) | Lecture PDF/XLSX | `office` (pi-office) |
| Skill commun (réutilisé) | Chargement XLSX → DuckDB, requêtes SQL | `structured-data-duckdb` |
| État persistant | Source de vérité des résultats | `workspace/data/obligations.duckdb` |
| Evaluator (hors exécution) | Ground truth + grille de scoring | `evaluator/` |

Un seul agent : aucune séparation de permissions, de contexte ou de parallélisation
n'est justifiée pour ce POC.

## 3. Modèle de données (DuckDB)

- `documents(doc_id, path, doc_type, contract_ref, version, status)`
- `milestones(id, name, date, kind, source_doc)` — kind : `CONTRACTUELLE` | `CIBLE` | `INDICATIF`
- `obligations(id, party, obligation, category, trigger, deadline, deliverable, source_doc, source_locator, confidence, status, notes)`
  - `party` : `TITULAIRE` | `AC` | `CONJOINTE`
  - `confidence` : `HAUTE` (texte explicite) | `MOYENNE` (déduit d'une référence croisée) | `BASSE` (interprétation)
  - `status` : `EXTRAITE` | `VALIDEE` | `EN_CONFLIT` | `AMBIGUE`
- `conflicts(id, description, source_a, source_b, precedence_applied, resolution, status)`
- `ambiguities(id, description, source_doc, readings, status)`
- `progress(doc_id, stage, status, updated_at)` — stage : `INGESTED` | `EXTRACTED` | `CROSSED` | `REPORTED`

## 4. Pipeline (repreneable)

1. **Inventaire** : lister `workspace/contract/`, remplir `documents`, vérifier formats.
2. **Référentiel** : lire définitions + ordre de préséance (contrat §1–2) ; charger les XLSX dans DuckDB (skill `structured-data-duckdb`).
3. **Extraction par document** (1 lot = 1 document ou 1 feuille) : insérer les obligations avec source précise ; marquer `progress`.
4. **Croisement planning** : charger les jalons ; rattacher les échéances relatives (JO avant/après jalon, Mx, jours calendaires) ; marquer `CIBLE`/`INDICATIF` le cas échéant.
5. **Conflits et ambiguïtés** : comparer les sources sur les mêmes objets ; appliquer la préséance §2.1 ; consigner le conflit même si tranché.
6. **Dédoublonnage + traçabilité** : une obligation = une ligne ; chaque ligne cite `source_doc` + `source_locator` ; aucune ligne sans source.
7. **Livrables** : générer les 4 rapports par fragments (`output/.parts/`) puis assembler.

## 5. Règles dures (rappel)

- Source contractuelle obligatoire par obligation ; sinon ne pas l'inclure.
- Interprétation ≠ fait : la mentionner dans `notes` avec `confidence` réduite.
- Conflit : appliquer la préséance ET le signaler dans `conflicts` + rapport dédié.
- JO sans calendrier fériés : conserver la règle, ne pas inventer de date exacte.
- Cible ≠ effective : conserver le déclencheur contractuel réel.
- Sources en lecture seule ; écriture uniquement `workspace/data/` et `workspace/output/`.
- Jamais d'accès à `evaluator/` pendant l'exécution.

## 6. Sorties

| Fichier | Contenu |
|---------|---------|
| `data-ingestion-report.md` | Inventaire des documents, format, volumes, données chargées, anomalies de lecture. |
| `obligations-register.md` | Registre complet (colonnes : ID, Partie responsable, Obligation, Catégorie, Déclencheur, Échéance/périodicité, Livrable/preuve, Source, Confiance). |
| `ambiguities-and-conflicts.md` | Conflits détectés, préséance appliquée, ambiguïtés, informations manquantes. |
| `executive-summary.md` | Synthèse chiffrée : total par partie, par catégorie, points de vigilance majeurs. |
