---
name: process-automation-bootstrap
description: Transforme une description de processus métier en automatisation agentique minimale prête à tester. S'appuie sur @firstpick/pi-extension-grill-me pour l'entretien déterministe et la persistance des décisions, puis ajoute la readiness métier R1-R10, l'inspection existing-data-first, la génération local-first, l'evaluator, la reprise automatique après entretien et la classification de promotion.
---

# Process Automation Bootstrap — V3

## Mission

Transformer une description métier, éventuellement incomplète, en une automatisation agentique minimale, testable, traçable, reprenable et documentée.

Cette V3 **ne réimplémente pas le moteur d'entretien interactif**.

Lorsqu'une clarification humaine est nécessaire, elle délègue à :

```text
@firstpick/pi-extension-grill-me
```

et à ses mécanismes natifs.

Le bootstrap ajoute uniquement ce qui est spécifique à la conception et à la génération d'une automatisation métier :

- lecture de `PROCESS_AUTOMATION.md` et des artefacts disponibles ;
- readiness R1 à R10 ;
- détection des lacunes réellement bloquantes ;
- inspection des données existantes avant toute génération synthétique ;
- gestion du cycle de vie des sources entre exécutions (ajout, modification, suppression, retraitement) ;
- Definition of Ready déterministe ;
- orchestration de l'entretien Grill Me lorsque nécessaire ;
- reprise automatique demandée après l'entretien ;
- garde-fou si la reprise automatique ne se produit pas ;
- architecture minimale ;
- génération local-first ;
- réutilisation des skills existants ;
- état persistant ;
- test data et evaluator si nécessaires ;
- classification LOCAL / DOMAIN_CANDIDATE / COMMON_CANDIDATE ;
- documentation et vérification finale.

---

# 1. Répartition des responsabilités

## Grill Me possède

Ne pas réimplémenter dans ce skill :

- le principe « une question à la fois » ;
- l'enregistrement structuré de chaque question ;
- la recommandation proposée par l'assistant ;
- la réponse explicite de l'utilisateur ;
- le statut résolu / non résolu ;
- les notes d'entretien ;
- la persistance de la session d'entretien ;
- la génération du résumé d'entretien.

Ces fonctions appartiennent à Grill Me.

## Le bootstrap possède

Le bootstrap reste responsable de :

```text
PROCESS_AUTOMATION.md
BOOTSTRAP_TASK.md
.bootstrap/READINESS.md
.bootstrap/ASSUMPTIONS.md
.bootstrap/OPEN_QUESTIONS.md
.bootstrap/PROMOTION_CANDIDATES.md
AUTOMATION_SPEC.md
AGENTS.md
TASK.md
README.md
.agents/skills/*
agents/*
workspace/*
test-data/*
evaluator/*
```

Il traduit les informations connues et les décisions Grill Me en readiness R1-R10 et poursuit jusqu'à la fin du bootstrap.

---

# 2. Précondition Grill Me

Cette V3 suppose que l'extension suivante est installée dans Pi :

```text
@firstpick/pi-extension-grill-me
```

Si une interview est nécessaire et qu'aucune session Grill Me n'est active, ne simule pas Grill Me avec une interview maison.

Le bootstrap doit préparer une commande `/grill-me` ciblée sur les dimensions de readiness encore insuffisantes.

Exemple conceptuel :

```text
/grill-me Compléter la définition de l'automatisation décrite dans
PROCESS_AUTOMATION.md jusqu'à satisfaire uniquement les dimensions R1-R10
encore PARTIAL ou UNKNOWN. Ne pas redemander les informations déjà établies.
À la fin de l'entretien, sauvegarder les résultats, réévaluer R1-R10 et
reprendre immédiatement le bootstrap sans attendre une nouvelle instruction
de l'utilisateur.
```

Une fois Grill Me actif, utiliser ses mécanismes natifs pour toute clarification.

Ne pas dupliquer l'historique détaillé de Grill Me dans un journal parallèle.

---

# 3. Convention d'arborescence

Structure de référence :

