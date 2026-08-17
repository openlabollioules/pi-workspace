# Lote 4 : Annexe C - Responsabilites (04-annexe-c-responsabilites)
import duckdb
D = '04-annexe-c-responsabilites'
def F(s): return 'Feuille ' + s
R = [
# GFE-GFI (AC)
("OBL-0108","AC","Fournir le referentiel d'emploi et les scenarios contractuels de verification (GFI-01)","fourniture-ac","Date d'Effet (DE)","DE + 30 jours calendaires","GFI-01","GFE-GFI, ligne GFI-01","HAUTE","EXTRAITE","Date indicative Annexe D : 2026-10-31"),
("OBL-0109","AC","Fournir les donnees d'interface initiales des equipements GFE lot Alpha (GFI-02)","fourniture-ac","Mois contractuel M5","Au M5","GFI-02","GFE-GFI, ligne GFI-02","HAUTE","EXTRAITE","Date indicative Annexe D : 2027-02-28"),
("OBL-0110","AC","Fournir les donnees d'interface consolidees des equipements GFE lot Alpha (GFI-03)","fourniture-ac","Jalon PDR","30 jours calendaires avant la PDR","GFI-03","GFE-GFI, ligne GFI-03","HAUTE","EXTRAITE","Date indicative Annexe D : 2028-01-16"),
("OBL-0111","AC","Fournir les donnees d'interface consolidees des equipements GFE lot Beta (GFI-04)","fourniture-ac","Jalon CDR","60 jours calendaires avant la CDR","GFI-04","GFE-GFI, ligne GFI-04","HAUTE","EXTRAITE","Date indicative Annexe D : 2029-04-21"),
("OBL-0112","AC","Fournir l'equipement GFE d'integration laboratoire lot Alpha (GFE-01)","fourniture-ac","Mois contractuel M14","Au M14","GFE-01","GFE-GFI, ligne GFE-01","HAUTE","EXTRAITE","Date indicative Annexe D : 2027-11-30"),
("OBL-0113","AC","Fournir l'equipement GFE d'integration plateforme lot Alpha (GFE-02)","fourniture-ac","Jalon INT1 (debut essais a quai FNG-01)","90 jours calendaires avant le debut des essais a quai FNG-01","GFE-02","GFE-GFI, ligne GFE-02","HAUTE","EXTRAITE","Date indicative Annexe D : 2031-12-11"),
("OBL-0114","AC","Fournir l'equipement GFE d'integration plateforme lot Beta (GFE-03)","fourniture-ac","Jalon INT2 (debut essais a quai FNG-02)","90 jours calendaires avant le debut des essais a quai FNG-02","GFE-03","GFE-GFI, ligne GFE-03","HAUTE","EXTRAITE","Date indicative Annexe D : 2032-08-17"),
("OBL-0115","AC","Fournir les jeux de donnees d'acceptation FNG-01 (GFI-05-FNG01)","fourniture-ac","Campagne d'essais a la mer FNG-01 (STM1)","60 jours calendaires avant la campagne d'essais a la mer FNG-01","GFI-05-FNG01","GFE-GFI, ligne GFI-05-FNG01","HAUTE","EXTRAITE","Date indicative Annexe D : 2033-01-19"),
("OBL-0116","AC","Fournir les jeux de donnees d'acceptation FNG-02 (GFI-05-FNG02)","fourniture-ac","Campagne d'essais a la mer FNG-02 (STM2)","60 jours calendaires avant la campagne d'essais a la mer FNG-02","GFI-05-FNG02","GFE-GFI, ligne GFI-05-FNG02","HAUTE","EXTRAITE","Date indicative Annexe D : 2033-10-16"),
# GFE du Titulaire
("OBL-0117","TITULAIRE","Fournir l'environnement d'integration logiciel (C3-01)","fourniture-ac","Jalon CDR","Au jalon CDR","Environnement d'integration logiciel","Titulaire-GFE, ligne C3-01","HAUTE","EXTRAITE",None),
("OBL-0118","TITULAIRE","Fournir les bancs d'essai a quai (C3-02)","fourniture-ac","Jalon INT1","Au jalon INT1 (debut integration a quai FNG-01)","Bancs d'essai a quai","Titulaire-GFE, ligne C3-02","HAUTE","EXTRAITE",None),
("OBL-0119","TITULAIRE","Fournir les outillages d'integration (C3-03)","fourniture-ac","Jalon PSF1","Au jalon PSF1 (premiere tele FNG-01)","Outillages d'integration","Titulaire-GFE, ligne C3-03","HAUTE","EXTRAITE",None),
("OBL-0120","TITULAIRE","Fournir les supports de diagnostic embarque (C3-04)","fourniture-ac","Jalon INT1","Au jalon INT1 (debut integration a quai FNG-01)","Supports de diagnostic embarque","Titulaire-GFE, ligne C3-04","HAUTE","EXTRAITE",None),
# Revues conjointes
("OBL-0121","TITULAIRE","Transmettre le dossier de revue pour la SRR","revue","Jalon SRR","15 JO avant la revue","Dossier de revue SRR","Revues-Conjointes, ligne SRR","HAUTE","EXTRAITE",None),
("OBL-0122","AC","Transmettre les commentaires consolides pour la SRR","revue","Dossier de revue SRR recu dans les delais","3 JO avant la revue","Commentaires consolides SRR","Revues-Conjointes, ligne SRR","HAUTE","EXTRAITE",None),
("OBL-0123","TITULAIRE","Transmettre le dossier de revue pour la PDR","revue","Jalon PDR","15 JO avant la revue","Dossier de revue PDR","Revues-Conjointes, ligne PDR","HAUTE","EXTRAITE",None),
("OBL-0124","AC","Transmettre les commentaires consolides pour la PDR","revue","Dossier de revue PDR recu dans les delais","3 JO avant la revue","Commentaires consolides PDR","Revues-Conjointes, ligne PDR","HAUTE","EXTRAITE",None),
("OBL-0125","TITULAIRE","Transmettre le dossier de revue pour la CDR","revue","Jalon CDR","15 JO avant la revue","Dossier de revue CDR","Revues-Conjointes, ligne CDR","HAUTE","EXTRAITE",None),
("OBL-0126","AC","Transmettre les commentaires consolides pour la CDR","revue","Dossier de revue CDR recu dans les delais","3 JO avant la revue","Commentaires consolides CDR","Revues-Conjointes, ligne CDR","HAUTE","EXTRAITE",None),
("OBL-0127","TITULAIRE","Transmettre le dossier de revue pour la TRR-Mer","revue","Jalons TRR1 / TRR2","10 JO avant la revue","Dossier de revue TRR-Mer","Revues-Conjointes, ligne TRR-Mer","HAUTE","EXTRAITE",None),
("OBL-0128","AC","Transmettre les commentaires consolides pour la TRR-Mer","revue","Dossier de revue TRR-Mer recu dans les delais","3 JO avant la revue","Commentaires consolides TRR-Mer","Revues-Conjointes, ligne TRR-Mer","HAUTE","EXTRAITE",None),
("OBL-0129","TITULAIRE","Transmettre le dossier de revue pour l'acceptation A1 (FNG-01)","revue","Jalon A1","10 JO avant la revue","Dossier de revue A1","Revues-Conjointes, ligne A1","HAUTE","EXTRAITE",None),
("OBL-0130","AC","Transmettre les commentaires consolides pour l'acceptation A1","revue","Dossier de revue A1 recu dans les delais","3 JO avant la revue","Commentaires consolides A1","Revues-Conjointes, ligne A1","HAUTE","EXTRAITE",None),
("OBL-0131","TITULAIRE","Transmettre le dossier de revue pour l'acceptation A2 (FNG-02)","revue","Jalon A2","10 JO avant la revue","Dossier de revue A2","Revues-Conjointes, ligne A2","HAUTE","EXTRAITE",None),
("OBL-0132","AC","Transmettre les commentaires consolides pour l'acceptation A2","revue","Dossier de revue A2 recu dans les delais","3 JO avant la revue","Commentaires consolides A2","Revues-Conjointes, ligne A2","HAUTE","EXTRAITE",None),
# Comptes rendus
("OBL-0133","CONJOINTE","Etablir le compte rendu de revue signe (par les deux parties)","gouvernance","Fin de chaque revue","10 JO apres la revue","Compte rendu de revue signe","Compte-Rendus, ligne C4-PV","HAUTE","EXTRAITE",None),
# Acces site
("OBL-0134","TITULAIRE","Transmettre la liste nominative du personnel pour toute activite sur site","gouvernance","Toute activite sur site","20 JO avant l'activite","Liste nominative du personnel","Acces-Site, ligne C5-01","HAUTE","EXTRAITE",None),
("OBL-0135","AC","Confirmer les acces du personnel","gouvernance","Reception de la liste nominative","10 JO apres reception","Confirmation des acces","Acces-Site, ligne C5-02","HAUTE","EXTRAITE",None),
# Donnees d'essai
("OBL-0136","TITULAIRE","Definir les besoins en donnees d'essai","essai","Chaque essai contractuel","45 jours calendaires avant la disponibilite desiree","Besoins en donnees d'essai","Donnees-Essai, ligne C6-01","HAUTE","EXTRAITE",None),
("OBL-0137","AC","Fournir le jeu de donnees d'essai defini","essai","Besoins en donnees d'essai defines","15 jours calendaires avant l'essai","Jeu de donnees d'essai","Donnees-Essai, ligne C6-02","HAUTE","EXTRAITE",None),
]
con = duckdb.connect('workspace/data/obligations.duckdb')
for r in R:
    con.execute("INSERT OR REPLACE INTO obligations VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (r[0], r[1], r[2], r[3], r[4], r[5], r[6], D, r[7], r[8], r[9], r[10]))
con.execute("INSERT OR REPLACE INTO progress VALUES ('04-annexe-c-responsabilites','EXTRACTED', 'DONE', strftime(now(),'YYYY-MM-DD HH24:MI:SS'))")
print('lote 04 inserte :', len(R), 'obligations')
print('total obligations :', con.execute('select count(*) from obligations').fetchone()[0])
con.close()
