# Conflits et ambiguïtés

Méthode : conflit = deux sources contractuelles incompatibles ; tranché par l'ordre de préséance §2.1 (Contrat Principal > Annexe A > B > C > D) quand la préséance le permet, sinon soumis à validation humaine. Ambiguïté = plusieurs lectures raisonnables ou information manquante ; jamais tranchée sans validation.

## Conflits détectés

### CONF-001 — TRANCHE_PAR_PRESEANCE

- **Conflit** : Echeance du rapport mensuel d'avancement : le Contrat Principal §4.2 fixe le 10e JO apres la fin du mois contractuel, tandis que CDRL-005 (Annexe B) fixe le 7e JO apres la fin du mois contractuel.
- **Sources** : `01-contrat-principal §4.2` vs `03-annexe-b-livrables-cdrl, CDRL-005`
- **Préséance appliquée** : Contrat Principal §2.1 : le Contrat Principal prevaut sur l'Annexe B
- **Résolution** : Delai retenu : 10e JO apres la fin du mois contractuel (OBL-0010, statut EN_CONFLIT)

## Ambiguïtés ouvertes (à validation humaine)
### AMBIG-001 — OUVERT

- **Constat** : Les jalons A1 et A2 sont des dates d'acceptation CIBLE (Annexe D, qualifiees 'Acceptation contractuelle cible'). La date effective d'acceptation depend du processus §10.4 (acceptation ou rejet sous 30 jours calendaires). Les periodes de soutien initial (12 mois) et de garantie (24 mois) sont ancrees sur l'acceptation effective, dont la date exacte est inconnue.
- **Sources** : 05-planning-contractuel (Milestones A1/A2) ; 01-contrat-principal §10.4, §12.3, §13
- **Lectures possibles** : Lecture 1 : A1/A2 sont des cibles de planning et l'acceptation effective peut survenir a une date differente. Lecture 2 : A1/A2 sont les dates butoirs d'acceptation.

### AMBIG-002 — OUVERT

- **Constat** : Le corpus ne fournit aucun calendrier de jours feries. Les delais exprimes en jours ouvrables (JO) ne peuvent etre convertis en dates exactes ; seules les regles contractuelles sont conservees dans le registre.
- **Sources** : 01-contrat-principal §1 ; 05-planning-contractuel (Hypotheses)
- **Lectures possibles** : Lecture unique : conserver la regle contractuelle en JO sans produire de date exacte.

### AMBIG-003 — OUVERT

- **Constat** : Le terme 'revue majeure' est utilise (Contrat §5.3 ; CDRL-003 ; CDRL-027) sans definition contractuelle : l'ensemble des revues concernees n'est pas explicitement liste.
- **Sources** : 01-contrat-principal §5.3 ; 03-annexe-b-livrables-cdrl, CDRL-003/CDRL-027
- **Lectures possibles** : Lecture 1 : SRR, PDR, CDR (revues de conception). Lecture 2 : inclut egalement TRR-Mer et les revues d'acceptation.

### AMBIG-004 — OUVERT

- **Constat** : Le jalon KO de l'Annexe D ('Revue de lancement programme', 2026-10-20) et la 'Revue de Lancement Technique' de l'Annexe A §A2 (dans les 30 jours calendaires suivant la DE, soit avant le 31-10-2026) designent vraisemblablement le meme evenement, mais les libelles differe et aucun lien explicite n'est fait.
- **Sources** : 05-planning-contractuel (KO) ; 02-annexe-a-specification-technique §A2
- **Lectures possibles** : Lecture 1 : meme revue (KO = Revue de Lancement). Lecture 2 : deux revues distinctes de lancement (programme vs technique).

### AMBIG-005 — OUVERT

- **Constat** : Le mecanisme de l'indication contraire approuvee n'est pas specifie : §10.1 'sauf indication contraire de l'Annexe B' et CDRL-014 'sauf indication contraire approuvee' renvoient a un processus de derogation non detaille dans le corpus.
- **Sources** : 01-contrat-principal §10.1 ; 03-annexe-b-livrables-cdrl, CDRL-014
- **Lectures possibles** : Lecture unique : une derogation ecrite approuvee serait requise, mais le corpus ne precise ni l'organe ni la forme.

## Règle de préséance (rappel)

§2.1 du Contrat Principal : en cas de conflit, le Contrat Principal prévaut sur l'Annexe A, qui prévaut sur l'Annexe B, qui prévaut sur l'Annexe C, qui prévaut sur l'Annexe D. Tout conflit identifié doit être signalé à l'autre partie sous 10 JO (§2.2).