```text
G:\pi-workspace\
├── AGENTS.md
├── .agents\
│   └── skills\                         # COMMON
│
└── domains\
    ├── contract-management\
    │   ├── AGENTS.md
    │   ├── .agents\
    │   │   └── skills\                 # DOMAIN
    │   │
    │   ├── obligations\                # automation/workspace
    │   │   ├── PROCESS_AUTOMATION.md
    │   │   ├── BOOTSTRAP_TASK.md
    │   │   ├── AUTOMATION_SPEC.md
    │   │   ├── AGENTS.md
    │   │   ├── TASK.md
    │   │   ├── README.md
    │   │   ├── .agents\
    │   │   │   └── skills\             # LOCAL
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
    └── ivvq\
```

Ne pas créer de niveau intermédiaire `automations/`.

La configuration globale de Pi :

```text
~/.pi/agent/
```

n'est pas une source à explorer pour découvrir les artefacts métier ou les skills de la plateforme.

---

# 4. Détermination du contexte

Identifier au démarrage :

```text
CURRENT_WORKSPACE
DOMAIN_DIR
PLATFORM_ROOT
```

Exemple :

```text
CURRENT_WORKSPACE = G:\pi-workspace\domains\contract-management\obligations
DOMAIN_DIR        = G:\pi-workspace\domains\contract-management
PLATFORM_ROOT     = G:\pi-workspace
```

Ne pas dépendre d'un nombre fixe de `../`.

Chercher la racine de plateforme à partir de la structure `domains/` et des répertoires `.agents/skills/`.

Si la structure est ambiguë :

- garder toute nouvelle création localement ;
- ne demander une précision de chemin que si elle devient réellement nécessaire.

---

# 5. Entrées

Chercher en priorité :

```text
PROCESS_AUTOMATION.md
BOOTSTRAP_TASK.md
AGENTS.md hérités
workspace/
workspace/input/
workspace/contract/
test-data/
evaluator/
```

Lire intégralement `PROCESS_AUTOMATION.md` s'il existe.

Ne pas redemander une information déjà suffisamment définie dans :

- `PROCESS_AUTOMATION.md` ;
- les `AGENTS.md` hérités ;
- les fichiers présents ;
- les résultats Grill Me déjà persistés ;
- `.bootstrap/READINESS.md`.

Ne pas inventer le fonctionnement métier à partir de connaissances externes.

---

# 6. État persistant

Créer :

```text
.bootstrap/
├── READINESS.md
├── ASSUMPTIONS.md
├── OPEN_QUESTIONS.md
└── PROMOTION_CANDIDATES.md
```

Ne pas créer `.bootstrap/DECISIONS.md` par défaut.

Les décisions interactives sont déjà enregistrées par Grill Me.

## READINESS.md

`READINESS.md` est la vue canonique de l'état du bootstrap.

Il doit contenir deux parties :

### A. Readiness métier

R1 à R10.

### B. État d'exécution du bootstrap

Utiliser exactement ces champs :

```text
BOOTSTRAP_PHASE: ASSESSMENT | INTERVIEW | GENERATION | VALIDATION | COMPLETE
RESUME_AFTER_INTERVIEW: true | false
NEXT_ACTION: <action explicite>
AUTOMATION_READY: YES | NO
```

Exemple avant Grill Me :

```text
BOOTSTRAP_PHASE: INTERVIEW
RESUME_AFTER_INTERVIEW: true
NEXT_ACTION: REASSESS_READINESS_AND_GENERATE
AUTOMATION_READY: NO
```

Exemple pendant génération :

```text
BOOTSTRAP_PHASE: GENERATION
RESUME_AFTER_INTERVIEW: false
NEXT_ACTION: GENERATE_MINIMAL_POC
AUTOMATION_READY: YES
```

Exemple final :

```text
BOOTSTRAP_PHASE: COMPLETE
RESUME_AFTER_INTERVIEW: false
NEXT_ACTION: NONE
AUTOMATION_READY: YES
```

## ASSUMPTIONS.md

Contient uniquement les hypothèses du bootstrap qui ne sont pas des décisions humaines explicites.

## OPEN_QUESTIONS.md

Contient uniquement les lacunes encore ouvertes, avec référence vers la dimension R concernée.

Ne pas recopier l'historique détaillé de Grill Me.

---

# 7. Readiness métier R1-R10

Évaluer :

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

Statuts :

```text
UNKNOWN
PARTIAL
CONFIRMED
N/A
```

Pour chaque dimension, `READINESS.md` doit contenir :

```text
Status
Evidence
Blocking gap
Source
```

Sources possibles :

```text
PROCESS_AUTOMATION.md
AGENTS.md
existing file/data
Grill Me decision
user instruction
```

