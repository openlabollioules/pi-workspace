---
name: contract-obligation-register
description: Construit, consolide et met à jour un registre d'obligations contractuelles traçable à partir d'un corpus mixte PDF/XLSX. Utilise pi-office pour comprendre les documents, structured-data-duckdb/pi-alchemy pour les données structurées, DuckDB comme source de vérité persistante, un traitement incrémental par lots et des exports Markdown assemblés sans gros appels write.
---

# Contract Obligation Register

Utiliser ce skill lorsqu'il faut extraire, consolider, contrôler ou mettre à jour un registre d'obligations contractuelles depuis un corpus comprenant notamment :

- contrat principal ;
- annexes techniques ;
- CDRL / listes de livrables ;
- matrices de responsabilités ;
- planning contractuel ;
- registres ou tableaux XLSX ;
- avenants ou documents contractuels complémentaires.

L'objectif n'est pas seulement de produire un rapport. L'objectif est de construire un **état contractuel traçable, persistant et reprenable**.

---

# 1. Principes impératifs

## 1.1 DuckDB est la source de vérité de travail

Pour toute analyse de taille non triviale, ne pas conserver le registre principal uniquement dans le contexte du LLM ou dans un gros fichier Markdown.

Le registre des obligations, l'état d'avancement et les conflits doivent être persistés progressivement dans DuckDB.

Le Markdown est un **format de restitution**, pas la mémoire de travail principale.

## 1.2 Preuve et traçabilité

Une obligation ne doit être retenue que si elle est supportée par le corpus contractuel.

Pour chaque obligation, conserver au minimum :

- partie responsable ;
- action obligatoire ;
- catégorie ;
- déclencheur ;
- échéance, règle temporelle ou périodicité ;
- livrable ou preuve attendue ;
- source documentaire exacte ;
- niveau de confiance ;
- éventuelle note d'interprétation.

Ne jamais transformer :

- une bonne pratique ;
- une recommandation ;
- une hypothèse ;
- une interprétation métier ;
- une connaissance externe

en obligation contractuelle.

## 1.3 Faits, interprétations et ambiguïtés

Toujours distinguer :

- **fait contractuel** : directement supporté par une source ;
- **interprétation** : conséquence raisonnable mais non explicitement formulée ;
- **ambiguïté** : plusieurs lectures raisonnables sont possibles ;
- **conflit** : deux sources contractuelles donnent des règles incompatibles ;
- **information manquante** : le corpus ne permet pas de conclure.

Ne jamais résoudre silencieusement une ambiguïté.

## 1.4 Ne pas perdre le travail déjà validé

Le traitement doit être **reprenable après interruption**.

Avant toute nouvelle analyse :

1. vérifier si les tables DuckDB existent ;
2. vérifier l'état de `analysis_progress` ;
3. vérifier combien d'obligations sont déjà persistées ;
4. reprendre uniquement les sections ou sources non terminées ;
5. ne jamais supprimer ou reconstruire la base complète sans demande explicite.

---

# 2. Stratégie multi-format

## 2.1 PDF et documents narratifs

Utiliser `pi-office` pour :

- inventorier le document ;
- identifier les sections ;
- lire les clauses pertinentes ;
- rechercher les formulations obligatoires ;
- retrouver définitions, préséance et règles temporelles ;
- citer document + section ou repère précis.

Rechercher notamment, sans s'y limiter :

- doit ;
- devra ;
- remet ;
- fournit ;
- transmet ;
- notifie ;
- maintient ;
- organise ;
- dispose de ;
- au plus tard ;
- dans les X jours ;
- avant ;
- après ;
- à compter de ;
- chaque ;
- trimestriellement ;
- mensuellement.

Ne pas se limiter à une recherche lexicale : certaines obligations sont exprimées par une condition, un droit assorti d'un délai, une responsabilité, une règle d'acceptation ou une matrice.

## 2.2 XLSX et données structurées

