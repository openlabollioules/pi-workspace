# Fragments : conflits + ambiguites, et resume executif
import duckdb
con = duckdb.connect('workspace/data/obligations.duckdb')
def q(sql, *a): return con.execute(sql, a).fetchall()

# --- conflits et ambiguites ---
p = ["# Conflits et ambiguïtés", "",
 "Méthode : conflit = deux sources contractuelles incompatibles ; tranché par l'ordre de préséance §2.1 (Contrat Principal > Annexe A > B > C > D) quand la préséance le permet, sinon soumis à validation humaine. Ambiguïté = plusieurs lectures raisonnables ou information manquante ; jamais tranchée sans validation.",
 "", "## Conflits détectés", ""]
for c in q("select id, description, source_a, source_b, precedence_applied, resolution, status from conflicts order by id"):
    p += [f"### {c[0]} — {c[6]}", "",
          f"- **Conflit** : {c[1]}",
          f"- **Sources** : `{c[2]}` vs `{c[3]}`",
          f"- **Préséance appliquée** : {c[4]}",
          f"- **Résolution** : {c[5]}", ""]
p += ["## Ambiguïtés ouvertes (à validation humaine)"]
for a in q("select id, description, source_doc, readings, status from ambiguities order by id"):
    p += [f"### {a[0]} — {a[4]}", "",
          f"- **Constat** : {a[1]}",
          f"- **Sources** : {a[2]}",
          f"- **Lectures possibles** : {a[3]}", ""]
p += ["## Règle de préséance (rappel)", "",
 "§2.1 du Contrat Principal : en cas de conflit, le Contrat Principal prévaut sur l'Annexe A, qui prévaut sur l'Annexe B, qui prévaut sur l'Annexe C, qui prévaut sur l'Annexe D. Tout conflit identifié doit être signalé à l'autre partie sous 10 JO (§2.2)."]
open("workspace/output/.parts/frag_conflicts.md", "w", encoding="utf-8").write("\n".join(p) + "\n")

# --- resume executif ---
tot = q("select count(*) from obligations")[0][0]
by_p = dict(q("select party, count(*) from obligations group by 1"))
by_c = dict(q("select category, count(*) from obligations group by 1 order by 2 desc"))
n_ms = q("select count(*) from milestones")[0][0]
n_cf = q("select count(*) from conflicts")[0][0]
n_am = q("select count(*) from ambiguities")[0][0]
p = ["# Résumé exécutif — Registre des obligations contractuelles FNG-01", "",
 f"Corpus de 5 documents (contrat principal, annexes A à D) analysé ; le registre couvre **{tot} obligations** : "
 f"**{by_p.get('TITULAIRE',0)} Titulaire**, **{by_p.get('AC',0)} AC**, **{by_p.get('CONJOINTE',0)} conjointes**, "
 f"et **{n_ms} jalons** (dont 2 cibles d'acceptation et 9 dates indicatives GFE/GFI).",
 "", "## Principaux constats", "",
 f"1. **{n_cf} conflit tranché par préséance** : CONF-001 — échéance du rapport mensuel (10e JO au Contrat Principal §4.2 vs 7e JO à CDRL-005) ; le Contrat Principal prévaut (§2.1). Obligation OBL-0010 marquée EN_CONFLIT.",
 f"2. **{n_am} ambiguïtés ouvertes** soumises à validation humaine, dont deux structurantes :",
 "   - AMBIG-001 : A1/A2 sont des dates d'acceptation **cible** ; les périodes de soutien (12 mois) et garantie (24 mois) sont ancrées sur l'acceptation **effective**, date inconnue.",
 "   - AMBIG-002 : aucun calendrier de jours fériés fourni ; les délais en JO ne peuvent être convertis en dates exactes — les règles contractuelles sont conservées telles quelles.",
 "3. **Charge du Titulaire** : 103 obligations (livrables, revues, essais, configuration, cyber, soutien, garantie, planning) ; 30 pour l'AC (fournitures GFE/GFI, approbations, revues) ; 4 conjointes (COPIL, signalements de conflits et d'incidents de sécurité).",
 "", "## Top catégories"]
for k, v in list(by_c.items())[:8]:
    p.append(f"- **{k}** : {v}")
p += ["",
 "## Points de vigilance pour le Contract Manager",
 "",
 "- Suivre le délai d'acceptation effectif FNG-01/FNG-02 : il ancre soutien initial (12 mois) et garantie (24 mois) — planifier sur les cibles A1/A2 mais ne pas les traiter comme des butoirs.",
 "- Les 9 dates GFE/GFI de l'Annexe D sont indicatives ; la règle de l'Annexe C fait foi en cas d'écart de planning.",
 "- Le terme « revue majeure » (OBL-0016, CDRL-003/027) reste à faire préciser par l'AC (AMBIG-003).",
 "- Confirmer si KO (Annexe D) = Revue de Lancement (Annexe A §A2) (AMBIG-004).",
 ""]
open("workspace/output/.parts/frag_exec.md", "w", encoding="utf-8").write("\n".join(p) + "\n")
print("frag_conflicts.md + frag_exec.md OK")
con.close()