Ne pas marquer `CONFIRMED` une dimension reposant uniquement sur une supposition non validée.

---

# 8. Analyse avant interview

Avant de déclencher Grill Me :

1. lire les descriptions disponibles ;
2. inspecter les artefacts utiles ;
3. inventorier les données présentes ;
4. remplir R1-R10 avec les informations déjà établies ;
5. identifier uniquement les lacunes réellement bloquantes.

Si R1-R10 sont déjà `CONFIRMED` ou `N/A`, **ne pas lancer Grill Me inutilement**.

Passer directement au gate de génération.

---

# 9. Utilisation de Grill Me

Lorsque des dimensions restent `UNKNOWN` ou `PARTIAL` et empêchent la génération :

1. produire la liste des gaps ;
2. classer les gaps par impact ;
3. persister l'état de reprise dans `READINESS.md` ;
4. construire une seule commande `/grill-me` ciblée ;
5. demander à l'utilisateur de lancer cette commande ;
6. laisser Grill Me gérer l'entretien ;
7. lorsque l'entretien est terminé, reprendre automatiquement le bootstrap ;
8. mettre à jour `READINESS.md` ;
9. réévaluer R1-R10 ;
10. continuer jusqu'à `COMPLETE`.

## État obligatoire avant bascule vers Grill Me

Avant d'afficher la commande `/grill-me`, écrire :

```text
BOOTSTRAP_PHASE: INTERVIEW
RESUME_AFTER_INTERVIEW: true
NEXT_ACTION: REASSESS_READINESS_AND_GENERATE
AUTOMATION_READY: NO
```

---

# 10. Contrat de continuation automatique Grill Me

Toute commande `/grill-me` proposée par le bootstrap DOIT inclure explicitement un contrat de continuation.

Le texte peut être adapté au contexte, mais doit imposer les comportements suivants :

```text
Lorsque toutes les décisions bloquantes de l'entretien sont résolues :

1. sauvegarder/finaliser les résultats Grill Me avec son mécanisme natif ;
2. considérer que la session Grill Me n'est qu'une étape du
   process-automation-bootstrap en cours ;
3. relire `.bootstrap/READINESS.md` ;
4. réévaluer R1-R10 avec les décisions obtenues ;
5. mettre à jour les statuts de readiness ;
6. si la Definition of Ready est satisfaite, poursuivre immédiatement
   la génération du POC ;
7. ne pas attendre que l'utilisateur dise "continue", "resume",
   "poursuis le bootstrap" ou équivalent ;
8. poursuivre jusqu'à ce que BOOTSTRAP_PHASE soit COMPLETE ou qu'un
   nouveau blocage nécessitant réellement l'utilisateur soit identifié.
```

Le bootstrap ne doit donc pas considérer la fin de l'entretien comme la fin de sa mission.

---

# 11. Garde-fou de reprise après Grill Me

Le contrat de continuation automatique peut ne pas être exécuté parfaitement par le modèle ou le harness.

Il faut donc un garde-fou supplémentaire.

## Règle

Si, après l'entretien :

```text
BOOTSTRAP_PHASE: INTERVIEW
RESUME_AFTER_INTERVIEW: true
```

est toujours présent et que l'entretien Grill Me est terminé ou ne nécessite plus de réponse utilisateur, le système doit afficher explicitement un message de garde-fou.

Message recommandé :

```text
L'entretien Grill Me est terminé, mais le bootstrap n'a pas encore repris.

Demande explicitement :
"Poursuis le bootstrap."

Le bootstrap doit alors relire `.bootstrap/READINESS.md`, réévaluer R1-R10
et reprendre à partir de NEXT_ACTION.
```

Le message peut être formulé dans la langue de l'utilisateur.

## Quand afficher ce garde-fou

Afficher ce message uniquement si les trois conditions sont vraies :

```text
1. BOOTSTRAP_PHASE = INTERVIEW
2. RESUME_AFTER_INTERVIEW = true
3. Grill Me n'attend plus de réponse utilisateur
```

Ne pas afficher le garde-fou pendant qu'une question Grill Me attend encore une réponse.

Ne pas l'afficher si le bootstrap a déjà repris.

---

# 12. Détection d'un bootstrap interrompu

À chaque nouveau tour lié à cette automatisation, vérifier `READINESS.md`.

Si :

