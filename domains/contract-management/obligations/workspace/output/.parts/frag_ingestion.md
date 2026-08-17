# Rapport d'ingestion des données

Corpus : programme FNG-01 (fictif) — 5 documents contractuels, `workspace/contract/`.

| Document | Type | Référence contractuelle | Version |
|---|---|---|---|
| `01-contrat-principal` (workspace/contract/01-contrat-principal.pdf) | PDF | ACN-FNG-2026-001 | 1.0 |
| `02-annexe-a-specification-technique` (workspace/contract/02-annexe-a-specification-technique.pdf) | PDF | ACN-FNG-2026-001-A | 1.0 |
| `03-annexe-b-livrables-cdrl` (workspace/contract/03-annexe-b-livrables-cdrl.xlsx) | XLSX | ACN-FNG-2026-001-B | 1.0 |
| `04-annexe-c-responsabilites` (workspace/contract/04-annexe-c-responsabilites.xlsx) | XLSX | ACN-FNG-2026-001-C | 1.0 |
| `05-planning-contractuel` (workspace/contract/05-planning-contractuel.xlsx) | XLSX | ACN-FNG-2026-001-D | 1.0 |

## Méthode d'ingestion

- PDF : extraction texte intégrale, lecture complète (9 + 6 pages).
- XLSX : structure inspectée, 12 tables chargées dans DuckDB (`workspace/data/obligations.duckdb`) puis requêtes ciblées (toutes < 30 lignes).
- Tables chargées : cdrl (30), submission_rules (3), gfe_gfi (9), titulaire_gfe (4), joint_reviews (6), review_minutes (1), site_access (2), test_data (2), milestones_x (19), training (6), gfe_gfi_derived (9), assumptions (3).
- Dates de l'Annexe D : nombres sériels Excel convertis en dates calendaires ; dates dérivées GFE/GFI marquées INDICATIF.

## Vérifications de cohérence à l'ingestion

- Dates dérivées GFE/GFI (Annexe D) cohérentes avec les règles de l'Annexe C (ex. GFI-03 : 30 j cal. avant PDR 2028-02-15 → 2028-01-16 ; GFE-02 : 90 j cal. avant INT1 2032-03-10 → 2031-12-11).
- Feuille `Hypotheses` (Annexe D) : dates GFE/GFI dérivées indicatives ; en cas de conflit, les règles de l'Annexe C priment ; aucun calendrier de jours fériés fourni.
- **Conflit détecté** : Contrat Principal §4.2 (rapport mensuel au **10e JO**) vs CDRL-005 (**7e JO**) → CONF-001.
- A1/A2 qualifiées « Acceptation contractuelle **cible** » → type CIBLE (AMBIG-001).

## État des tables de travail (DuckDB)

- `obligations` : 137 lignes
- `milestones` : 34 lignes
- `conflicts` : 1 lignes
- `ambiguities` : 5 lignes
- `documents` : 5 lignes

Aucun document source n'a été modifié (corpus en lecture seule).