Pour toute annexe tabulaire, appliquer le skill `structured-data-duckdb`.

Séquence obligatoire :

1. inspecter le classeur avec `pi-office` ;
2. identifier les feuilles pertinentes ;
3. identifier la vraie ligne d'en-tête et, si nécessaire, la plage utile ;
4. inspecter le schéma potentiel avec `DESCRIBE SELECT * FROM read_xlsx(...)` ;
5. charger la feuille utile dans DuckDB ;
6. appeler `alchemy_schema` ;
7. valider le chargement avec une requête ciblée et `LIMIT 10` ;
8. utiliser SQL pour filtrer, joindre, agréger et contrôler.

Ne jamais analyser un gros tableur cellule par cellule dans le contexte du LLM.

Ne jamais charger des milliers de lignes dans le contexte lorsqu'une requête SQL peut réduire le résultat.

---

# 3. Initialisation de la base de travail

Au début d'une mission, créer les tables de travail si elles n'existent pas déjà.

Ne pas supprimer les tables existantes sauf si l'utilisateur demande explicitement une remise à zéro.

## 3.1 Sources contractuelles

```sql
CREATE TABLE IF NOT EXISTS contract_sources (
    source_id VARCHAR PRIMARY KEY,
    file_path VARCHAR NOT NULL,
    source_type VARCHAR,
    title VARCHAR,
    precedence_rank INTEGER,
    processing_status VARCHAR,
    notes VARCHAR
);
```

Valeurs recommandées pour `processing_status` :

- `pending`
- `in_progress`
- `complete`
- `needs_review`
- `failed`

## 3.2 Progression d'analyse

```sql
CREATE TABLE IF NOT EXISTS analysis_progress (
    source_id VARCHAR NOT NULL,
    locator VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    obligations_found INTEGER DEFAULT 0,
    notes VARCHAR,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (source_id, locator)
);
```

`locator` représente une unité de traitement reprenable :

- section de contrat, par exemple `§4.1-§4.3` ;
- section d'annexe, par exemple `A8-A10` ;
- feuille XLSX, par exemple `CDRL`;
- bloc logique d'une feuille si elle est volumineuse.

## 3.3 Registre des obligations

