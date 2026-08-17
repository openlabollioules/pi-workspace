---
name: process-automation-bootstrap
description: Interviewe un expert métier ou analyse PROCESS_AUTOMATION.md afin de définir une automatisation agentique prête à tester. Génère d'abord agents et skills localement dans le workspace courant, puis évalue quels composants pourraient être promus au niveau domaine ou commun sans les déplacer automatiquement.
---

# Process Automation Bootstrap — MVP local-first

## Mission

Transformer une description métier incomplète en une automatisation agentique minimale, testable et documentée.

Le bootstrap suit quatre principes :

1. **local-first** : tout nouveau composant est créé dans le workspace courant ;
2. **test-before-promote** : aucun skill n'est placé directement dans un catalogue partagé ;
3. **promotion explicite** : après génération, proposer ce qui pourrait devenir domaine ou commun ;
4. **no automatic promotion** : ne jamais déplacer un composant hors du workspace sans demande explicite de l'utilisateur.

---

# 1. Convention d'arborescence

La plateforme d'automatisation est un dépôt ou répertoire de travail séparé de la configuration globale de Pi.

Dans l'environnement de référence :

```text
G:\pi-workspace\
```

est la racine de la plateforme.

La configuration globale de Pi reste dans son emplacement par défaut :

```text
~/.pi/agent/
```

Ne pas confondre ces deux emplacements.

La convention cible est :

```text
G:\pi-workspace\
├── .agents\
│   └── skills\                         # skills communs à tous les domaines
│
└── domains\
    ├── contract-management\
    │   ├── AGENTS.md                   # règles partagées du domaine, si utile
    │   ├── .agents\
    │   │   └── skills\                 # skills partagés Contract Management
    │   │
    │   ├── obligations\                # automation/workspace
    │   │   ├── PROCESS_AUTOMATION.md
    │   │   ├── AGENTS.md
    │   │   ├── TASK.md
    │   │   ├── .agents\
    │   │   │   └── skills\             # skills locaux en incubation
    │   │   ├── agents\
    │   │   ├── workspace\
    │   │   ├── test-data\
    │   │   ├── evaluator\
    │   │   └── .bootstrap\
    │   │
    │   ├── changes\
    │   └── correspondence\
    │
    ├── quality\
    │   ├── .agents\
    │   │   └── skills\
    │   ├── non-conformities\
    │   └── audits\
    │
    └── ivvq\
        ├── .agents\
        │   └── skills\
        ├── test-analysis\
        └── requirements-coverage\
```

Il n'est pas nécessaire d'ajouter un niveau intermédiaire `automations/`.

Chaque sous-répertoire fonctionnel du domaine peut être directement un workspace d'automatisation.

---

# 2. Détermination du contexte

Au démarrage, identifier :

```text
CURRENT_WORKSPACE
DOMAIN_DIR
PLATFORM_ROOT
```

Dans la structure conventionnelle :

```text
G:\pi-workspace\domains\contract-management\obligations
```

on a :

```text
CURRENT_WORKSPACE = G:\pi-workspace\domains\contract-management\obligations
DOMAIN_DIR        = G:\pi-workspace\domains\contract-management
PLATFORM_ROOT     = G:\pi-workspace
```

Ne pas dépendre aveuglément d'un nombre fixe de `../`.

Pour identifier ces niveaux :

1. partir du workspace courant ;
2. rechercher le parent correspondant au domaine ;
3. rechercher un ancêtre contenant `domains/` et éventuellement `.agents/skills/` ;
4. considérer cet ancêtre comme racine de plateforme ;
5. si la structure est ambiguë, conserver tous les composants localement et ne demander le chemin de promotion que lorsqu'une promotion est réellement souhaitée.

---

# 3. Entrées

Chercher en priorité à la racine du workspace courant :

```text
PROCESS_AUTOMATION.md
```

S'il existe :

- le lire intégralement ;
- exploiter les informations déjà présentes ;
- ne pas redemander une information suffisamment explicite ;
- relever contradictions, ambiguïtés et informations manquantes.

S'il n'existe pas :

- démarrer l'interview ;
- créer progressivement `PROCESS_AUTOMATION.md`.

Ne pas inventer le fonctionnement métier à partir de connaissances externes.

---

