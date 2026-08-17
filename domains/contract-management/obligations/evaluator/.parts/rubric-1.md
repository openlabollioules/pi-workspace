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
