# Lote 3 : Annexe B - Livrables CDRL (03-annexe-b-livrables-cdrl)
import duckdb
D = '03-annexe-b-livrables-cdrl'
# Nouvelles obligations (CDRL sans homologue dans Contrat/Annexe A)
R = [
("OBL-0102","TITULAIRE","Transmettre le Plan de Management Programme","livrable","Date d'Effet (DE)","Au M2","Plan de Management Programme (CDRL-001)","Feuille CDRL, ligne CDRL-001","HAUTE","EXTRAITE","Revue AC : 15 JO"),
("OBL-0103","TITULAIRE","Transmettre les livrables dans l'espace documentaire contractuel designe par l'AC, avec index, annexes obligatoires et fichiers sources requis (condition pour qu'un livrable soit considere comme soumis pour revue)","gouvernance","Chaque soumission de livrable","A chaque soumission","Soumission complete dans l'espace designe","Feuille Regles de transmission, B1","HAUTE","EXTRAITE",None),
("OBL-0104","AC","Notifier tout rejet purement administratif d'un dossier manifestement incomplet","gouvernance","Soumission d'un livrable","3 JO apres la soumission (le delai de revue ne court pas)","Notification de rejet administratif","Feuille Regles de transmission, B2","HAUTE","EXTRAITE",None),
("OBL-0105","TITULAIRE","Transmettre une version corrigee d'un livrable apres commentaires de l'AC","livrable","Commentaires AC requerant une nouvelle version","10 JO (sauf date differente convenue dans la fiche de commentaires)","Version corrigee","Feuille Regles de transmission, B3","HAUTE","EXTRAITE",None),
("OBL-0106","TITULAIRE","Transmettre le dossier d'acceptation de FNG-01 avec index des preuves","livrable","Jalon A1 (acceptation cible FNG-01)","Au jalon A1","Dossier d'acceptation FNG-01 (CDRL-018)","Feuille CDRL, ligne CDRL-018","HAUTE","EXTRAITE","A1 est une date cible (AMBIG-001) ; le declencheur reel est le processus d'acceptation §10.4"),
("OBL-0107","TITULAIRE","Transmettre le dossier d'acceptation de FNG-02 avec index des preuves","livrable","Jalon A2 (acceptation cible FNG-02)","Au jalon A2","Dossier d'acceptation FNG-02 (CDRL-019)","Feuille CDRL, ligne CDRL-019","HAUTE","EXTRAITE","A2 est une date cible (AMBIG-001)"),
]
# CDRL deja couvertes par une obligation existante : ajout de la source Annexe B
MERGES = {
 "OBL-0010": "CDRL-005", "OBL-0011": "CDRL-006", "OBL-0016": "CDRL-027",
 "OBL-0022": "CDRL-002", "OBL-0026": "CDRL-003", "OBL-0031": "CDRL-004",
 "OBL-0033": "CDRL-007", "OBL-0035": "CDRL-014", "OBL-0038": "CDRL-016",
 "OBL-0039": "CDRL-017", "OBL-0043": "CDRL-022", "OBL-0044": "CDRL-023",
 "OBL-0047": "CDRL-025", "OBL-0052": "CDRL-026", "OBL-0061": "CDRL-008",
 "OBL-0069": "CDRL-009", "OBL-0072": "CDRL-010", "OBL-0074": "CDRL-011",
 "OBL-0078": "CDRL-012", "OBL-0081": "CDRL-013", "OBL-0083": "CDRL-015",
 "OBL-0087": "CDRL-020", "OBL-0088": "CDRL-021", "OBL-0092": "CDRL-028",
 "OBL-0094": "CDRL-024", "OBL-0100": "CDRL-029", "OBL-0101": "CDRL-030",
}
con = duckdb.connect('workspace/data/obligations.duckdb')
for r in R:
    con.execute("INSERT OR REPLACE INTO obligations VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                (r[0], r[1], r[2], r[3], r[4], r[5], r[6], D, r[7], r[8], r[9], r[10]))
for oid, cdrl in MERGES.items():
    con.execute("UPDATE obligations SET source_doc = source_doc || ' + 03-annexe-b-livrables-cdrl', "
                "source_locator = source_locator || ' + ' || ? WHERE id = ?", (cdrl, oid))
con.execute("INSERT OR REPLACE INTO progress VALUES ('03-annexe-b-livrables-cdrl','EXTRACTED', 'DONE', strftime(now(),'YYYY-MM-DD HH24:MI:SS'))")
print('lote 03 :', len(R), 'nouvelles +', len(MERGES), 'sources mergees')
print('total obligations :', con.execute('select count(*) from obligations').fetchone()[0])
con.close()
