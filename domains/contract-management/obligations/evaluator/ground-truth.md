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
| GT-29 | CONJOINTE | Aucune donnée contractuelle à diffusion restreinte transférée vers un système tiers non autorisé par écrit par l'AC | §8.3 |
| GT-30 | Titulaire | Remettre la liste initiale des fournisseurs critiques à M3 | §9.1 |
| GT-31 | Titulaire | Notifier tout changement de fournisseur critique au moins 20 JO avant la prise d'effet envisagée | §9.1 |
| GT-32 | Titulaire | À compter de M6, tenir un registre des obsolescences et le remettre trimestriellement avec le dossier COPIL | §9.2 |
| GT-33 | Titulaire | Notifier toute obsolescence susceptible d'affecter un jalon dans les 12 mois suivants dans les 5 JO suivant son identification | §9.2 |
| GT-34 | Titulaire | Remettre les procédures d'essai soumises à approbation au moins 45 jours calendaires avant le début prévu de l'essai | §10.1 |
| GT-35 | AC | Accepter ou commenter une procédure complète sous 20 jours calendaires ; absence de réponse = PAS réputée acceptée | §10.1 |
| GT-36 | Titulaire | Notifier la disponibilité d'un bâtiment pour la TRR au moins 30 jours calendaires avant la date souhaitée | §10.2 |
| GT-37 | Titulaire | Remettre le dossier provisoire de résultats d'essais dans les 10 JO suivant la fin de chaque campagne d'essais à la mer | §10.3 |
| GT-38 | Titulaire | Remettre le dossier consolidé dans les 30 jours calendaires suivant la fin de la campagne, après traitement des anomalies significatives ou identification explicite des anomalies ouvertes | §10.3 |
| GT-39 | AC | Prononcer l'acceptation ou notifier un refus motivé dans les 30 jours calendaires suivant réception d'un dossier d'acceptation complet ; Réserve Majeure empêche l'acceptation | §10.4 |
| GT-40 | Titulaire | Remettre le fichier source éditable pour tout document généré sous forme éditable lorsque l'Annexe B l'exige | §11.2 |
| GT-41 | Titulaire | Remettre la documentation « tel que construit » de chaque bâtiment au plus tard 60 jours calendaires après son acceptation | §11.3 |
| GT-42 | Titulaire | Remettre le Plan de Formation Initiale au plus tard à M18 | §12.1 |
| GT-43 | AC | Communiquer la liste nominative des stagiaires au plus tard 30 jours calendaires avant le début de chaque session | §12.1 |
| GT-44 | Titulaire | Réaliser les sessions de formation prévues à l'Annexe D ; supports définitifs au plus tard 10 JO avant le début de la première session | §12.2 |
| GT-45 | Titulaire | Assurer un soutien initial de 12 mois à compter de l'acceptation de chaque bâtiment | §12.3 |
| GT-46 | Titulaire | Période de garantie de 24 mois à compter de l'acceptation de chaque bâtiment | §13 |
| GT-47 | Titulaire | Accuser réception d'une notification de défaut sous garantie dans un délai maximal de 2 JO | §13 |
| GT-48 | Titulaire | Fournir dans les 5 JO une première analyse : actions conservatoires recommandées + plan d'investigation | §13 |
| GT-49 | Titulaire | Tenir un registre des éléments préexistants incorporés aux livrables ; version mise à jour à la CDR puis avec chaque dossier d'acceptation | §14 |
| GT-50 | Titulaire | Fournir les éléments justificatifs relatifs aux droits d'usage dans les 15 JO suivant la demande de l'AC | §14 |
| GT-51 | CONJOINTE | Notifier à l'autre partie, sans délai indu et au plus tard 24 h après confirmation, tout incident de sécurité susceptible d'affecter les informations contractuelles | §15 |
| GT-52 | Titulaire | S'assurer que les personnels ayant accès aux informations protégées disposent des habilitations/autorisations requises avant cet accès | §15 |
| GT-53 | Titulaire | Notifier tout événement dont l'impact prévisionnel excède 15 jours calendaires sur un Jalon Contractuel dans les 3 JO suivant sa caractérisation | §16 |
| GT-54 | Titulaire | Remettre un plan de rétablissement (causes, actions, responsables, dates cibles, impact résiduel) dans les 10 JO suivant cette notification | §16 |
| GT-55 | Titulaire | Accompagner les demandes de paiement liées à un jalon des preuves de franchissement définies à l'Annexe B | §17 |
| GT-56 | AC | Notifier toute contestation motivée d'une demande de paiement dans les 15 JO suivant réception du dossier complet | §17 |
## B. Annexe A — Spécification technique

