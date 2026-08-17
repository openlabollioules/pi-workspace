# Scoring Rubric — Registre des obligations FNG-01

Évaluation du POC « registre des obligations contractuelles » à partir de
`workspace/output/` et `workspace/data/`. Le `evaluator/` est lu **uniquement**
par l'évaluateur, jamais par l'agent.

## Barème (100 points)

### 1. Couverture des obligations — 50 pts
- Base : 135 obligations de référence (`ground-truth.md`, sections A–E).
- 1 point par GT couvert, normalisé : `50 × (GT couverts / 135)`.
- Une GT est **couverte** si le registre contient une ligne avec : même partie
  (CONJOINTE acceptée pour une ligne « chaque partie »), même action
  (reformulation fidèle), même source (doc + localisateur).
- Une ligne du registre peut couvrir plusieurs GT (fusion contrat + CDRL
  autorisée, cf. table H du ground truth).
- **Seuil de passage : ≥ 80 % de couverture (≥ 108 GT, soit ≥ 40 pts).**

### 2. Traçabilité — 15 pts
- 5 pts : 100 % des lignes ont `source_doc` + `source_locator` non vides
  (sinon 5 × proportion de lignes tracées).
- 5 pts : spot-check 10 lignes aléatoires — chaque localisateur existe dans le
  document cité.
- 5 pts : toutes les sources sont dans le corpus (aucun document inventé).

### 3. Conflits et ambiguïtés — 20 pts
- **CT-1** (rapport mensuel : 10e JO §4.2 vs 7e JO CDRL-005) — 6 pts :
  - 2 pts : conflit identifié avec les deux sources ;
  - 2 pts : préséance contrat principal (§2.1/§2.2) appliquée, règle retenue = 10e JO ;
  - 2 pts : conflit **consigné** malgré la résolution.
- **CT-2** (A1/A2 cible vs acceptation effective) — 4 pts :
  - 2 pts : déclencheur d'acceptation conservé, date cible non substituée ;
  - 2 pts : distinction explicite cible/effective documentée.
- **CT-3 / CT-4** — 3 pts : tension readiness 15 JO (A9/CDRL-013) vs TRR-Mer
  10 JO (Annexe C) signalée (1 pt) ; primat des règles Annexe C sur les rappels
  Annexe D consigné (2 pts).
- **Ambiguïtés (AM-1 à AM-9)** — 4 pts : au moins 4 des 9 points listés
  identifiés (1 pt chacun, max 4). Critiques : AM-2 (deux pièges
  d'acceptation tacite opposés) et AM-8 (JO sans calendrier fériés).
- **Informations manquantes** — 3 pts : absence de calendrier de jours fériés
  signalée AVEC sa conséquence (pas de dates exactes en JO).
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
