# Lote 5 : jalons (Annexe D), conflits, ambiguities, QC
import duckdb
con = duckdb.connect('workspace/data/obligations.duckdb')

# --- Jalons contractuels (Annexe D, feuille Milestones) ---
MS = [
 ("KO","Revue de lancement programme","2026-10-20"),
 ("SRR","System Requirements Review","2027-04-15"),
 ("PDR","Preliminary Design Review","2028-02-15"),
 ("CDR","Critical Design Review","2029-06-20"),
 ("PSF1","Premiere tele / demarrage fabrication FNG-01","2030-01-15"),
 ("PSF2","Premiere tele / demarrage fabrication FNG-02","2030-10-15"),
 ("INT1","Debut integration a quai FNG-01","2032-03-10"),
 ("TRR1","Revue preparation essais mer FNG-01","2033-02-15"),
 ("STM1","Debut campagne essais mer FNG-01","2033-03-20"),
 ("ENDSTM1","Fin campagne essais mer FNG-01","2033-06-30"),
 ("A1","Acceptation contractuelle cible FNG-01","2033-09-30"),
 ("INT2","Debut integration a quai FNG-02","2032-11-15"),
 ("TRR2","Revue preparation essais mer FNG-02","2033-11-15"),
 ("STM2","Debut campagne essais mer FNG-02","2033-12-15"),
 ("ENDSTM2","Fin campagne essais mer FNG-02","2034-03-31"),
 ("A2","Acceptation contractuelle cible FNG-02","2034-06-30"),
 ("RETEX1","Revue retour d'experience FNG-01","2033-11-10"),
 ("CLOSE-SI1","Fin soutien initial FNG-01","2034-09-30"),
 ("CLOSE-SI2","Fin soutien initial FNG-02","2035-06-30"),
]
for mid, name, d in MS:
    kind = "CIBLE" if mid in ("A1","A2") else "CONTRACTUELLE"
    con.execute("INSERT OR REPLACE INTO milestones VALUES (?,?,?,?,?)",
                (mid, name, d, kind, "05-planning-contractuel"))
# Jalons de formation (Annexe D, feuille Formation) - sessions contractuelles §12.2
TR = [("F-01","Premiere session equipage FNG-01","2033-06-05"),("F-02","Premiere session maintenance FNG-01","2033-07-03"),
      ("F-03","Premiere session administrateur numerique FNG-01","2033-09-04"),
      ("F-04","Premiere session equipage FNG-02","2034-02-05"),("F-05","Premiere session maintenance FNG-02","2034-03-04"),
      ("F-06","Premiere session administrateur numerique FNG-02","2034-05-06")]
for mid, name, d in TR:
    con.execute("INSERT OR REPLACE INTO milestones VALUES (?,?,?,?,?)",
                (mid, name, d, "CONTRACTUELLE", "05-planning-contractuel"))
# Dates derivees GFE/GFI : INDICATIF (Annexe D, feuille GFE-GFI-Derived)
GV = [("GFI-01","DE + 30 jours calendaires","2026-10-31"),("GFI-02","M5","2027-02-28"),
      ("GFI-03","30 jours calendaires avant PDR","2028-01-16"),("GFI-04","60 jours calendaires avant CDR","2029-04-21"),
      ("GFE-01","M14","2027-11-30"),("GFE-02","90 jours calendaires avant INT1","2031-12-11"),
      ("GFE-03","90 jours calendaires avant INT2","2032-08-17"),
      ("GFI-05-FNG01","60 jours calendaires avant STM1","2033-01-19"),
      ("GFI-05-FNG02","60 jours calendaires avant STM2","2033-10-16")]
for mid, name, d in GV:
    con.execute("INSERT OR REPLACE INTO milestones VALUES (?,?,?,?,?)",
                (mid, name, d, "INDICATIF", "05-planning-contractuel"))

# --- Conflits ---
CON = [
 ("CONF-001",
  "Echeance du rapport mensuel d'avancement : le Contrat Principal §4.2 fixe le 10e JO apres la fin du mois contractuel, tandis que CDRL-005 (Annexe B) fixe le 7e JO apres la fin du mois contractuel.",
  "01-contrat-principal §4.2", "03-annexe-b-livrables-cdrl, CDRL-005",
  "Contrat Principal §2.1 : le Contrat Principal prevaut sur l'Annexe B",
  "Delai retenu : 10e JO apres la fin du mois contractuel (OBL-0010, statut EN_CONFLIT)",
  "TRANCHE_PAR_PRESEANCE"),
]
for c in CON:
    con.execute("INSERT OR REPLACE INTO conflicts VALUES (?,?,?,?,?,?,?)", c)