| ID | Partie | Obligation | Source |
|----|--------|------------|--------|
| GT-57 | Titulaire | Concevoir une architecture navire intégrée (plateforme/énergie, navigation, réseaux de données, communications, infrastructure informatique de mission, interfaces AC, diagnostic/soutien) | A1 |
| GT-58 | Titulaire | Permettre la traçabilité entre exigences de niveau système, éléments de conception, interfaces et moyens de vérification | A1 |
| GT-59 | Titulaire | Remettre la matrice de traçabilité : initiale à la PDR, consolidée à la CDR, « as-built » avec le dossier d'acceptation de chaque bâtiment | A1 |
| GT-60 | Titulaire | Organiser la Revue de Lancement Technique dans les 30 jours calendaires suivant la DE | A2 |
| GT-61 | Titulaire | Transmettre au moins 10 JO avant la revue : organisation d'ingénierie, stratégie de gestion des exigences, stratégie de gestion des interfaces, proposition de référentiel de criticité cyber, liste initiale des hypothèses de conception | A2 |
| GT-62 | AC | Confirmer ou commenter le référentiel de criticité cyber dans les 10 JO suivant la revue | A2 |
| GT-63 | Titulaire | Maintenir la base des exigences contractuelles et dérivées pendant toute la durée de l'ingénierie | A3 |
| GT-64 | Titulaire | Soumettre à l'AC toute exigence dérivée susceptible d'imposer une contrainte nouvelle à une fourniture de l'AC avant son incorporation à la baseline | A3 |
| GT-65 | Titulaire | Fournir un export lisible de la base d'exigences à chaque SRR, PDR et CDR | A3 |
| GT-66 | Titulaire | Tenir un registre des interfaces | A4 |
| GT-67 | Titulaire | Soumettre les ICD de niveau système : préliminaire à la PDR, approuvable à la CDR, « as-built » avec le dossier d'acceptation de chaque bâtiment | A4 |
| GT-68 | AC | Remettre les données d'interface des équipements GFE listés à l'Annexe C au plus tard aux jalons de l'Annexe D | A4 |
| GT-69 | Titulaire | Identifier les hypothèses temporaires utilisées sur une donnée GFE incomplète et les soumettre à l'AC dans les 5 JO suivant leur formalisation | A4 |
| GT-70 | Titulaire | Remettre mensuellement un bilan masse et centre de gravité de M6 à la CDR | A5 |
| GT-71 | Titulaire | Remettre le bilan masse trimestriellement avec le rapport d'avancement de la CDR à l'acceptation de FNG-02 | A5 |
| GT-72 | Titulaire | Signaler toute consommation > 50 % de la marge de masse d'un sous-ensemble critique dans le rapport suivant + action de maîtrise identifiée | A5 |
| GT-73 | Titulaire | Remettre le bilan de puissance électrique : préliminaire à la PDR, consolidé à la CDR, mis à jour avant la première mise sous tension intégrée de chaque bâtiment, « as-built » avec chaque dossier d'acceptation | A6 |
| GT-74 | Titulaire | Maintenir la liste de configuration logicielle des éléments dont il a la responsabilité | A7 |
| GT-75 | Titulaire | Fournir au moins 15 jours calendaires avant le début d'une campagne d'essais à la mer la déclaration de version (identifiant, fonctions modifiées, anomalies connues, statut des non-régressions, dépendances) | A7 |
| GT-76 | Titulaire | Notifier toute modification de version après déclaration avant embarquement de la version modifiée dans la configuration d'essai | A7 |
| GT-77 | Titulaire | Réaliser une analyse de risques cyber initiale avant la PDR ; la mettre à jour avant la CDR, avant la première campagne d'essais à la mer de chaque bâtiment et avant chaque acceptation | A8 |
| GT-78 | Titulaire | Inscrire les écarts cyber ouverts au moment d'une revue dans un registre avec responsable, traitement prévu et date cible | A8 |
| GT-79 | CONJOINTE | Aucun écart cyber classé critique selon le référentiel approuvé ne peut rester ouvert à l'acceptation, sauf dérogation écrite de l'AC | A8 |
| GT-80 | Titulaire | Préparer un dossier de readiness pour chaque séquence majeure d'essais à quai | A9 |
| GT-81 | Titulaire | Remettre le dossier de readiness 15 JO avant la revue de préparation correspondante (contenu minimal : configuration testée, prérequis, procédures, moyens, anomalies ouvertes, analyse de sécurité, critères de démarrage) | A9 |
| GT-82 | AC | Communiquer ses observations sur le dossier de readiness au plus tard 5 JO avant la revue, lorsque le dossier a été reçu dans les délais | A9 |
| GT-83 | Titulaire | Fournir une configuration de référence gelée au plus tard 10 jours calendaires avant le départ prévu de chaque campagne d'essais à la mer | A10 |
| GT-84 | Titulaire | Consigner les écarts à la configuration de référence dans le journal de configuration de campagne | A10 |
| GT-85 | Titulaire | Fournir à l'AC un accès aux données d'essais contractuellement requises au plus tard 2 JO après leur acquisition (sauf délai supplémentaire justifié par un traitement technique nécessaire) | A10 |
| GT-86 | Titulaire | Produire pour chaque bâtiment : arborescence logistique, nomenclature de soutien, plans de maintenance, catalogue illustré des pièces, documentation de diagnostic, liste des rechanges initiaux | A11 |
| GT-87 | Titulaire | Remettre une version préliminaire du jeu documentaire de soutien 6 mois avant l'acceptation prévue de FNG-01 | A11 |
| GT-88 | Titulaire | Pour FNG-02 : version préliminaire 4 mois avant son acceptation prévue, intégrant le retour d'expérience validé de FNG-01 disponible à cette date | A11 |
| GT-89 | Titulaire | Pendant le soutien initial (12 mois) : point de contact technique les jours ouvrés, enregistrement des demandes, accusé de réception sous 1 JO, premier diagnostic ou demande d'information complémentaire sous 3 JO | A12 |
| GT-90 | Titulaire | Remettre un rapport mensuel de soutien au plus tard le 5e JO du mois suivant | A12 |
| GT-91 | Titulaire | Préparer un cursus équipage, un cursus maintenance et un cursus administrateur des systèmes numériques | A13 |
| GT-92 | Titulaire | Soumettre les supports de formation en version projet 60 jours calendaires avant la première session correspondante | A13 |
| GT-93 | AC | Remettre ses observations sur les supports de formation dans les 20 jours calendaires suivant réception | A13 |
| GT-94 | Titulaire | Maintenir un registre unique des anomalies issues des essais sous sa responsabilité | A14 |
| GT-95 | Titulaire | Remettre une synthèse des anomalies ouvertes, ventilée par criticité, avec chaque rapport mensuel à compter du début des essais d'intégration à quai | A14 |
| GT-96 | Titulaire | Notifier à l'AC toute anomalie empêchant la poursuite d'une séquence d'essais le jour même de sa classification | A14 |
| GT-97 | Titulaire | Organiser une revue de retour d'expérience dans les 45 jours calendaires suivant l'acceptation de FNG-01 | A15 |
| GT-98 | Titulaire | Remettre le dossier de revue RETEX 10 JO avant la réunion | A15 |
| GT-99 | Titulaire | Remettre le plan d'intégration du retour d'expérience sur FNG-02 dans les 20 JO suivant la revue | A15 |