# 4. État persistant du bootstrap

Créer :

```text
.bootstrap/
├── READINESS.md
├── DECISIONS.md
├── ASSUMPTIONS.md
├── OPEN_QUESTIONS.md
└── PROMOTION_CANDIDATES.md
```

Ces fichiers doivent permettre de reprendre une session interrompue.

---

# 5. Readiness MVP

Évaluer ces 10 dimensions :

| ID | Dimension |
|---|---|
| R1 | Objectif métier et résultat attendu |
| R2 | Déclencheur |
| R3 | Acteurs et responsabilités |
| R4 | Entrées, formats et sources |
| R5 | Processus nominal |
| R6 | Règles de décision et exceptions critiques |
| R7 | Sorties attendues |
| R8 | Validations humaines et actions interdites |
| R9 | Contraintes techniques, permissions et données |
| R10 | Critères d'acceptation et scénario de test |

Statuts autorisés :

```text
UNKNOWN
PARTIAL
CONFIRMED
N/A
```

La génération commence uniquement lorsque R1 à R10 sont `CONFIRMED` ou `N/A` et qu'aucune contradiction bloquante n'est ouverte.

---

# 6. Interview

## Une question à la fois

Ne jamais envoyer un questionnaire massif.

Choisir la question qui réduit le plus l'incertitude bloquante.

## Ne pas redemander ce qui est connu

Avant chaque question, vérifier :

- `PROCESS_AUTOMATION.md` ;
- les fichiers fournis ;
- `.bootstrap/DECISIONS.md` ;
- les réponses précédentes.

## Chercher activement les exceptions

Vérifier notamment :

- que faire si une entrée manque ;
- quel cas sort du processus nominal ;
- que faire si deux sources se contredisent ;
- que faire si une étape échoue après qu'une partie du travail a déjà été persistée.

---

# 7. Gate de génération

Lorsque R1 à R10 sont prêts :

1. résumer l'automatisation ;
2. enregistrer `AUTOMATION_READY` dans `.bootstrap/DECISIONS.md` ;
3. concevoir l'architecture minimale ;
4. générer immédiatement les composants dans le workspace courant.

Ne pas demander de confirmation supplémentaire si l'utilisateur a déjà demandé la génération dès que le système est prêt.

---

# 8. Architecture minimale

Toujours préférer :

```text
1 agent principal
+ quelques skills spécialisés
+ outils existants
+ état persistant si nécessaire
```

Ne créer plusieurs agents que si une raison claire existe :

- permissions différentes ;
- contexte réellement différent ;
- expertise spécialisée ;
- isolation de risque ;
- parallélisation utile.

Le nombre d'agents doit rester minimal.

---

# 9. Génération local-first

## 9.1 Agent principal

Créer au niveau du workspace courant :

```text
AGENTS.md
TASK.md
```

`AGENTS.md` contient les règles de comportement de l'agent principal.

`TASK.md` contient une mission directement exécutable.

## 9.2 Skills locaux de l'automatisation

Tous les nouveaux skills doivent être créés initialement dans :

```text
CURRENT_WORKSPACE\.agents\skills\<skill-name>\SKILL.md
```

Exemple :

```text
G:\pi-workspace\domains\contract-management\obligations\
└── .agents\
    └── skills\
        └── contract-obligation-register\
            └── SKILL.md
```

Ne pas créer un nouveau skill directement au niveau domaine ou commun.

Ne pas utiliser `.pi/skills/` pour un skill portable, sauf nécessité explicite liée à Pi.

Le contenu d'un skill métier doit autant que possible rester indépendant du harness.

## 9.3 Agents supplémentaires

Si plusieurs agents sont réellement nécessaires, créer leurs spécifications dans :

```text
agents\<agent-name>\AGENTS.md
```

Ces fichiers sont des spécifications locales d'agents.

Toute adaptation spécifique à Pi, Hermes ou un autre runtime doit rester séparée de la logique métier portable.

---

# 10. Arborescence minimale générée

Le bootstrap doit viser :

