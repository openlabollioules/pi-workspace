# process-automation-bootstrap V3

Version complète du bootstrap d'automatisation.

## V3 ajoute

La V3 conserve intégralement les comportements de la V2 et ajoute la gestion générique du cycle de vie des sources entre exécutions :

- NEW
- MODIFIED
- UNCHANGED
- DELETED
- REPROCESS_REQUIRED
- content hash
- processing version
- tombstones
- invalidation ciblée des données dérivées
- reprise après interruption

Cette logique n'est activée que pour les automatisations dont les entrées peuvent évoluer entre plusieurs runs.

## Grill Me

La V3 conserve la délégation de l'entretien à :

`@firstpick/pi-extension-grill-me`

avec :

- persistance de l'état de reprise avant l'entretien ;
- contrat de continuation automatique ;
- garde-fou demandant explicitement `Poursuis le bootstrap.` si la reprise automatique échoue.

## Runtime capabilities

La V3 conserve aussi la résolution explicite des capacités runtime avant génération :

besoin logique → skill commun/domaine → extension/provider réellement disponible → outils exacts → politique offline/install.

## Installation

Remplacer le dossier commun existant par :

```text
G:\pi-workspace\.agents\skills\process-automation-bootstrap\
```

Le fichier attendu est :

```text
G:\pi-workspace\.agents\skills\process-automation-bootstrap\SKILL.md
```

## Pas de fichier de migration

Ce package ne contient volontairement aucun fichier `MIGRATION-*.md`.

La V3 est destinée aux nouveaux bootstraps. Elle ne cherche pas à migrer ou réécrire automatiquement les automatisations générées par des versions précédentes.