## C. Annexe B — Livrables contractuels

| ID | Partie | Obligation | Source |
|----|--------|------------|--------|
| GT-100 | Règle (B1) | Un livrable n'est réputé « soumis pour revue » que si index + annexes obligatoires + fichiers sources sont présents dans l'espace documentaire de l'AC | B1 |
| GT-101 | AC | Notifier un rejet purement administratif dans les 3 JO suivant la soumission ; le délai de revue ne court pas | B2 |
| GT-102 | Titulaire | Remettre une version corrigée sous 10 JO après commentaires de l'AC (sauf mention contraire de la feuille de commentaires) | B3 |
| GT-103 | Titulaire | Remettre le Plan de Management Programme à M2 (PDF + source éditable) ; revue AC 15 JO | CDRL-001 |
| GT-104 | Titulaire | Remettre le dossier d'acceptation FNG-01 au jalon A1 (30 jours calendaires) ; revue AC 15 JO | CDRL-018 |
| GT-105 | Titulaire | Remettre le dossier d'acceptation FNG-02 au jalon A2 (30 jours calendaires) ; revue AC 15 JO | CDRL-019 |
## D. Annexe C — Matrice des responsabilités

| ID | Partie | Obligation | Source |
|----|--------|------------|--------|
| GT-106 | AC | Fournir GFI-01 « Référentiel d'emploi et scénarios de vérification contractuels » à DE + 30 jours calendaires | Annexe C ! GFE-GFI ! GFI-01 |
| GT-107 | AC | Fournir GFI-02 « Données d'interface initiales lot Alpha » à M5 | Annexe C ! GFE-GFI ! GFI-02 |
| GT-108 | AC | Fournir GFI-03 « Données d'interface consolidées lot Alpha » à 30 jours calendaires avant PDR | Annexe C ! GFE-GFI ! GFI-03 |
| GT-109 | AC | Fournir GFI-04 « Données d'interface consolidées lot Beta » à 60 jours calendaires avant CDR | Annexe C ! GFE-GFI ! GFI-04 |
| GT-110 | AC | Fournir GFE-01 « Équipement d'intégration laboratoire — lot Alpha » à M14 | Annexe C ! GFE-GFI ! GFE-01 |
| GT-111 | AC | Fournir GFE-02 « Équipement d'intégration plateforme — lot Alpha » à 90 jours calendaires avant le début des essais à quai de FNG-01 | Annexe C ! GFE-GFI ! GFE-02 |
| GT-112 | AC | Fournir GFE-03 « Équipement d'intégration plateforme — lot Beta » à 90 jours calendaires avant le début des essais à quai de FNG-02 | Annexe C ! GFE-GFI ! GFE-03 |
| GT-113 | AC | Fournir GFI-05-FNG01 « Jeu de données d'acceptation FNG-01 » à 60 jours calendaires avant la campagne d'essais à la mer de FNG-01 | Annexe C ! GFE-GFI ! GFI-05 FNG-01 |
| GT-114 | AC | Fournir GFI-05-FNG02 « Jeu de données d'acceptation FNG-02 » à 60 jours calendaires avant la campagne d'essais à la mer de FNG-02 | Annexe C ! GFE-GFI ! GFI-05 FNG-02 |
| GT-115 | Titulaire | Recevoir, inventorier et assurer la traçabilité des GFE | Annexe C ! Titulaire GFE ! C3-01 |
| GT-116 | Titulaire | Notifier toute non-conformité apparente dans les 5 JO suivant la réception | Annexe C ! Titulaire GFE ! C3-02 |
| GT-117 | Titulaire | Renvoyer ou réaffecter les GFE selon instruction écrite de l'AC | Annexe C ! Titulaire GFE ! C3-03 |
| GT-118 | Titulaire | Maintenir l'historique d'intégration des GFE dans le registre de configuration | Annexe C ! Titulaire GFE ! C3-04 |
| GT-119 | Titulaire | Remettre le dossier de revue SRR 15 JO avant la revue | Annexe C ! Joint Reviews ! SRR |
| GT-120 | AC | Remettre ses commentaires consolidés SRR 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! SRR |
| GT-121 | Titulaire | Remettre le dossier de revue PDR 15 JO avant la revue | Annexe C ! Joint Reviews ! PDR |
| GT-122 | AC | Remettre ses commentaires consolidés PDR 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! PDR |
| GT-123 | Titulaire | Remettre le dossier de revue CDR 15 JO avant la revue | Annexe C ! Joint Reviews ! CDR |
| GT-124 | AC | Remettre ses commentaires consolidés CDR 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! CDR |
| GT-125 | Titulaire | Remettre le dossier de revue TRR-Mer 10 JO avant la revue | Annexe C ! Joint Reviews ! TRR-Mer |
| GT-126 | AC | Remettre ses commentaires consolidés TRR-Mer 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! TRR-Mer |
| GT-127 | Titulaire | Remettre le dossier de revue A1 10 JO avant la revue | Annexe C ! Joint Reviews ! A1 |
| GT-128 | AC | Remettre ses commentaires consolidés A1 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! A1 |
| GT-129 | Titulaire | Remettre le dossier de revue A2 10 JO avant la revue | Annexe C ! Joint Reviews ! A2 |
| GT-130 | AC | Remettre ses commentaires consolidés A2 3 JO avant la revue si le dossier a été reçu à temps | Annexe C ! Joint Reviews ! A2 |
| GT-131 | CONJOINTE | Consigner les décisions de revue dans un compte-rendu signé par les deux parties dans les 10 JO suivant la revue | Annexe C ! Review Minutes ! C4-PV |
| GT-132 | Titulaire | Soumettre la liste des personnels devant accéder au site 20 JO avant l'activité concernée | Annexe C ! Site Access ! C5-01 |
| GT-133 | AC | Confirmer l'accès ou notifier un dossier incomplet dans les 10 JO suivant réception de la liste | Annexe C ! Site Access ! C5-02 |
| GT-134 | Titulaire | Soumettre la définition des jeux de données spécifiques demandés 45 jours calendaires avant la date demandée | Annexe C ! Test Data ! C6-01 |
| GT-135 | AC | Fournir les jeux de données spécifiques demandés 15 jours calendaires avant l'essai concerné, si la définition a été soumise à temps | Annexe C ! Test Data ! C6-02 |