```text
BOOTSTRAP_PHASE != COMPLETE
```

alors le bootstrap doit traiter la mission comme **reprenable**.

Règles :

### Si phase = ASSESSMENT

Continuer l'évaluation R1-R10.

### Si phase = INTERVIEW

- vérifier si Grill Me attend encore une réponse ;
- si oui, continuer l'entretien ;
- si non et `RESUME_AFTER_INTERVIEW = true`, reprendre le bootstrap ;
- si la reprise ne s'est toujours pas produite, afficher le garde-fou.

### Si phase = GENERATION

Reprendre la génération à partir de `NEXT_ACTION`.

### Si phase = VALIDATION

Reprendre les vérifications finales.

### Si phase = COMPLETE

Ne rien régénérer inutilement.

---

# 13. Definition of Ready / gate

La génération peut commencer uniquement si :

```text
R1..R10 = CONFIRMED ou N/A
```

et si :

```text
aucune contradiction bloquante ouverte
aucune entrée obligatoire non résolue sans stratégie
aucune action interdite ambiguë
un scénario de test existe ou est N/A de façon justifiée
```

Quand le gate est atteint :

1. mettre à jour :

```text
AUTOMATION_READY: YES
BOOTSTRAP_PHASE: GENERATION
RESUME_AFTER_INTERVIEW: false
NEXT_ACTION: GENERATE_MINIMAL_POC
```

2. si une session Grill Me vient de se terminer, finaliser ses résultats ;
3. ne pas demander une seconde confirmation si l'utilisateur a déjà demandé de générer dès que prêt ;
4. poursuivre immédiatement.

---

# 14. Existing-data-first

Avant toute génération de données synthétiques, inspecter au minimum :

```text
CURRENT_WORKSPACE\workspace\
CURRENT_WORKSPACE\workspace\input\
CURRENT_WORKSPACE\workspace\contract\
CURRENT_WORKSPACE\test-data\
```

et tout chemin déclaré dans `PROCESS_AUTOMATION.md`.

Pour chaque entrée requise :

```text
PRESENT
MISSING
OPTIONAL
```

## Toutes les entrées existent

```text
EXISTING → REUSE
```

- réutiliser ;
- ne pas régénérer ;
- ne pas écraser ;
- ne pas modifier ;
- ne pas créer une copie équivalente.

## Corpus partiel

```text
PARTIAL → KEEP + GENERATE ONLY MISSING
```

- conserver les fichiers présents ;
- identifier les éléments manquants ;
- ne générer que les éléments manquants si autorisé et utile.

## Aucun corpus utilisable

```text
NO DATA → GENERATE
```

Générer le plus petit corpus réaliste permettant de tester l'automatisation.

## Inspection ≠ exécution métier

Le bootstrap peut inventorier et inspecter les formats.

Il ne doit pas exécuter toute la mission métier simplement pour reconstruire des données de test qui existent déjà.

---

# 15. Evaluator et ground truth existants

Avant de créer un evaluator, inspecter :

```text
evaluator/
test-data/
```

Si un benchmark ou ground truth existe :

- le préserver ;
- ne pas le régénérer ;
- ne pas le modifier ;
- ne pas le déplacer dans `workspace/` ;
- ne jamais l'exposer à l'agent métier évalué.

Si le benchmark est externe au workspace, ne pas exiger sa copie.

Créer un nouvel evaluator seulement si :

- aucun evaluator approprié n'existe ;
- ou l'utilisateur le demande explicitement.

---

# 16. Réutilisation des skills avant création

Chercher dans cet ordre :

```text
CURRENT_WORKSPACE\.agents\skills\
DOMAIN_DIR\.agents\skills\
PLATFORM_ROOT\.agents\skills\
```

Pour chaque besoin :

1. identifier la capacité nécessaire ;
2. rechercher un skill existant ;
3. comparer sa portée et ses dépendances ;
4. le réutiliser s'il couvre suffisamment le besoin ;
5. ne créer un skill local que si aucune capacité existante ne convient.

Ne pas modifier un skill DOMAIN ou COMMON sans accord explicite.

---

# 17. Runtime capability resolution

Before generating implementation instructions for any required capability:

1. identify the logical capability required;
2. inspect the capabilities/tools already exposed by the current harness;
3. inspect reusable COMMON and DOMAIN skills that abstract this capability;
4. resolve the logical capability to an existing runtime implementation;
5. record the exact tool names the generated automation must use;
6. record whether the capability is already installed and usable offline.

