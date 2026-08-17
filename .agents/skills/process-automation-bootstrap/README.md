# process-automation-bootstrap V2

Version complète avec orchestration Grill Me et reprise.

## Principes

`@firstpick/pi-extension-grill-me` possède la mécanique d'entretien.

`process-automation-bootstrap` possède :

- readiness R1-R10 ;
- Definition of Ready ;
- existing-data-first ;
- génération local-first ;
- evaluator ;
- reprise automatique ;
- garde-fou de reprise ;
- promotion LOCAL / DOMAIN / COMMON.

## Installation

Remplacer :

```text
G:\pi-workspace\.agents\skills\process-automation-bootstrap\
```

par le contenu de ce package.

L'extension Grill Me reste installée séparément.

## Reprise après entretien

Avant Grill Me, le bootstrap persiste :

```text
BOOTSTRAP_PHASE: INTERVIEW
RESUME_AFTER_INTERVIEW: true
NEXT_ACTION: REASSESS_READINESS_AND_GENERATE
```

La commande `/grill-me` proposée doit inclure un contrat demandant la reprise automatique.

Si cette reprise automatique ne se produit pas alors que l'entretien est fini, le skill demande explicitement à l'utilisateur :

```text
Poursuis le bootstrap.
```

Ce message est un garde-fou et non le workflow nominal.

## Fin du bootstrap

Un bootstrap n'est terminé que lorsque :

```text
BOOTSTRAP_PHASE: COMPLETE
```
