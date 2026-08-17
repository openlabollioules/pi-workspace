# Bootstrap Readiness — obligations

Évalué le bootstrap initial (corpus déjà présent, PROCESS_AUTOMATION.md complet).

| ID | Dimension | Statut | Justification |
|----|-----------|--------|---------------|
| R1 | Objectif et résultat attendu | CONFIRMED | PROCESS_AUTOMATION §1 : registre traçable des obligations, 4 livrables, critères de succès définis. |
| R2 | Déclencheur | CONFIRMED | §3 : lancement explicite par l'utilisateur du POC. |
| R3 | Acteurs et responsabilités | CONFIRMED | §2 : Contract Manager utilisateur ; parties AC / Titulaire ; validation humaine des ambiguïtés. |
| R4 | Entrées, formats, sources | CONFIRMED | Corpus présent dans `workspace/contract/` : 2 PDF (contrat, Annexe A), 3 XLSX (Annexe B CDRL, Annexe C, Annexe D planning). Formats inspectés et validés. |
| R5 | Processus nominal | CONFIRMED | §5 : 13 étapes (inventaire → préséance → lecture → DuckDB → extraction par lots → persistance → croisement planning → conflits → dédoublonnage → traçabilité → livrables). |
| R6 | Règles de décision et exceptions | CONFIRMED | §6–7 : source obligatoire par obligation, préséance §2.1 contrat, signalement des conflits, JO sans calendrier fériés, cible vs effective, reprise depuis état persistant. |
| R7 | Sorties attendues | CONFIRMED | §8 : 4 fichiers dans `workspace/output/`, colonnes minimales du registre définies. |
| R8 | Validations humaines et actions interdites | CONFIRMED | §9 + AGENTS.md domaine : extraction AUTONOME ; ambiguïté non tranchable VALIDATION_HUMAINE ; qualification juridique et modification des sources INTERDIT. |
| R9 | Contraintes techniques, permissions, données | CONFIRMED | §10 : Windows 11, Pi, pi-office, pi-alchemy/DuckDB, sources en lecture seule, écriture `workspace/data/` + `workspace/output/`. |
| R10 | Critères d'acceptation et scénario de test | CONFIRMED | §12 : ~80 obligations de référence, ≥ 80 % de couverture MVP, source obligatoire, conflits préparés détectés, AC couverte, pas d'accès au ground truth, reprise possible. |

**Conclusion : R1–R10 CONFIRMED. Aucune contradiction bloquante. Génération autorisée.**