## E. Annexe D — Planning contractuel

L'Annexe D ne crée pas d'obligation nouvelle : elle fixe les dates des Jalons
Contractuels, les dates des sessions de formation (F-01 à F-06) et des rappels
indicatifs des dates GFE/GFI. Règles de la feuille Assumptions à consigner :
- le planning est la baseline contractuelle initiale ;
- les rappels GFE/GFI sont donnés à titre de commodité : **les règles de l'Annexe C
  prévalent** en cas de contradiction ;
- le planning ne contient pas de calendrier de jours fériés : les calculs en JO à
  partir d'un événement futur sont **indicatifs**.

Jalons (dates du corpus, à citer telles quelles) :
KO 2026-10-20, SRR 2027-04-15, PDR 2028-02-15, CDR 2029-06-20, PSF1 2030-01-15,
PSF2 2030-10-15, INT1 2032-03-10, TRR1 2033-02-15, STM1 2033-03-20, ENDSTM1 2033-06-30,
A1 2033-09-30 (**cible**), INT2 2032-11-15, TRR2 2033-11-15, STM2 2033-12-15,
ENDSTM2 2034-03-31, A2 2034-06-30 (**cible**), RETEX1 2033-11-10,
CLOSE-SI1 2034-09-30, CLOSE-SI2 2035-06-30.

