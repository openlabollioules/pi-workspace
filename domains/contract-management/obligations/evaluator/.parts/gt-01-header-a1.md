# Ground Truth — Registre des obligations (corpus FNG-01)

Corpus de référence (lecture seule) : `workspace/contract/`
- `01-contrat-principal.pdf` (ACN-FNG-2026-001, 9 pages, §§1–18)
- `02-annexe-a-specification-technique.pdf` (ACN-FNG-2026-001-A, 6 pages, §A1–A15)
- `03-annexe-b-livrables-cdrl.xlsx` (ACN-FNG-2026-001-B : CDRL 30 lignes + Submission Rules B1–B3)
- `04-annexe-c-responsabilites.xlsx` (ACN-FNG-2026-001-C : GFE-GFI 9, Titulaire GFE 4, Joint Reviews 6, Review Minutes 1, Site Access 2, Test Data 2)
- `05-planning-contractuel.xlsx` (ACN-FNG-2026-001-D : Milestones 19, Training 6, GFE-GFI Derived 9, Assumptions 3)

Parties : **AC** = Agence des Capacités Navales ; **Titulaire** = Navisys Défense Maritime SAS.
DE = 1er octobre 2026. Préséance décroissante (§2.1/§2.2) : contrat > A > B > C > D.

**Mode d'emploi** : chaque GT-xx est une obligation de référence distincte. Couverture =
correspondance sémantique (même partie + même action + même source), pas littérale. Une ligne
du registre de l'agent peut couvrir plusieurs GT-xx. Les CDRL qui redonnent une obligation du
contrat ou de l'Annexe A ne sont pas comptés deux fois (table de dédoublonnage, section H).
Total de référence : **135 références** (134 obligations + 1 règle de remise GT-100).

## A. Contrat principal

| ID | Partie | Obligation | Source |
|----|--------|------------|--------|
| GT-01 | CONJOINTE | Notifier à l'autre partie toute contradiction identifiée dans les 10 JO suivant sa découverte | §2.2 |
| GT-02 | AC | Fournir les éléments GFE/GFI de l'Annexe C aux dates de l'Annexe D | §3.2 |
| GT-03 | Titulaire | Signaler tout retard GFE/GFI susceptible d'affecter un jalon dans les 5 JO après avoir pu caractériser l'impact | §3.2 |
| GT-04 | CONJOINTE | Tenir un COPIL une fois par trimestre civil | §4.1 |
| GT-05 | Titulaire | Transmettre l'ordre du jour et le dossier COPIL au moins 5 JO avant chaque COPIL | §4.1 |
| GT-06 | AC | Transmettre ses commentaires sur le dossier COPIL au plus tard 2 JO avant le COPIL | §4.1 |
| GT-07 | Titulaire | Émettre le projet de compte rendu COPIL dans les 5 JO suivant le COPIL | §4.1 |
| GT-08 | AC | Formuler ses observations sur le compte rendu COPIL dans les 5 JO suivants ; à défaut, réputé accepté | §4.1 |
| GT-09 | Titulaire | Remettre le rapport mensuel au plus tard le 10e JO après fin de chaque mois contractuel (contenu minimal : planning, jalons, risques, changements, qualité, maturité documentaire, approvisionnements, marges) | §4.2 |
| GT-10 | Titulaire | Maintenir le registre des risques et le mettre à disposition avec chaque rapport mensuel | §4.3 |
| GT-11 | Titulaire | Notifier tout risque nouvellement identifié à impact potentiel > 30 jours sur un Jalon Contractuel dans les 3 JO suivant sa qualification | §4.3 |
| GT-12 | Titulaire | Soumettre la Baseline Fonctionnelle à l'approbation de l'AC au jalon SRR | §5.1 |
| GT-13 | Titulaire | Soumettre la Baseline de Définition à l'approbation de l'AC au jalon CDR | §5.2 |
| GT-14 | Titulaire | Après CDR : aucune modification de la Baseline de Définition (coût, délai, performance, sécurité, interfaces externes) sans traitement selon le processus §6 | §5.3 |
| GT-15 | Titulaire | Tenir un registre de configuration et remettre un état de configuration de référence à chaque revue majeure et chaque livraison de bâtiment | §5.3 |
| GT-16 | Titulaire | Accuser réception d'une DC de l'AC dans les 10 JO suivant réception et indiquer si les informations sont suffisantes | §6.1 |
| GT-17 | Titulaire | Remettre la proposition d'impact dans les 20 JO (coûts, planning, performances, risques, documentation, essais, soutien, autres lots) | §6.2 |
| GT-18 | Titulaire | S'il ne peut remettre l'analyse complète dans les 20 JO, proposer une date alternative motivée avant expiration | §6.2 |
| GT-19 | CONJOINTE | Aucune DC à impact prix ou Jalon Contractuel mise en œuvre sans accord écrit de l'AC | §6.3 |
| GT-20 | AC | Notifier sa décision sur une proposition d'impact complète dans les 15 JO suivant réception | §6.3 |
| GT-21 | Titulaire | Remettre le Plan de Management de la Qualité dans les 60 jours calendaires suivant la DE | §7.1 |
| GT-22 | Titulaire | Notifier toute non-conformité majeure dans les 2 JO suivant sa classification comme majeure | §7.2 |
| GT-23 | Titulaire | Remettre rapport d'analyse de cause + plan d'action dans les 10 JO suivant la classification (sauf accord écrit différent) | §7.2 |
| GT-24 | AC | Peut réaliser jusqu'à 4 audits qualité programmés par année contractuelle avec préavis minimal de 10 JO | §7.3 |
| GT-25 | Titulaire | Fournir l'accès aux enregistrements qualité et répondre aux constats d'audit dans les 15 JO suivant réception du rapport d'audit | §7.3 |
| GT-26 | Titulaire | Remettre le Plan de Cybersécurité Programme au plus tard à M4 et le maintenir à jour jusqu'à l'acceptation de FNG-02 | §8.1 |
| GT-27 | Titulaire | Notifier toute vulnérabilité critique affectant une configuration destinée aux essais/livraison dans les 24 h suivant sa confirmation | §8.2 |
| GT-28 | Titulaire | Remettre la stratégie de remédiation dans les 5 JO suivant la confirmation de la vulnérabilité | §8.2 |
