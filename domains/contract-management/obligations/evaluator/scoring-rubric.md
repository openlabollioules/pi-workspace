# Scoring Rubric — POC 1

Score conseillé sur 100.

## 1. Couverture des obligations — 40 points

Comparer aux 80 obligations minimales de `ground-truth-obligations.md`.

- 40 pts : ≥ 90 % correctement capturées
- 35 pts : 80–89 %
- 28 pts : 70–79 %
- 20 pts : 55–69 %
- 10 pts : 40–54 %
- 0 pt : < 40 %

Une obligation peut être considérée couverte même si le découpage atomique diffère, à condition que :
- l'action obligatoire soit correcte ;
- la partie responsable soit correcte ;
- le déclencheur ou l'échéance soit correctement représenté.

## 2. Traçabilité — 20 points

Échantillonner au moins 20 obligations.

- source exacte document + section : 1 pt par obligation ;
- plafonné à 20.

## 3. Temporalité — 15 points

Évaluer :
- distinction date fixe / date relative ;
- conservation des déclencheurs événementiels ;
- absence d'invention de jours fériés ;
- calculs calendaires corrects ;
- distinction acceptation cible / effective.

## 4. Conflits et ambiguïtés — 15 points

3 pts chacun pour C-A à C-E si :
- conflit identifié ;
- sources citées ;
- traitement cohérent ;
- absence de résolution inventée.

## 5. Hallucinations / faux positifs — 10 points

- 10 pts : aucun faux positif matériel ;
- 7 pts : 1–2 faux positifs mineurs ;
- 3 pts : plusieurs obligations non supportées ;
- 0 pt : hallucinations contractuelles importantes.

## Malus critique

Retirer jusqu'à 20 points si l'agent :
- invente des clauses ;
- présente une interprétation comme un fait ;
- utilise des sources externes ;
- accède au dossier `evaluator/` pendant un test à l'aveugle ;
- omet systématiquement les obligations de l'AC.

## Indicateurs complémentaires

À mesurer sans forcément les intégrer au score :
- durée totale ;
- nombre de tool calls ;
- tokens consommés ;
- nombre de fichiers lus ;
- nombre de passes de vérification ;
- qualité de l'executive summary ;
- stabilité du résultat sur 3 exécutions identiques.
