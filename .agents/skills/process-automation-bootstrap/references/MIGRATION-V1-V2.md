# Migration V1 → V2

## Entretien

La V2 délègue la mécanique d'entretien à `@firstpick/pi-extension-grill-me`.

Elle ne réimplémente plus :

- une question à la fois ;
- stockage des réponses ;
- resolved/unresolved ;
- journal détaillé d'entretien.

## `.bootstrap/DECISIONS.md`

N'est plus créé par défaut.

Un ancien fichier peut rester comme archive V1.

## Nouvel état dans READINESS.md

Ajouter :

```text
BOOTSTRAP_PHASE
RESUME_AFTER_INTERVIEW
NEXT_ACTION
AUTOMATION_READY
```

## Nouveau comportement

Avant Grill Me :

```text
BOOTSTRAP_PHASE: INTERVIEW
RESUME_AFTER_INTERVIEW: true
NEXT_ACTION: REASSESS_READINESS_AND_GENERATE
```

À la fin de Grill Me :

- reprise automatique demandée ;
- réévaluation R1-R10 ;
- génération immédiate si ready.

Si la reprise échoue :

```text
L'entretien Grill Me est terminé, mais le bootstrap n'a pas repris.
Demande explicitement : "Poursuis le bootstrap."
```

## Fin

```text
BOOTSTRAP_PHASE: COMPLETE
RESUME_AFTER_INTERVIEW: false
NEXT_ACTION: NONE
```
