# Ground Truth — POC 1

> Fichier réservé à l'évaluation humaine. Ne pas exposer à l'agent pendant le test.

Le but n'est pas d'imposer un découpage atomique unique, mais de vérifier que les obligations importantes suivantes ont été capturées avec leur source et leur logique temporelle.

## Obligations minimales attendues

| GT | Partie | Obligation attendue | Échéance / déclencheur | Source principale |
|---|---|---|---|---|
| GT-001 | Titulaire | Transmettre dossier + ordre du jour COPIL | ≥ 5 JO avant chaque COPIL | Contrat §4.1 |
| GT-002 | AC | Commenter dossier COPIL | ≤ 2 JO avant COPIL | Contrat §4.1 |
| GT-003 | Titulaire | Émettre projet CR COPIL | 5 JO après COPIL | Contrat §4.1 |
| GT-004 | AC | Commenter projet CR COPIL | 5 JO après émission | Contrat §4.1 |
| GT-005 | Titulaire | Remettre rapport mensuel | 10e JO après fin de mois | Contrat §4.2, conflit Annexe B CDRL-005 |
| GT-006 | Titulaire | Maintenir/remettre registre des risques | Avec rapport mensuel | Contrat §4.3 + B CDRL-006 |
| GT-007 | Titulaire | Notifier risque >30 j sur jalon | 3 JO après qualification | Contrat §4.3 |
| GT-008 | Titulaire | Soumettre baseline fonctionnelle | SRR 15/04/2027 | Contrat §5.1 + Annexe D |
| GT-009 | Titulaire | Soumettre baseline définition | CDR 20/06/2029 | Contrat §5.2 + Annexe D |
| GT-010 | Titulaire | Maintenir registre configuration / états | revues majeures + livraisons | Contrat §5.3 + B CDRL-027 |
| GT-011 | Titulaire | Accuser réception DC et vérifier complétude | 10 JO après DC AC | Contrat §6.1 |
| GT-012 | Titulaire | Remettre proposition impact DC | 20 JO après informations suffisantes | Contrat §6.2 |
| GT-013 | AC | Décider sur proposition complète | 15 JO après réception | Contrat §6.3 |
| GT-014 | Titulaire | Remettre plan qualité | 60 j calendaires après DE = 30/11/2026 | Contrat §7.1 |
| GT-015 | Titulaire | Notifier NC majeure | 2 JO après classification | Contrat §7.2 |
| GT-016 | Titulaire | Rapport cause + plan action NC majeure | 10 JO après classification | Contrat §7.2 |
| GT-017 | Titulaire | Répondre constats audit | 15 JO après rapport audit | Contrat §7.3 |
| GT-018 | Titulaire | Remettre plan cybersécurité | M4 = 31/01/2027, puis tenir à jour | Contrat §8.1 + B CDRL-003 |
| GT-019 | Titulaire | Notifier vulnérabilité critique confirmée | 24 h | Contrat §8.2 |
| GT-020 | Titulaire | Remettre stratégie remédiation cyber | 5 JO après confirmation | Contrat §8.2 |
| GT-021 | Titulaire | Remettre liste fournisseurs critiques | M3 = 31/12/2026 | Contrat §9.1 |
| GT-022 | Titulaire | Notifier changement fournisseur critique | ≥20 JO avant prise d'effet | Contrat §9.1 |
| GT-023 | Titulaire | Remettre registre obsolescences | Trimestriel à compter M6 | Contrat §9.2 |
| GT-024 | Titulaire | Notifier obsolescence affectant jalon <12 mois | 5 JO après identification | Contrat §9.2 |
| GT-025 | Titulaire | Remettre procédure essai | 45 j calendaires avant essai | Contrat §10.1 + B |
| GT-026 | AC | Accepter/commenter procédure essai | 20 j calendaires après dossier complet | Contrat §10.1 |
| GT-027 | Titulaire | Notifier disponibilité TRR mer | ≥30 j calendaires avant revue souhaitée | Contrat §10.2 |
| GT-028 | Titulaire | Dossier provisoire résultats essais mer | 10 JO après campagne | Contrat §10.3 |
| GT-029 | Titulaire | Dossier consolidé résultats essais mer | 30 j calendaires après campagne | Contrat §10.3 |
| GT-030 | AC | Prononcer acceptation/refus motivé | 30 j calendaires après dossier complet | Contrat §10.4 |
| GT-031 | Titulaire | Documentation as-built | 60 j calendaires après acceptation chaque navire | Contrat §11.3 |
| GT-032 | Titulaire | Plan formation initiale | M18 = 31/03/2028 | Contrat §12.1 |
| GT-033 | AC | Liste nominative stagiaires | ≥30 j calendaires avant chaque session | Contrat §12.1 |
| GT-034 | Titulaire | Supports définitifs formation | ≥10 JO avant première session / session selon B | Contrat §12.2 + B CDRL-025 |
| GT-035 | Titulaire | Soutien initial | 12 mois après acceptation chaque bâtiment | Contrat §12.3 |
| GT-036 | Titulaire | Accuser défaut garantie | 2 JO | Contrat §13 |
| GT-037 | Titulaire | Première analyse défaut garantie | 5 JO | Contrat §13 |
| GT-038 | Titulaire | Registre éléments préexistants | CDR + chaque acceptation | Contrat §14 |
| GT-039 | Titulaire | Fournir justificatifs droits d'usage | 15 JO après demande AC | Contrat §14 |
| GT-040 | Chaque Partie | Notifier incident sécurité | ≤24 h après confirmation | Contrat §15 |
| GT-041 | Titulaire | Notifier impact planning >15 j | 3 JO après caractérisation | Contrat §16 |
| GT-042 | Titulaire | Plan de rétablissement | 10 JO après notification | Contrat §16 |
| GT-043 | AC | Contester demande paiement | 15 JO après dossier complet | Contrat §17 |
| GT-044 | Titulaire | Matrice traçabilité exigences | PDR, CDR, acceptations | A1 + B CDRL-008 |
| GT-045 | Titulaire | Organiser revue lancement technique | 30 j calendaires après DE = 31/10/2026 au plus tard | A2 |
| GT-046 | Titulaire | Documents préparatoires lancement technique | 10 JO avant revue | A2 |
| GT-047 | AC | Confirmer/commenter référentiel criticité cyber | 10 JO après revue | A2 |
| GT-048 | Titulaire | Export base exigences | SRR, PDR, CDR | A3 |
| GT-049 | Titulaire | Soumettre hypothèses liées à GFE incomplet | 5 JO après formalisation | A4 |
| GT-050 | Titulaire | Bilan masse/CG mensuel puis trimestriel | M6→CDR puis CDR→A2 | A5 |
| GT-051 | Titulaire | Déclaration version logiciel essai mer | ≥15 j calendaires avant campagne | A7 |
| GT-052 | Titulaire | Analyse risque cyber aux points clés | avant PDR, CDR, chaque essais mer, chaque acceptation | A8 |
| GT-053 | Titulaire | Dossier readiness essais quai | 15 JO avant revue | A9 |
| GT-054 | AC | Observations readiness | 5 JO avant revue si dossier à temps | A9 |
| GT-055 | Titulaire | Configuration gelée essais mer | 10 j calendaires avant départ | A10 |
| GT-056 | Titulaire | Accès données essais | 2 JO après acquisition sauf justification | A10 |
| GT-057 | Titulaire | Documentation soutien préliminaire FNG-01 | 6 mois avant A1 cible = 30/03/2033 | A11/B |
| GT-058 | Titulaire | Documentation soutien préliminaire FNG-02 | 4 mois avant A2 cible = 28/02/2034 | A11/B |
| GT-059 | Titulaire | Accusé demande soutien initial | 1 JO | A12 |
| GT-060 | Titulaire | Premier diagnostic soutien | 3 JO | A12 |
| GT-061 | Titulaire | Rapport mensuel soutien | 5e JO mois suivant | A12/B |
| GT-062 | Titulaire | Supports formation projet | 60 j calendaires avant session | A13/B |
| GT-063 | AC | Commentaires supports formation projet | 20 j calendaires après réception | A13 |
| GT-064 | Titulaire | Synthèse anomalies essais | avec chaque rapport mensuel à compter essais quai | A14 |
| GT-065 | Titulaire | Notifier anomalie bloquante | jour même classification | A14 |
| GT-066 | Titulaire | Organiser RETEX FNG-01 | ≤45 j après A1 | A15 |
| GT-067 | Titulaire | Dossier RETEX | 10 JO avant revue | A15/B |
| GT-068 | Titulaire | Plan intégration RETEX FNG-02 | 20 JO après revue | A15/B |
| GT-069 | AC | Fournir GFI/GFE selon Annexe C | multiples échéances | C2 + D3 |
| GT-070 | AC | Désigner correspondants GFE/GFI | M2 = 30/11/2026 | C2 |
| GT-071 | Titulaire | Notifier NC apparente GFE | 5 JO après réception | C3 |
| GT-072 | Titulaire | Dossiers revues SRR/PDR/CDR | 15 JO avant revue | C4 |
| GT-073 | Titulaire | Dossiers TRR/A1/A2 | 10 JO avant revue | C4 |
| GT-074 | AC | Commentaires consolidés revues majeures | 3 JO avant revue si dossier à temps | C4 |
| GT-075 | Parties conjointes | Cosigner PV revue | 10 JO après revue | C4 |
| GT-076 | Titulaire | Liste personnels accès site AC | 20 JO avant activité | C5 |
| GT-077 | AC | Confirmer accès / dossiers incomplets | 10 JO après liste | C5 |
| GT-078 | Titulaire | Définition besoin données test AC | 45 j calendaires avant besoin | C6 |
| GT-079 | AC | Fournir données test | 15 j calendaires avant essai, si demande à temps | C6 |
| GT-080 | Titulaire | Corriger livrable après commentaires | 10 JO sauf accord différent | B3 |

