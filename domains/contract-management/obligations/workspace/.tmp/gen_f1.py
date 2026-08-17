# Fragments : rapport d'ingestion
import duckdb, os
OUT = 'workspace/output/.parts'
os.makedirs(OUT, exist_ok=True)
con = duckdb.connect('workspace/data/obligations.duckdb')
def q(sql, *a): return con.execute(sql, a).fetchall()
docs = q("select doc_id, path, doc_type, contract_ref, version from documents order by doc_id")
p = ["# Rapport d'ingestion des données", "",
 "Corpus : programme FNG-01 (fictif) — 5 documents contractuels, `workspace/contract/`.", "",
 "| Document | Type | Référence contractuelle | Version |", "|---|---|---|---|"]
for d in docs:
    p.append(f"| `{d[0]}` ({d[1]}) | {d[2]} | {d[3]} | {d[4]} |")
p += ["", "## Méthode d'ingestion", "",
 "- PDF : extraction texte intégrale, lecture complète (9 + 6 pages).",
 "- XLSX : structure inspectée, 12 tables chargées dans DuckDB (`workspace/data/obligations.duckdb`) puis requêtes ciblées (toutes < 30 lignes).",
 "- Tables chargées : cdrl (30), submission_rules (3), gfe_gfi (9), titulaire_gfe (4), joint_reviews (6), review_minutes (1), site_access (2), test_data (2), milestones_x (19), training (6), gfe_gfi_derived (9), assumptions (3).",
 "- Dates de l'Annexe D : nombres sériels Excel convertis en dates calendaires ; dates dérivées GFE/GFI marquées INDICATIF.",
 "", "## Vérifications de cohérence à l'ingestion", "",
 "- Dates dérivées GFE/GFI (Annexe D) cohérentes avec les règles de l'Annexe C (ex. GFI-03 : 30 j cal. avant PDR 2028-02-15 → 2028-01-16 ; GFE-02 : 90 j cal. avant INT1 2032-03-10 → 2031-12-11).",
 "- Feuille `Hypotheses` (Annexe D) : dates GFE/GFI dérivées indicatives ; en cas de conflit, les règles de l'Annexe C priment ; aucun calendrier de jours fériés fourni.",
 "- **Conflit détecté** : Contrat Principal §4.2 (rapport mensuel au **10e JO**) vs CDRL-005 (**7e JO**) → CONF-001.",
 "- A1/A2 qualifiées « Acceptation contractuelle **cible** » → type CIBLE (AMBIG-001).",
 "", "## État des tables de travail (DuckDB)", ""]
for t, n in q("select t, n from (values ('obligations', (select count(*) from obligations)), ('milestones', (select count(*) from milestones)), ('conflicts', (select count(*) from conflicts)), ('ambiguities', (select count(*) from ambiguities)), ('documents', (select count(*) from documents))) as t(t, n)"):
    p.append(f"- `{t}` : {n} lignes")
p += ["", "Aucun document source n'a été modifié (corpus en lecture seule)."]
open(f"{OUT}/frag_ingestion.md", "w", encoding="utf-8").write("\n".join(p) + "\n")
print("frag_ingestion.md OK")