When a required capability is already available:

- explicitly state that it is already available;
- name the provider/extension;
- name the exact tools to use;
- prohibit redundant installation attempts;
- prohibit Internet searches/downloads when the environment is offline;
- do not ask the business agent to discover the runtime implementation itself.

Generated skills must describe HOW to invoke required capabilities,
not merely name the underlying technology.

Example:

BAD:

"Use DuckDB to store obligations."

GOOD:

"Use the existing `structured-data-duckdb` capability backed in Pi by
`@nqbao/pi-alchemy`. Use `alchemy_query`, `alchemy_tables`,
`alchemy_schema`, and `alchemy_load` where applicable. DuckDB is embedded;
do not look for a CLI or attempt installation."

---

# 18. Source lifecycle and change management

Lorsqu'une automatisation consomme une collection persistante de fichiers, documents ou autres sources susceptibles d'évoluer entre deux exécutions, le bootstrap doit définir explicitement une stratégie de réconciliation des sources avant de générer l'architecture finale.

Cette gestion ne doit pas être ajoutée systématiquement aux automatisations purement one-shot ou dont les entrées sont immuables par définition.

## 18.1 Déterminer la politique de mutation

Pour chaque collection de sources persistantes, déterminer si elle est :

```text
APPEND_ONLY
MUTABLE
REPLACEABLE
DELETABLE
```

et préciser :

```text
Can new sources appear?
Can existing sources be modified?
Can existing sources disappear?
Must modified/deleted sources invalidate derived data?
Must source history be preserved?
```

Si une réponse est réellement nécessaire pour concevoir correctement l'automatisation et n'est pas déductible des artefacts existants, la traiter comme un gap de readiness et utiliser Grill Me si nécessaire.

Ne pas demander ces précisions si elles ne changent pas la conception du POC.

## 18.2 Registre persistant des sources

Pour une collection mutable ou incrémentale, générer un registre persistant des sources.

Préférer DuckDB ou un autre stockage structuré déjà résolu par la section Runtime capability resolution lorsque :

- le nombre de sources peut croître ;
- l'automatisation doit reprendre après interruption ;
- des résultats dérivés doivent rester reliés à leurs sources ;
- les changements doivent être détectés entre plusieurs runs.

Le registre devrait contenir, lorsque pertinent :

```text
source_id
relative_path
file_name
file_size
modified_at
content_hash
status
first_seen_at
last_seen_at
last_processed_at
processing_version
```

`source_id` doit être stable autant que possible.

`content_hash` doit être utilisé pour détecter une modification réelle de contenu.

Ne pas se fier uniquement :

- au nom de fichier ;
- à la date de modification ;
- à la taille du fichier.

Ces métadonnées peuvent servir de préfiltre, mais le hash reste la preuve de changement de contenu lorsque cela est nécessaire.

## 18.3 Réconciliation obligatoire au début du run

Pour les automatisations concernées, le `TASK.md` et les skills générés doivent imposer une phase de source reconciliation avant le traitement métier.

Comparer :

```text
sources actuellement présentes
vs
sources connues dans l'état persistant
```

Classifier chaque source :

```text
NEW
MODIFIED
UNCHANGED
DELETED
REPROCESS_REQUIRED
```

### NEW

Source présente maintenant mais absente du registre.

Action typique :

```text
register
→ extract/parse
→ process
→ persist derived data
→ mark processed
```

### UNCHANGED

Même source et même `content_hash`, avec une `processing_version` encore valide.

Action :

```text
skip expensive reprocessing
```

Ne pas retraiter inutilement une source inchangée.

### MODIFIED

Source connue mais `content_hash` différent.

Action :

```text
preserve source history if required
→ invalidate affected derived data
→ reprocess source
→ rebuild impacted results
```

Ne pas modifier ligne par ligne des résultats dérivés non fiables si une reconstruction déterministe de la portion impactée est plus sûre.

### DELETED

Source connue dans l'état persistant mais absente du corpus actuel.

Ne pas supprimer immédiatement son historique.

Préférer un tombstone :

```text
status = DELETED
last_seen_at = <last known time>
```

Puis déterminer quelles données dérivées doivent :

```text
remain valid
lose one source link
be downgraded in confidence
be invalidated
be rebuilt
```

