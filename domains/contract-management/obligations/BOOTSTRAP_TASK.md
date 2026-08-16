# Bootstrap de l'automatisation

Utilise le skill `process-automation-bootstrap`.

Le processus métier à automatiser est décrit dans `PROCESS_AUTOMATION.md`.

## Initialisation

Commence par :

1. lire intégralement `PROCESS_AUTOMATION.md` ;
2. prendre en compte les `AGENTS.md` hérités du niveau plateforme et du domaine ;
3. inspecter les données déjà présentes dans le workspace ;
4. réutiliser les données de test existantes sans les régénérer ni les modifier.

## Readiness

Évalue les critères de readiness R1 à R10.

Ne redemande aucune information déjà suffisamment définie dans :

- `PROCESS_AUTOMATION.md` ;
- les `AGENTS.md` ;
- les fichiers disponibles ;
- les décisions déjà enregistrées dans `.bootstrap/`.

S'il reste une information réellement bloquante, pose uniquement la question la plus importante, une par une, jusqu'à ce que tous les critères soient `CONFIRMED` ou `N/A`.

## Génération

Dès que la readiness est complète :

- génère directement le POC dans le workspace courant ;
- ne crée pas de dossier `generated-automation` ;
- crée les nouveaux skills localement dans `.agents/skills/` ;
- réutilise les skills communs et domaine existants lorsqu'ils conviennent ;
- ne modifie aucun skill partagé sans accord explicite ;
- ne déplace aucun skill vers le domaine ou le niveau commun sans accord explicite ;
- conserve les documents source existants en lecture seule ;
- utilise un état persistant lorsque nécessaire ;
- conçois le POC pour être reprenable après interruption ;
- évite les gros appels `write` ou `edit` monolithiques ;
- ne génère pas de nouvelles données de test lorsque les entrées nécessaires existent déjà ;
- génère un evaluator uniquement s'il est nécessaire et qu'aucun benchmark existant approprié n'est disponible.

## Finalisation

À la fin :

1. vérifie que le POC généré est exécutable ;
2. génère `README.md` avec les instructions d'utilisation ;
3. génère `TASK.md` avec la mission de l'agent métier ;
4. génère ou complète `.bootstrap/PROMOTION_CANDIDATES.md` ;
5. classe les composants en `LOCAL`, `DOMAIN_CANDIDATE` ou `COMMON_CANDIDATE` ;
6. ne déplace aucun composant partagé sans accord ;
7. ne lance pas encore la mission métier elle-même.