## Conflits / ambiguïtés attendus

### C-A — Rapport mensuel

- Contrat Principal §4.2 : **10e JO** après fin du mois contractuel.
- Annexe B CDRL-005 : **7e JO**.
- Préséance : Contrat Principal > Annexe B.
- Résultat attendu : retenir contractuellement 10e JO selon la clause de préséance, tout en signalant le conflit.

### C-B — Supports définitifs de formation

- Contrat Principal §12.2 : supports définitifs au plus tard 10 JO avant le début de la **première session**.
- Annexe B CDRL-025 : 10 JO avant **session**.
- La portée exacte (première session de chaque cursus ou chaque session) mérite d'être signalée.

### C-C — Calcul des dates en jours ouvrés

- Aucun calendrier des jours fériés n'est fourni.
- L'agent ne doit pas inventer des dates exactes lorsqu'un calcul en JO pourrait franchir un jour férié.

### C-D — Acceptation cible vs acceptation effective

- Le planning donne A1/A2 comme dates contractuelles cibles.
- Plusieurs obligations sont déclenchées par **l'acceptation effective**, qui pourrait être différente.
- L'agent doit conserver le déclencheur contractuel et ne pas remplacer systématiquement celui-ci par la date cible.

### C-E — Revue RETEX

- A15 impose une revue dans les 45 jours après acceptation FNG-01.
- Annexe D fixe RETEX1 au 10/11/2033, soit cohérent avec A1 cible du 30/09/2033.
- Si A1 effective dérive, la règle relative reste à surveiller : ne pas considérer la date fixe comme seule obligation.