### REPROCESS_REQUIRED

Le fichier n'a pas changé, mais la logique de traitement a évolué.

Exemples :

```text
skill version changed
extraction schema changed
business rule changed
processing_version changed
```

Action :

```text
reprocess even if content_hash is unchanged
```

## 18.4 Version de traitement

Les résultats persistants qui dépendent d'une logique susceptible d'évoluer doivent conserver une version de traitement.

Exemple :

```text
processing_version = obligation-register-v3
```

Règle recommandée :

```text
same content_hash
+ same processing_version
→ UNCHANGED

different content_hash
→ MODIFIED

same content_hash
+ different processing_version
→ REPROCESS_REQUIRED
```

La `processing_version` doit refléter une version fonctionnelle significative, pas chaque modification triviale de fichier.

## 18.5 Traçabilité des données dérivées

Toute donnée dérivée importante doit rester reliée à ses sources lorsque la traçabilité métier l'exige.

Exemple conceptuel :

```text
derived_record
    │
    └── derived_record_sources
            ├── derived_record_id
            ├── source_id
            ├── source_locator
            ├── source_hash
            └── processing_version
```

Cette relation permet de recalculer uniquement la partie impactée lorsqu'une source change ou disparaît.

## 18.6 Invalidation ciblée

Lorsqu'une source est `MODIFIED`, `DELETED` ou `REPROCESS_REQUIRED` :

1. identifier les résultats qui en dépendent ;
2. invalider uniquement ce qui est impacté ;
3. préserver les résultats indépendants ;
4. recalculer les agrégats, conflits ou synthèses qui dépendent des données invalidées ;
5. conserver la provenance de l'ancienne version si l'audit l'exige.

Éviter deux extrêmes :

```text
retraiter tout le corpus à chaque run
```

et :

```text
ne jamais remettre en cause les anciennes données dérivées
```

## 18.7 Reprise après interruption

La source reconciliation elle-même doit être reprenable si elle peut être longue.

Pour chaque source, persister si utile :

```text
DISCOVERED
REGISTERED
PROCESSING
PROCESSED
FAILED
INVALIDATED
DELETED
```

Un redémarrage ne doit pas :

- retraiter les sources déjà terminées sans raison ;
- perdre le statut des fichiers supprimés ;
- créer des doublons ;
- oublier une invalidation déjà identifiée.

## 18.8 Generated runtime contract

Si la gestion de changements de sources est applicable, les artefacts générés doivent préciser explicitement cette capacité.

### Dans AUTOMATION_SPEC.md

Ajouter une section :

```text
Source lifecycle
```

décrivant au minimum :

```text
mutation policy
source registry
change detection
content hash strategy
processing version strategy
derived-data invalidation
deletion/tombstone policy
resume behavior
```

### Dans TASK.md

Ajouter une règle du type :

```text
Always reconcile the current input corpus against persistent source state
before business processing.

Do not assume that the source collection is identical to the previous run.
Process only NEW, MODIFIED or REPROCESS_REQUIRED sources unless a full
rebuild is explicitly required.

Handle DELETED sources according to the configured invalidation policy.
```

### Dans les skills métier générés

Décrire concrètement :

- comment inventorier les sources ;
- comment calculer ou obtenir le hash ;
- quelle table/structure persiste l'état ;
- comment détecter les suppressions ;
- comment invalider les données dérivées ;
- comment versionner le traitement ;
- comment reprendre après interruption.

Ne pas se contenter d'écrire :

```text
Support incremental updates.
```

Le comportement doit être exécutable.


---

# 19. Architecture minimale

Préférer :

```text
1 agent principal
+ skills existants
+ quelques skills locaux réellement nécessaires
+ outils existants
+ stockage persistant si nécessaire
```

Créer plusieurs agents uniquement pour une raison forte :

- permissions différentes ;
- isolation de risque ;
- contexte spécialisé réellement distinct ;
- parallélisation utile ;
- séparation évaluateur / agent testé.

Le bootstrap doit pouvoir justifier chaque agent supplémentaire.

---

# 20. Génération local-first

Tout nouveau composant commence localement.

## Agent principal

Créer ou compléter :

```text
AGENTS.md
TASK.md
AUTOMATION_SPEC.md
README.md
```

## Skills locaux

Créer sous :