Sessions de formation (Annexe D ! Training) : F-01 2033-06-05, F-02 2033-07-03,
F-03 2033-09-04, F-04 2034-02-05, F-05 2034-03-04, F-06 2034-05-06.

Rappels GFE/GFI (Annexe D ! GFE-GFI Derived, indicatifs) : GFI-01 2026-10-31,
GFI-02 2027-02-28, GFI-03 2028-01-16, GFI-04 2029-04-21, GFE-01 2027-11-30,
GFE-02 2031-12-11, GFE-03 2032-08-17, GFI-05-FNG01 2033-01-19, GFI-05-FNG02 2033-10-16.
## F. Conflits documentaires attendus

| ID | Conflit | Sources | Résultat attendu |
|----|---------|---------|------------------|
| CT-1 | Délai du rapport mensuel d'avancement : « 10e JO suivant la fin du mois contractuel » (§4.2) vs « 7e JO après fin du mois contractuel » (CDRL-005) | 01-contrat §4.2 vs 03-annexe-b CDRL-005 | Contradiction explicite. Préséance §2.1/§2.2 : le contrat principal prévaut → **10e JO**. Le conflit doit être consigné même tranché. |
| CT-2 | A1/A2 sont des dates d'acceptation **cible** (Annexe D, « Acceptation contractuelle cible ») alors que les obligations (CDRL-018/019, §10.4, §11.3, §13, A11, A12, A15) sont déclenchées par l'**acceptation effective** | 05-planning Milestones vs 03-annexe-b CDRL-018/019 et 01-contrat | Pas de contradiction textuelle (le planning est indicatif pour A1/A2). L'agent doit conserver le déclencheur contractuel (acceptation) et ne pas substituer la date cible à l'événement effectif. |
| CT-3 | Dossier readiness : « 15 JO avant la revue » pour les essais à quai (A9, CDRL-013) vs « dossier de revue TRR-Mer 10 JO avant » (Annexe C ! Joint Reviews) | 02-annexe-a A9 vs 04-annexe-c Joint Reviews | Objets probablement distincts (essais à quai vs TRR mer) ; tension à signaler comme ambiguïté si l'agent les met en regard. |
| CT-4 | Rappels de dates GFE/GFI (Annexe D ! GFE-GFI Derived) vs règles de l'Annexe C | 05-planning vs 04-annexe-c | L'Annexe D le dit elle-même : les rappels sont de commodité, **les règles de l'Annexe C prévalent**. Vérifier la cohérence (les dates dérivées sont cohérentes avec les règles). |