```sql
CREATE TABLE IF NOT EXISTS obligations (
    obligation_key VARCHAR PRIMARY KEY,
    responsible_party VARCHAR NOT NULL,
    obligation_text VARCHAR NOT NULL,
    category VARCHAR,
    trigger_text VARCHAR,
    due_rule VARCHAR,
    deliverable_or_evidence VARCHAR,
    primary_source_id VARCHAR NOT NULL,
    primary_source_locator VARCHAR NOT NULL,
    secondary_sources VARCHAR,
    confidence VARCHAR,
    interpretation_note VARCHAR,
    review_status VARCHAR DEFAULT 'candidate',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Valeurs recommandées pour `confidence` :

- `Élevée`
- `Moyenne`
- `Faible`

Valeurs recommandées pour `review_status` :

- `candidate`
- `validated`
- `needs_review`
- `rejected`

## 3.4 Sources complémentaires d'une obligation

Lorsqu'une obligation est supportée par plusieurs documents, utiliser si nécessaire :

```sql
CREATE TABLE IF NOT EXISTS obligation_sources (
    obligation_key VARCHAR NOT NULL,
    source_id VARCHAR NOT NULL,
    source_locator VARCHAR NOT NULL,
    evidence_summary VARCHAR,
    is_primary BOOLEAN DEFAULT FALSE
);
```

## 3.5 Conflits et ambiguïtés

```sql
CREATE TABLE IF NOT EXISTS contract_issues (
    issue_key VARCHAR PRIMARY KEY,
    issue_type VARCHAR NOT NULL,
    subject VARCHAR NOT NULL,
    source_a VARCHAR,
    source_b VARCHAR,
    factual_finding VARCHAR,
    precedence_rule VARCHAR,
    retained_interpretation VARCHAR,
    impact VARCHAR,
    human_question VARCHAR,
    confidence VARCHAR,
    status VARCHAR DEFAULT 'open'
);
```

Valeurs recommandées pour `issue_type` :

- `conflict`
- `ambiguity`
- `missing_information`
- `date_uncertainty`

---

# 4. Identifiants stables et reprise

Ne pas utiliser immédiatement `OBL-001`, `OBL-002`, etc. comme clé interne de travail.

Utiliser une clé stable dérivée de la source, par exemple :

- `CP-4.1-01`
- `CP-10.3-02`
- `A-A12-03`
- `B-CDRL-005-01`
- `C-C5-02`
- `D-MILESTONE-A1-01`

Règles :

1. la clé doit rester stable entre deux exécutions ;
2. une reprise ne doit pas renuméroter les éléments existants ;
3. une déduplication ne doit pas obliger à réécrire tout le registre ;
4. les identifiants de présentation `OBL-001...` peuvent être générés uniquement lors de l'export final.

---

# 5. Protocole de traitement par lots

## 5.1 Ne jamais tenter une extraction monolithique

Ne jamais analyser un document complet puis tenter d'écrire toutes les obligations en une seule opération.

Traiter le corpus par unités petites et vérifiables.

Taille recommandée d'un lot :

- 1 à 3 sections contractuelles denses ; ou
- environ 5 à 15 obligations candidates ; ou
- un résultat textuel suffisamment petit pour être vérifié sans gros appel `write`.

Ces seuils sont des règles de robustesse, pas des limites techniques officielles.

## 5.2 Cycle obligatoire pour chaque lot

Pour chaque lot :

1. marquer le locator `in_progress` dans `analysis_progress` ;
2. lire uniquement les sources nécessaires ;
3. extraire les obligations candidates ;
4. atomiser les obligations ;
5. vérifier partie, déclencheur, délai et source ;
6. insérer immédiatement les obligations dans DuckDB ;
7. vérifier les lignes insérées par une requête ciblée ;
8. mettre à jour `analysis_progress` avec `complete` ou `needs_review` ;
9. passer au lot suivant.

Ne pas attendre la fin du document pour persister les résultats.

## 5.3 Après une interruption

À la reprise, commencer par :

```sql
SELECT source_id, locator, status, obligations_found, notes
FROM analysis_progress
ORDER BY source_id, locator;
```

puis :

```sql
SELECT COUNT(*) AS obligation_count
FROM obligations
WHERE review_status <> 'rejected';
```

Reprendre uniquement :

- les locators `pending` ;
- les locators `in_progress` interrompus ;
- les locators `needs_review` qui nécessitent une vérification.

Ne pas retraiter automatiquement les locators `complete`.

---

# 6. Atomisation des obligations

Une ligne doit représenter une obligation aussi atomique que raisonnablement possible.

Exemple à éviter :

> Le Titulaire remet le rapport, maintient le registre et notifie tout risque critique.

Préférer trois obligations distinctes si elles ont :

- des déclencheurs différents ;
- des délais différents ;
- des preuves différentes ;
- des sources ou responsabilités différentes.

En revanche, ne pas fragmenter artificiellement une seule obligation lorsque plusieurs éléments ne sont que le contenu obligatoire d'un même livrable.

---

# 7. Ordre de travail contractuel

Suivre cet ordre sauf raison explicite de déroger :

1. inventorier tout le corpus ;
2. enregistrer les sources dans `contract_sources` ;
3. lire en priorité :
   - définitions ;
   - liste des documents contractuels ;
   - ordre de préséance ;
   - règles de calcul des délais ;
4. planifier les locators dans `analysis_progress` ;
5. analyser le contrat principal par lots ;
6. charger les annexes XLSX utiles dans DuckDB ;
7. analyser séparément :
   - obligations du Titulaire ;
   - obligations de l'Autorité Contractante ;
   - obligations conjointes ;
8. croiser les jalons et dates avec le planning ;
9. rechercher les conflits et divergences ;
10. dédupliquer ;
11. contrôler la couverture des sources ;
12. valider les obligations ;
13. générer les restitutions finales depuis DuckDB.

---

# 8. Temporalité

Distinguer strictement :

- date fixe ;
- date calculée depuis la Date d'Effet ;
- date relative à un jalon ;
- délai en jours calendaires ;
- délai en jours ouvrés ;
- périodicité ;
- obligation déclenchée par un événement futur ;
- date cible de planning ;
- date effective.

## 8.1 Jours ouvrés

Si le calendrier des jours fériés n'est pas fourni :

- conserver la règle contractuelle en JO ;
- ne pas fabriquer une date exacte lorsque des jours fériés pourraient modifier le calcul ;
- marquer l'incertitude si nécessaire dans `contract_issues`.

## 8.2 Dates cibles et dates effectives

Ne pas remplacer une date d'acceptation effective par une date cible de planning sans le signaler.

Lorsqu'une obligation dit :

> 60 jours après acceptation

et que le planning donne une date cible A1, conserver :

- le déclencheur contractuel : acceptation effective ;
- éventuellement une date indicative basée sur A1 cible ;
- une note précisant que la date finale dépend de l'acceptation effective.

---

# 9. Conflits documentaires

Pour chaque conflit :

1. citer les deux sources ;
2. exposer factuellement la divergence ;
3. identifier la clause de préséance applicable ;
4. indiquer la valeur retenue si la préséance permet de trancher ;
5. conserver malgré tout le conflit dans `contract_issues` ;
6. indiquer une question humaine si une décision reste nécessaire.

Ne jamais masquer un conflit parce qu'une clause de préséance permet de déterminer la valeur applicable.

---

# 10. Déduplication

Avant validation finale, rechercher les obligations proches ou dupliquées.

Utiliser notamment :

- même partie ;
- même action ;
- même déclencheur ;
- même source ;
- même livrable ;
- références croisées entre contrat principal et annexes.

Lorsque plusieurs sources décrivent la même obligation :

- conserver une seule obligation logique ;
- choisir une source primaire selon la préséance et la précision ;
- enregistrer les sources complémentaires dans `obligation_sources` ou `secondary_sources`.

Ne pas supprimer une obligation uniquement parce que son texte ressemble à une autre : vérifier d'abord les déclencheurs et délais.

---

# 11. Contrôle du contexte LLM

Éviter les gros résultats d'outils.

## Interdit par défaut

```sql
SELECT * FROM obligations;
```

si la table est déjà volumineuse.

## Préférer

Comptages :

```sql
SELECT COUNT(*) FROM obligations;
```

Agrégations :

```sql
SELECT responsible_party, COUNT(*) AS n
FROM obligations
WHERE review_status <> 'rejected'
GROUP BY responsible_party
ORDER BY n DESC;
```

Contrôles ciblés :

```sql
SELECT obligation_key, primary_source_id, primary_source_locator
FROM obligations
WHERE primary_source_id IS NULL
   OR primary_source_locator IS NULL;