# --- Ambiguites ---
AM = [
 ("AMBIG-001",
  "Les jalons A1 et A2 sont des dates d'acceptation CIBLE (Annexe D, qualifiees 'Acceptation contractuelle cible'). La date effective d'acceptation depend du processus §10.4 (acceptation ou rejet sous 30 jours calendaires). Les periodes de soutien initial (12 mois) et de garantie (24 mois) sont ancrees sur l'acceptation effective, dont la date exacte est inconnue.",
  "05-planning-contractuel (Milestones A1/A2) ; 01-contrat-principal §10.4, §12.3, §13",
  "Lecture 1 : A1/A2 sont des cibles de planning et l'acceptation effective peut survenir a une date differente. Lecture 2 : A1/A2 sont les dates butoirs d'acceptation.",
  "OUVERT"),
 ("AMBIG-002",
  "Le corpus ne fournit aucun calendrier de jours feries. Les delais exprimes en jours ouvrables (JO) ne peuvent etre convertis en dates exactes ; seules les regles contractuelles sont conservees dans le registre.",
  "01-contrat-principal §1 ; 05-planning-contractuel (Hypotheses)",
  "Lecture unique : conserver la regle contractuelle en JO sans produire de date exacte.",
  "OUVERT"),
 ("AMBIG-003",
  "Le terme 'revue majeure' est utilise (Contrat §5.3 ; CDRL-003 ; CDRL-027) sans definition contractuelle : l'ensemble des revues concernees n'est pas explicitement liste.",
  "01-contrat-principal §5.3 ; 03-annexe-b-livrables-cdrl, CDRL-003/CDRL-027",
  "Lecture 1 : SRR, PDR, CDR (revues de conception). Lecture 2 : inclut egalement TRR-Mer et les revues d'acceptation.",
  "OUVERT"),
 ("AMBIG-004",
  "Le jalon KO de l'Annexe D ('Revue de lancement programme', 2026-10-20) et la 'Revue de Lancement Technique' de l'Annexe A §A2 (dans les 30 jours calendaires suivant la DE, soit avant le 31-10-2026) designent vraisemblablement le meme evenement, mais les libelles differe et aucun lien explicite n'est fait.",
  "05-planning-contractuel (KO) ; 02-annexe-a-specification-technique §A2",
  "Lecture 1 : meme revue (KO = Revue de Lancement). Lecture 2 : deux revues distinctes de lancement (programme vs technique).",
  "OUVERT"),
 ("AMBIG-005",
  "Le mecanisme de l'indication contraire approuvee n'est pas specifie : §10.1 'sauf indication contraire de l'Annexe B' et CDRL-014 'sauf indication contraire approuvee' renvoient a un processus de derogation non detaille dans le corpus.",
  "01-contrat-principal §10.1 ; 03-annexe-b-livrables-cdrl, CDRL-014",
  "Lecture unique : une derogation ecrite approuvee serait requise, mais le corpus ne precise ni l'organe ni la forme.",
  "OUVERT"),
]
for a in AM:
    con.execute("INSERT OR REPLACE INTO ambiguities VALUES (?,?,?,?,?)", a)

# --- Croisement jalons / obligations ---
con.execute("INSERT OR REPLACE INTO progress VALUES ('05-planning-contractuel','EXTRACTED', 'DONE', strftime(now(),'YYYY-MM-DD HH24:MI:SS'))")
con.execute("INSERT OR REPLACE INTO progress VALUES ('05-planning-contractuel','CROSSED', 'DONE', strftime(now(),'YYYY-MM-DD HH24:MI:SS'))")
for d in ['01-contrat-principal','02-annexe-a-specification-technique','03-annexe-b-livrables-cdrl','04-annexe-c-responsabilites']:
    con.execute("INSERT OR REPLACE INTO progress VALUES (?, 'CROSSED', 'DONE', strftime(now(),'YYYY-MM-DD HH24:MI:SS'))", (d,))

# --- QC ---
print('jalons :', con.execute('select count(*) from milestones').fetchone()[0])
print('obligations :', con.execute('select count(*) from obligations').fetchone()[0])
print('sans localisateur :', con.execute("select count(*) from obligations where source_locator is null or trim(source_locator)=''").fetchone()[0])
print('parties :', con.execute("select party, count(*) from obligations group by 1 order by 1").fetchall())
print('statuts :', con.execute("select status, count(*) from obligations group by 1").fetchall())
print('conflits :', con.execute('select count(*) from conflicts').fetchone()[0])
print('ambiguites :', con.execute('select count(*) from ambiguities').fetchone()[0])
con.close()