## G. Ambiguïtés et informations manquantes attendues

| ID | Point | Détail attendu |
|----|-------|----------------|
| AM-1 | « Remis pour revue » (B1) | Critères de complétude : index + annexes obligatoires + fichiers sources. Le délai de revue ne court qu'après soumission administrativement valide (B2). |
| AM-2 | Pièges d'acceptation tacite opposés | Compte rendu COPIL : silence 5 JO = **réputé accepté** (§4.1). Procédure d'essai : silence 20 jours calendaires = **pas** réputée acceptée (§10.1). Les deux doivent être captés correctement. |
| AM-3 | « Acceptation prévue » (CDRL-020/021, A11) | Cible ou effective ? Conserver la formulation contractuelle ; relier à A1/A2 cibles sans les assimiler. |
| AM-4 | GFE-02/GFE-03 « avant le début des essais à quai » (Annexe C) | Le planning mappe sur INT1/INT2 (« début intégration à quai ») — hypothèse de mapping à expliciter. |
| AM-5 | Déclencheur §3.2 | « Date à laquelle il dispose d'éléments suffisants pour caractériser l'impact » — déclencheur factuel, non calendaire. |
| AM-6 | Observations AC sur dossier readiness (A9) | Conditionnées : « lorsque le dossier a été reçu dans les délais ». |
| AM-7 | Dossier consolidé essais mer (§10.3) | Condition alternative : traitement des anomalies significatives **ou** identification explicite des anomalies ouvertes. |
| AM-8 | Jours fériés | Aucun calendrier annexé au contrat (§1) : les délais en JO à partir d'un événement futur ne peuvent pas être convertis en dates exactes ; conserver la règle contractuelle. |
| AM-9 | Revue mensuelle (§4.2) | « Une revue d'avancement est organisée chaque mois contractuel » — l'organisateur n'est pas explicitement désigné ; le rapport mensuel (Titulaire) est l'obligation actionnable. |

## H. Table de dédoublonnage (CDRL ↔ obligations de référence)

| CDRL | GT couverte | CDRL | GT couverte |
|------|-------------|------|-------------|
| CDRL-001 | GT-103 | CDRL-016 | GT-37 |
| CDRL-002 | GT-21 | CDRL-017 | GT-38 |
| CDRL-003 | GT-26 | CDRL-018 | GT-104 |
| CDRL-004 | GT-30 | CDRL-019 | GT-105 |
| CDRL-005 | GT-09 (+ CT-1) | CDRL-020 | GT-87 |
| CDRL-006 | GT-10 | CDRL-021 | GT-88 |
| CDRL-007 | GT-32 | CDRL-022 | GT-41 |
| CDRL-008 | GT-59 | CDRL-023 | GT-42 |
| CDRL-009 | GT-67 | CDRL-024 | GT-92 |
| CDRL-010 | GT-70/71/72 | CDRL-025 | GT-44 |
| CDRL-011 | GT-73 | CDRL-026 | GT-49 |
| CDRL-012 | GT-77 | CDRL-027 | GT-15 |
| CDRL-013 | GT-81 | CDRL-028 | GT-90 |
| CDRL-014 | GT-34 | CDRL-029 | GT-98 |
| CDRL-015 | GT-83 | CDRL-030 | GT-99 |

Un registre qui liste à la fois l'obligation du contrat et le CDRL correspondant
sans les lier est pénalisé (doublon) ; un registre qui les fusionne en une ligne
avec les deux sources est conforme.