```

Pagination :

```sql
SELECT *
FROM obligations
ORDER BY obligation_key
LIMIT 20 OFFSET 40;
```

Projection minimale :

```sql
SELECT obligation_key, responsible_party, due_rule
FROM obligations
WHERE category = 'Essais / acceptation';
```

Ne ramener au LLM que les colonnes et lignes nécessaires à la décision courante.

---

# 12. Protocole "Large Output"

Ne jamais générer un gros fichier de sortie en un seul appel `write` ou `edit`.

Appliquer ce protocole dès qu'une sortie risque de dépasser approximativement :

- 200 lignes ;
- 20 KB de texte ;
- 30 lignes de tableau contenant du texte substantiel.

Ces seuils sont volontairement conservateurs.

## Règles

1. planifier la structure avant d'écrire ;
2. générer les données structurées dans DuckDB d'abord ;
3. ne jamais utiliser le Markdown comme stockage intermédiaire principal ;
4. pour un gros rapport, créer `output/.parts/` ;
5. écrire des fragments courts et indépendants ;
6. vérifier chaque fragment après écriture ;
7. ne jamais réécrire un fragment déjà validé sans nécessité ;
8. assembler les fragments avec le shell ;
9. vérifier le fichier assemblé ;
10. si un `write` échoue pour taille, ne jamais relancer exactement le même gros contenu.

Exemple d'assemblage :

```bash
cat output/.parts/obligations-*.md > output/obligations-register.md
```

Sous un shell Windows compatible, utiliser l'équivalent disponible si `cat` n'est pas adapté.

---

# 13. Génération du registre Markdown

`obligations-register.md` doit être généré **depuis les données validées dans DuckDB**.

Ne pas reconstruire le registre depuis la mémoire conversationnelle.

## 13.1 Validation avant export

Vérifier d'abord :

```sql
SELECT COUNT(*) AS total
FROM obligations
WHERE review_status = 'validated';
```

Puis :

```sql
SELECT responsible_party, COUNT(*) AS n
FROM obligations
WHERE review_status = 'validated'
GROUP BY responsible_party
ORDER BY responsible_party;
```

Puis rechercher les données manquantes :

```sql
SELECT obligation_key, responsible_party, obligation_text
FROM obligations
WHERE review_status = 'validated'
  AND (
      primary_source_id IS NULL
      OR primary_source_locator IS NULL
      OR obligation_text IS NULL
  );