```text
CURRENT_WORKSPACE\
├── PROCESS_AUTOMATION.md
├── AUTOMATION_SPEC.md
├── README.md
├── AGENTS.md
├── TASK.md
│
├── .agents\
│   └── skills\
│       └── <local-skill>\
│           └── SKILL.md
│
├── agents\
│   └── <optional-agent>\
│       └── AGENTS.md
│
├── workspace\
│   ├── input\
│   ├── data\
│   └── output\
│
├── test-data\
├── evaluator\
│   ├── ground-truth.md
│   └── scoring-rubric.md
│
└── .bootstrap\
    ├── READINESS.md
    ├── DECISIONS.md
    ├── ASSUMPTIONS.md
    ├── OPEN_QUESTIONS.md
    └── PROMOTION_CANDIDATES.md
```

Ne pas créer un niveau `generated-automation/`.

Le workspace courant est directement le projet d'automatisation généré.

---

# 11. Réutilisation avant création

Avant de créer un nouveau skill local :

1. rechercher les skills déjà visibles dans le workspace ;
2. rechercher les skills du domaine ;
3. rechercher les skills communs ;
4. comparer leur finalité avec le besoin ;
5. préférer la réutilisation d'un skill existant lorsqu'il couvre le besoin ;
6. ne créer un nouveau skill local que si aucune capacité existante ne convient suffisamment.

Dans la structure de référence, vérifier notamment :

```text
CURRENT_WORKSPACE\.agents\skills\
DOMAIN_DIR\.agents\skills\
PLATFORM_ROOT\.agents\skills\
```

Ne jamais modifier directement un skill partagé sans demande explicite.

---

# 12. Données et état persistants

Si le processus est volumineux, multi-étapes ou doit reprendre après interruption, préférer DuckDB ou un autre stockage structuré local.

Le POC doit alors :

- définir les tables nécessaires ;
- persister les progrès ;
- traiter les résultats par lots ;
- éviter les gros fichiers intermédiaires ;
- générer les rapports depuis l'état persistant.

---

# 13. Données de test existantes : priorité absolue

Avant de générer la moindre donnée synthétique, le bootstrap doit inspecter le workspace courant et `PROCESS_AUTOMATION.md` afin de déterminer si les données de test nécessaires existent déjà.

## 13.1 Recherche des données existantes

Vérifier notamment :

```text
CURRENT_WORKSPACE\workspace\
CURRENT_WORKSPACE\workspace\input\
CURRENT_WORKSPACE\workspace\contract\
CURRENT_WORKSPACE\test-data\
```

ainsi que tout emplacement explicitement déclaré dans `PROCESS_AUTOMATION.md`.

Pour chaque entrée requise par le processus, déterminer :

```text
PRESENT
MISSING
OPTIONAL
```

## 13.2 Règle de priorité

Les données existantes ont toujours priorité sur la génération synthétique.

Si toutes les entrées nécessaires sont présentes :

- les réutiliser telles quelles ;
- ne pas générer de nouveau corpus ;
- ne pas écraser les fichiers ;
- ne pas modifier les fichiers source ;
- ne pas créer de copie équivalente inutile.

Si certaines entrées seulement sont manquantes :

1. conserver toutes les entrées existantes ;
2. identifier précisément les entrées manquantes ;
3. générer uniquement les éléments manquants si `PROCESS_AUTOMATION.md` l'autorise ;
4. documenter ce qui a été généré.

Ne jamais régénérer tout un corpus uniquement parce qu'une entrée est absente.

## 13.3 Corpus déclaré immuable

Si `PROCESS_AUTOMATION.md` indique qu'un corpus existant doit être réutilisé, le traiter comme source en lecture seule.

Exemple :

```text
workspace\contract\
├── 01-contrat-principal.pdf
├── 02-annexe-a-specification-technique.pdf
├── 03-annexe-b-livrables-cdrl.xlsx
├── 04-annexe-c-responsabilites.xlsx
└── 05-planning-contractuel.xlsx
```

Le bootstrap peut :

- inventorier ces fichiers ;
- inspecter leurs noms, formats et disponibilité ;
- les référencer dans `AUTOMATION_SPEC.md`, `TASK.md` et le README.

Le bootstrap ne doit pas :

- les modifier ;
- les renommer sans nécessité ;
- les remplacer ;
- créer une nouvelle version synthétique du même corpus.

## 13.4 Ne pas perdre de temps à analyser en profondeur le corpus pendant le bootstrap

Le bootstrap doit seulement inspecter le corpus existant assez pour :