```text
CURRENT_WORKSPACE\.agents\skills\<skill-name>\SKILL.md
```

Ne pas créer directement un nouveau skill dans DOMAIN ou COMMON.

## Agents additionnels

Si nécessaires :

```text
agents\<agent-name>\AGENTS.md
```

## Pas de generated-automation

Le workspace courant est directement l'automatisation.

Ne pas créer :

```text
generated-automation/
```

---

# 21. Données et état d'exécution

Pour un processus volumineux, multi-étapes ou reprenable :

- préférer DuckDB ou un stockage structuré local ;
- définir des identifiants stables ;
- persister la progression ;
- traiter par lots ;
- rendre les étapes idempotentes autant que possible ;
- générer les rapports depuis l'état persistant.

Ne pas utiliser un énorme fichier Markdown comme base de données d'exécution.

---

# 22. Gros résultats

Si les sorties sont volumineuses :

```text
workspace/output/.parts/
```

peut contenir les fragments intermédiaires.

Prévoir :

- traitement par lots ;
- assemblage final ;
- reprise après interruption ;
- absence de régénération inutile des fragments validés.

Éviter les appels `write/edit` monolithiques.

---

# 23. Données synthétiques si réellement nécessaires

Si aucun corpus utilisable n'existe, créer le minimum permettant de tester :

- scénario nominal ;
- au moins une exception pertinente ;
- ambiguïté ou contradiction si la mission doit savoir les traiter ;
- ground truth séparé de l'espace visible par l'agent métier.

La génération synthétique doit suivre les contraintes établies par R1-R10.

---

# 24. AUTOMATION_SPEC.md

Générer une spécification concise contenant :

```text
Objective
Trigger
Actors
Inputs
Nominal flow
Decision rules
Critical exceptions
Outputs
Human-in-the-loop
Forbidden actions
Technical constraints
Runtime dependencies
Source lifecycle
Persistence strategy
Acceptance criteria
Test strategy
Reused components
New local components
```

Elle doit être cohérente avec `READINESS.md`.

Ne pas recopier tout l'historique Grill Me.

---

# 25. TASK.md

`TASK.md` est la mission d'exécution de l'agent métier.

Il ne doit pas contenir la mission du bootstrap.

Il doit préciser :

- quoi lire ;
- quoi produire ;
- quels chemins utiliser ;
- quelles actions sont autonomes ;
- quelles actions nécessitent validation humaine ;
- quelles actions sont interdites ;
- comment reprendre après interruption ;
- comment utiliser les skills réutilisés.

---

# 26. BOOTSTRAP_TASK.md

`BOOTSTRAP_TASK.md` reste distinct de `TASK.md`.

Il peut demander :

```text
Use process-automation-bootstrap.
Read PROCESS_AUTOMATION.md and inherited AGENTS.md.
Inspect existing data before generating anything.
Evaluate R1-R10.
If clarification is needed, use the installed Grill Me workflow rather
than implementing a separate interview loop.
Persist resume state before starting Grill Me.
After Grill Me finishes, resume automatically.
If automatic resume fails, show the explicit resume safeguard.
Generate the POC once the Definition of Ready is satisfied.
Do not execute the business mission itself yet.
```

---

# 27. Classification après génération

Classer chaque nouveau composant :

```text
LOCAL
DOMAIN_CANDIDATE
COMMON_CANDIDATE
```

## LOCAL

- spécifique à l'automatisation ;
- encore peu testé ;
- dépend de conventions locales.

Destination :

```text
CURRENT_WORKSPACE\.agents\skills\
```

## DOMAIN_CANDIDATE

- capacité métier réutilisable dans plusieurs automatisations du même domaine ;
- pas liée aux noms/données d'un seul POC.

Destination proposée :

```text
DOMAIN_DIR\.agents\skills\<skill-name>\
```

## COMMON_CANDIDATE

- capacité technique ou méthodologique générique ;
- utile dans plusieurs domaines.

Destination proposée :

```text
PLATFORM_ROOT\.agents\skills\<skill-name>\
```

---

# 28. Promotion

Créer ou mettre à jour :

```text
.bootstrap\PROMOTION_CANDIDATES.md
```

Statuts :

```text
PROPOSED
ACCEPTED
REJECTED
PROMOTED
```

La promotion est une proposition.

Ne jamais déplacer automatiquement un composant.

---

# 29. Vérification avant promotion