```

Le résultat attendu de ce dernier contrôle est zéro ligne.

## 13.2 Numérotation de présentation

Lors de l'export uniquement, générer les identifiants `OBL-001...` par ordre stable.

Exemple :

```sql
SELECT
    'OBL-' || LPAD(
        CAST(ROW_NUMBER() OVER (
            ORDER BY primary_source_id, primary_source_locator, obligation_key
        ) AS VARCHAR),
        3,
        '0'
    ) AS display_id,
    obligation_key,
    responsible_party,
    obligation_text,
    category,
    trigger_text,
    due_rule,
    deliverable_or_evidence,
    primary_source_id,
    primary_source_locator,
    confidence
FROM obligations
WHERE review_status = 'validated'
ORDER BY primary_source_id, primary_source_locator, obligation_key;
```

Conserver `obligation_key` dans la base même si elle n'est pas affichée dans le rapport final.

## 13.3 Export par fragments

Si le registre est long :

1. récupérer au maximum 15 à 20 obligations à la fois ;
2. écrire :
   - `output/.parts/obligations-001-020.md`
   - `output/.parts/obligations-021-040.md`
   - etc. ;
3. chaque fragment doit contenir uniquement les lignes de tableau, sauf le premier qui peut contenir l'en-tête ;
4. vérifier chaque fragment ;
5. assembler avec le shell ;
6. contrôler le nombre de lignes finales.

---

# 14. Génération du rapport de conflits

Construire `ambiguities-and-conflicts.md` depuis `contract_issues`.

Pour chaque issue, restituer :

- type ;
- sujet ;
- sources ;
- constat factuel ;
- règle de préséance ;
- interprétation retenue si applicable ;
- impact ;
- question à poser au contract manager ;
- confiance.

Si le rapport devient volumineux, appliquer le même protocole de fragments.

---

# 15. Génération de l'Executive Summary

`executive-summary.md` doit rester court.

Le construire principalement depuis des agrégations SQL et une sélection limitée des éléments les plus importants.

Inclure au minimum :

- nombre total d'obligations validées ;
- répartition Titulaire / Autorité Contractante / conjoint ;
- principales catégories ;
- obligations à date fixe ;
- obligations récurrentes ;
- obligations déclenchées par événement ;
- nombre de conflits / ambiguïtés ;
- maximum 5 points de vigilance ;
- limites de l'analyse.

Ne jamais charger l'intégralité du registre dans le contexte uniquement pour rédiger le résumé.

---

# 16. Contrôles SQL obligatoires avant finalisation

## 16.1 Sources non traitées

```sql
SELECT *
FROM contract_sources
WHERE processing_status <> 'complete';
```

## 16.2 Locators incomplets

```sql
SELECT *
FROM analysis_progress
WHERE status <> 'complete';
```

## 16.3 Obligations sans source exploitable

```sql
SELECT obligation_key, obligation_text
FROM obligations
WHERE review_status <> 'rejected'
  AND (
      primary_source_id IS NULL
      OR primary_source_locator IS NULL
  );