- vérifier qu'il correspond aux entrées attendues ;
- identifier les formats ;
- préparer l'architecture de l'automatisation ;
- préparer le benchmark si nécessaire.

Il ne doit pas exécuter à ce stade la mission métier complète.

Par exemple, pour une automatisation d'extraction d'obligations contractuelles, le bootstrap n'a pas à extraire toutes les obligations du contrat avant de générer l'agent métier.

---

# 14. Evaluator et ground truth existants

Le benchmark est distinct des données d'entrée de l'agent métier.

## 14.1 Si aucun evaluator n'existe

Si aucun benchmark utilisable n'existe et que le POC doit être mesurable, créer :

```text
evaluator\
├── ground-truth.md
└── scoring-rubric.md
```

ou une structure équivalente adaptée au processus.

## 14.2 Si un evaluator existe déjà

Si le bootstrap trouve un evaluator existant déclaré comme référence :

- le conserver tel quel ;
- ne pas le régénérer ;
- ne pas le réécrire ;
- ne pas le simplifier ;
- ne pas le déplacer dans `workspace\` ;
- ne jamais le rendre accessible à l'agent métier pendant son exécution.

Un evaluator existant est une **référence de test**, pas une source métier.

## 14.3 Isolation du ground truth

La structure recommandée est :

```text
CURRENT_WORKSPACE\
├── workspace\             # visible par l'agent métier lors du test
│   ├── contract\
│   ├── data\
│   └── output\
│
└── evaluator\             # hors du workspace d'exécution
    ├── ground-truth.md
    └── scoring-rubric.md
```

Lors du lancement ultérieur de l'automatisation métier, l'utilisateur doit pouvoir ouvrir uniquement :

```text
CURRENT_WORKSPACE\workspace\
```

sans exposer :

```text
CURRENT_WORKSPACE\evaluator\
```

à l'agent testé.

## 14.4 Evaluator externe

Si l'utilisateur conserve un benchmark hors du workspace courant, le bootstrap ne doit pas exiger qu'il soit copié.

Il peut simplement documenter dans le README qu'un benchmark externe peut être utilisé après l'exécution.

---

# 15. Données synthétiques : uniquement en dernier recours

Générer des données synthétiques seulement si au moins une entrée requise est absente et qu'aucun corpus existant approprié n'est disponible.

Dans ce cas :

- générer un corpus synthétique réaliste ;
- inclure un scénario nominal ;
- inclure au moins une exception ;
- inclure au moins une ambiguïté ou contradiction pertinente ;
- créer un ground truth séparé si nécessaire.

Avant génération, vérifier une dernière fois qu'un fichier équivalent n'existe pas déjà.

La règle est :

```text
EXISTING DATA
    ↓
REUSE

PARTIAL DATA
    ↓
KEEP EXISTING + GENERATE ONLY MISSING

NO DATA
    ↓
GENERATE SYNTHETIC DATA
```


# 16. Classification des composants après génération

Après avoir généré le POC localement, examiner chaque skill et chaque agent/spec d'agent.

Attribuer une recommandation parmi :

```text
LOCAL
DOMAIN_CANDIDATE
COMMON_CANDIDATE
```

## LOCAL

Conserver local si le composant :

- dépend fortement du processus courant ;
- contient des règles propres à l'automatisation ;
- dépend d'un format ou système spécifique à ce projet ;
- n'a pas encore été suffisamment testé.

Destination :

```text
CURRENT_WORKSPACE\.agents\skills\
```

## DOMAIN_CANDIDATE

Proposer le niveau domaine si le composant :

- exprime une capacité métier réutilisable ;
- pourrait servir à plusieurs automatisations du même métier ;
- ne dépend pas des noms, données ou contraintes d'un seul projet.

Destination proposée :

```text
DOMAIN_DIR\.agents\skills\<skill-name>\
```

Exemple Contract Management :

```text
G:\pi-workspace\domains\contract-management\
└── .agents\
    └── skills\
        └── contract-obligation-register\
```

## COMMON_CANDIDATE

Proposer le niveau commun si le composant :

- n'est pas spécifique au métier ;
- apporte une capacité technique ou méthodologique générique ;
- peut être utilisé dans plusieurs domaines.

Destination proposée :

```text
PLATFORM_ROOT\.agents\skills\<skill-name>\
```

Exemple :

```text
G:\pi-workspace\
└── .agents\
    └── skills\
        └── structured-data-duckdb\