Avant toute promotion :

1. vérifier les doublons ;
2. rechercher les capacités fonctionnellement proches ;
3. supprimer les chemins spécifiques au workspace ;
4. vérifier la description et la portée ;
5. vérifier les dépendances au harness ;
6. adapter les références relatives ;
7. éviter deux copies divergentes.

Préférer :

```text
LOCAL → DOMAIN → COMMON
```

quand l'expérience le justifie.

---

# 30. Portabilité entre harness

Pour les skills partageables :

- utiliser `.agents/skills/` ;
- respecter `skill-name/SKILL.md` ;
- exprimer les besoins en capacités plutôt qu'en détails Pi ;
- isoler les extensions/runtime adapters spécifiques.

## Exception assumée : phase d'interview

Cette V3 utilise Grill Me comme adapter d'entretien lorsqu'elle s'exécute sous Pi.

La logique métier R1-R10, la reprise, la génération et la promotion restent portables.

Sur un autre harness sans Grill Me :

- ne pas prétendre que l'extension existe ;
- utiliser une capacité d'entretien équivalente si elle est explicitement disponible ;
- sinon signaler que la phase interactive dépend d'un adapter de harness.

Ne pas copier le comportement interne de Grill Me dans le skill portable.

---

# 31. README généré

Le README de l'automatisation doit expliquer :

- objectif métier ;
- données attendues ;
- lancement ;
- résultats ;
- reprise ;
- evaluator ;
- skills réutilisés ;
- skills locaux créés.

Les détails de promotion restent dans :

```text
.bootstrap/PROMOTION_CANDIDATES.md
```

Les détails d'entretien restent dans les artefacts Grill Me.

---

# 32. Vérification finale

Avant de terminer :

1. vérifier que R1-R10 sont prêts ;
2. vérifier que les entrées existantes n'ont pas été écrasées ;
3. vérifier que le ground truth n'est pas visible par l'agent métier ;
4. vérifier que chaque nouveau skill commence LOCAL ;
5. vérifier que les skills partagés n'ont pas été modifiés ;
6. vérifier que `TASK.md` est exécutable ;
7. vérifier que la reprise après interruption est prévue ;
8. vérifier que le README permet de lancer le POC ;
9. vérifier que les composants inutiles ont été supprimés ;
10. vérifier que la stratégie de cycle de vie des sources est définie si les entrées peuvent évoluer entre deux runs ;
11. ne pas lancer la mission métier si le bootstrap devait seulement la générer.

Puis écrire :

```text
BOOTSTRAP_PHASE: COMPLETE
RESUME_AFTER_INTERVIEW: false
NEXT_ACTION: NONE
AUTOMATION_READY: YES
```

Critère de simplicité :

> Peut-on supprimer un agent, un skill, une table ou un fichier sans perdre une capacité importante ?

Si oui, simplifier.

---

# 33. Résumé du cycle V3

```text
PROCESS_AUTOMATION.md + AGENTS + existing artifacts
                    │
                    ▼
             assess R1-R10
                    │
          ┌─────────┴─────────┐
          │                   │
       READY              GAPS BLOCKING
          │                   │
          │                   ▼
          │          persist resume state
          │                   │
          │                   ▼
          │                Grill Me
          │          deterministic interview
          │                   │
          │                   ▼
          │             decisions persisted
          │                   │
          │                   ▼
          │           automatic continuation
          │                   │
          │          ┌────────┴────────┐
          │          │                 │
          │       success          no resume
          │          │                 │
          │          │                 ▼
          │          │          explicit safeguard:
          │          │          "Poursuis le bootstrap."
          │          │
          └──────────┴──────────────┐
                                    ▼
                             update R1-R10
                                    │
                                    ▼
                            Definition of Ready
                                    │
                                    ▼
                        inspect/reuse existing data
                                    │
                                    ▼
                     resolve runtime capabilities
                                    │
                                    ▼
                   define source lifecycle if applicable
                                    │
                                    ▼
                          minimal local-first POC
                                    │
                                    ▼
                           evaluator if needed
                                    │
                                    ▼
                      promotion candidates + README
                                    │
                                    ▼
                     BOOTSTRAP_PHASE = COMPLETE
```

Principe clé :

```text
Grill Me = HOW to interview
Bootstrap = WHAT must be known + WHAT to generate + WHEN to resume + HOW sources evolve
```