```

## 16.4 Obligations à revoir

```sql
SELECT obligation_key, confidence, interpretation_note
FROM obligations
WHERE review_status = 'needs_review'
   OR confidence = 'Faible';
```

## 16.5 Répartition par partie

```sql
SELECT responsible_party, COUNT(*) AS n
FROM obligations
WHERE review_status = 'validated'
GROUP BY responsible_party
ORDER BY n DESC;
```

## 16.6 Répartition par catégorie

```sql
SELECT category, COUNT(*) AS n
FROM obligations
WHERE review_status = 'validated'
GROUP BY category
ORDER BY n DESC;
```

## 16.7 Issues ouvertes

```sql
SELECT issue_type, COUNT(*) AS n
FROM contract_issues
WHERE status = 'open'
GROUP BY issue_type;
```

---

# 17. Critères de fin de mission

Ne déclarer la mission terminée que lorsque :

- toutes les sources prévues ont été inventoriées ;
- toutes les unités d'analyse sont `complete` ou explicitement signalées `needs_review` ;
- chaque obligation validée possède une source ;
- les obligations du Titulaire ont été recherchées ;
- les obligations de l'Autorité Contractante ont été recherchées ;
- les obligations conjointes ont été recherchées ;
- les dates et jalons XLSX ont été vérifiés via DuckDB ;
- les conflits documentaires ont été recherchés ;
- les doublons ont été traités ;
- les gros résultats n'ont pas été injectés inutilement dans le contexte ;
- les sorties finales proviennent de DuckDB ;
- les gros fichiers ont été produits par fragments puis assemblés ;
- une vérification finale de cohérence a été réalisée.

---

# 18. Sorties minimales

Lorsque la mission ne précise pas un autre format, produire :

- `output/data-ingestion-report.md`
- `output/obligations-register.md`
- `output/ambiguities-and-conflicts.md`
- `output/executive-summary.md`

Le registre final doit contenir au minimum :

| ID | Partie responsable | Obligation | Catégorie | Déclencheur | Échéance / périodicité | Livrable ou preuve attendue | Source | Confiance |
|---|---|---|---|---|---|---|---|---|

Le `data-ingestion-report.md` doit indiquer au minimum :

- sources inventoriées ;
- fichiers XLSX et feuilles analysées ;
- tables DuckDB créées ;
- schémas détectés ;
- nombre de lignes chargées ;
- problèmes d'inférence ou de structure ;
- éventuelles sources non traitées.

---

# 19. Comportements interdits

Ne pas :

- produire le registre complet depuis la mémoire du LLM ;
- tenter un énorme `write` puis recommencer après échec ;
- retraiter tout le corpus après une interruption ;
- charger une table complète dans le contexte sans nécessité ;
- inventer une date en jours ouvrés sans calendrier adapté ;
- masquer un conflit contractuel ;
- déduire une obligation uniquement d'une bonne pratique ;
- supprimer la base DuckDB existante sans demande explicite ;
- remplacer silencieusement une date effective par une date cible ;
- marquer `complete` une section non vérifiée.

La priorité est : **exactitude → traçabilité → persistance → reprise → efficacité → présentation**.