```

---

# 17. Règles de promotion

La promotion est une proposition, jamais une action implicite.

Après génération et premier test, créer ou mettre à jour :

```text
.bootstrap\PROMOTION_CANDIDATES.md
```

Format recommandé :

```markdown
# Promotion candidates

## contract-obligation-register

Current:
`.agents/skills/contract-obligation-register/`

Recommendation:
`DOMAIN_CANDIDATE`

Suggested destination:
`G:/pi-workspace/domains/contract-management/.agents/skills/contract-obligation-register/`

Reason:
Capacité spécifique au Contract Management mais réutilisable par plusieurs automatisations du domaine.

Status:
PROPOSED
```

Statuts possibles :

```text
PROPOSED
ACCEPTED
REJECTED
PROMOTED
```

Ne jamais déplacer le composant tant que l'utilisateur n'a pas explicitement accepté.

---

# 18. Vérifications avant promotion

Avant de promouvoir un skill :

1. vérifier qu'un skill du même nom n'existe pas déjà à destination ;
2. rechercher des skills fonctionnellement proches ;
3. supprimer les références propres au workspace courant ;
4. vérifier que la `description` reste valable au nouveau périmètre ;
5. supprimer les chemins locaux codés en dur ;
6. vérifier les dépendances au harness ;
7. adapter les références relatives si nécessaire ;
8. conserver une seule source de vérité après promotion.

Ne pas conserver silencieusement deux copies divergentes du même skill.

---

# 19. Promotion d'un skill local vers le domaine

Exemple :

```text
AVANT

G:\pi-workspace\domains\contract-management\obligations\
└── .agents\skills\
    └── contract-obligation-register\
        └── SKILL.md
```

Après accord utilisateur :

```text
APRÈS

G:\pi-workspace\domains\contract-management\
└── .agents\skills\
    └── contract-obligation-register\
        └── SKILL.md
```

Le workspace `obligations` doit ensuite utiliser le skill partagé et ne plus conserver une copie locale divergente.

---

# 20. Promotion du domaine vers le commun

Un skill déjà partagé au niveau domaine peut ultérieurement être proposé comme commun.

Exemple :

```text
AVANT

G:\pi-workspace\domains\contract-management\
└── .agents\skills\
    └── structured-data-duckdb\
```

Après validation qu'il n'est réellement pas spécifique au Contract Management :

```text
APRÈS

G:\pi-workspace\
└── .agents\skills\
    └── structured-data-duckdb\
```

Ne pas promouvoir directement un composant non testé de LOCAL vers COMMON sauf raison explicite.

Préférer :

```text
LOCAL → DOMAIN → COMMON
```

lorsque l'expérience de plusieurs automatisations justifie progressivement l'élargissement.

---

# 21. Portabilité entre harness

Pour les composants destinés à être partagés :

- préférer `.agents/skills/` ;
- respecter la structure `skill-name/SKILL.md` ;
- placer scripts, références et templates sous le dossier du skill ;
- exprimer les besoins métier en capacités génériques ;
- isoler les adaptations Pi/Hermes dans des scripts, extensions ou configurations spécifiques.

La portabilité du `SKILL.md` ne garantit pas la portabilité des outils utilisés.

---

# 22. README généré

Le README de l'automatisation doit expliquer :

- l'objectif métier ;
- comment fournir les données ;
- comment lancer le POC ;
- quels résultats attendre ;
- comment utiliser l'evaluator ;
- quels skills locaux sont créés ;
- quels skills partagés sont réutilisés.

Les détails de promotion restent dans :

```text
.bootstrap\PROMOTION_CANDIDATES.md
```

---

# 23. Critère de simplicité

Avant de finaliser :

> Puis-je supprimer un agent, un skill, une table ou un fichier sans perdre une capacité importante ?

Si oui, simplifier.

Le cycle de vie de référence est :

```text
créer local
    ↓
tester
    ↓
évaluer la réutilisabilité
    ↓
proposer DOMAIN ou COMMON
    ↓
promotion explicite
```

Tous les nouveaux composants commencent localement.
