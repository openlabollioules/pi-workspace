### 4. Qualité des données — 10 pts
- 3 pts : aucune obligation sans source (toute violation → 0 pt sur ce sous-item).
- 2 pts : pas de doublon non justifié (même partie + même action + même source).
- 2 pts : parties correctes (spot-check 10 lignes ; −1 par erreur, min 0).
- 2 pts : délais en JO non convertis en dates exactes ; dates du corpus citées
  telles quelles (pas de recalcul d'échéances JO).
- 1 pt : catégories cohérentes et exploitables (filtres possibles).

### 5. Livrables et robustesse — 5 pts
- 2 pts : les 4 rapports demandés existent dans `workspace/output/`
  (registre, planning, conflits, ambiguïtés) et sont cohérents entre eux.
- 2 pts : DuckDB présent dans `workspace/data/` avec tables requises
  (documents, milestones, obligations, conflicts, ambiguities, progress) et
  données cohérentes avec les rapports.
- 1 pt : reprise démontrable — la table `progress` montre un traitement par
  lots ; relancer l'agent ne duplique pas les données (idempotence).

## Grille de décision

| Score | Verdict |
|-------|---------|
| ≥ 80 et couverture ≥ 80 % | **PASS** — POC validé |
| 60–79 | **CONDITIONAL** — corriger les manques listés, re-évaluer |
| < 60 ou couverture < 80 % | **FAIL** — itération requise |

Veto automatique (FAIL quel que soit le score) :
- obligation inventée (non sourcée dans le corpus) présentée comme contractuelle ;
- date exacte produite pour un délai en JO à partir d'un événement futur ;
- accès de l'agent au dossier `evaluator/` ;
- modification des sources dans `workspace/contract/`.

## Procédure d'évaluation

1. **Inventaire** : lister `workspace/output/` et `workspace/data/` ; vérifier
   l'intégrité des sources (aucun fichier modifié dans `workspace/contract/`).
2. **Couverture** : charger le registre (DuckDB `obligations` ou Markdown) ;
   pour chaque GT-xx du ground truth, chercher la ligne couvrante (recherche
   sémantique + vérification partie/action/source). Produire la matrice
   GT ↔ ligne du registre.
3. **Traçabilité** : spot-check 10 localisateurs dans les documents sources.
4. **Conflits/ambiguïtés** : vérifier CT-1 à CT-4 et AM-1 à AM-9 dans les
   rapports et la table `conflicts`/`ambiguities`.
5. **Robustesse** : inspecter `progress` ; relancer l'exécution si possible
   pour vérifier l'idempotence.
6. **Synthèse** : remplir le barème, calculer le score, rédiger le verdict et
   la liste des manques actionnables.
