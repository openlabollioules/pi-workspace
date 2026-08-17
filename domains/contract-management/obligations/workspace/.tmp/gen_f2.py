# Fragments : registre des obligations (tete + 5 sections par document)
import duckdb, os
OUT = 'workspace/output/.parts'
con = duckdb.connect('workspace/data/obligations.duckdb')
def q(sql, *a): return con.execute(sql, a).fetchall()

P = {"TITULAIRE": "T", "AC": "AC", "CONJOINTE": "CJ"}
head = ["# Registre des obligations contractuelles — Programme FNG-01", "",
 "Registre traçable généré depuis DuckDB (`workspace/data/obligations.duckdb`). Chaque obligation cite un document ET un localisateur. Les sources multiples sont listées (ex. Contrat + CDRL).",
 "",
 "Légende parties : **T** = Titulaire (Navisys Défense Maritime SAS), **AC** = Autorité Contractante (Agence des Capacités Navales), **CJ** = conjointe.",
 "Statuts : EXTRAITE / EN_CONFLIT. Confiance : HAUTE (texte explicite) / MOYENNE (interprétation documentée).",
 ""]
open(f"{OUT}/frag_reg_head.md", "w", encoding="utf-8").write("\n".join(head) + "\n")

DOCS = [
 ("01-contrat-principal", "Contrat Principal (ACN-FNG-2026-001)"),
 ("02-annexe-a-specification-technique", "Annexe A — Spécification technique"),
 ("03-annexe-b-livrables-cdrl", "Annexe B — Livrables CDRL"),
 ("04-annexe-c-responsabilites", "Annexe C — Responsabilités"),
]
for doc, label in DOCS:
    rows = q("select id, party, obligation, category, trigger, deadline, deliverable, source_doc, source_locator, confidence, status, notes from obligations where source_doc like ? order by id", f"%{doc}%")
    p = [f"## {label} — {len(rows)} obligations", "",
         "| ID | Partie | Obligation | Catégorie | Déclencheur | Échéance | Livrable | Source | Conf. | Statut | Notes |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        cells = [r[0], P[r[1]], r[2], r[3] or "—", r[4] or "—", r[5] or "—", r[6] or "—",
                 (f"`{r[7]}` {r[8]}" if r[7] == doc else f"`{r[7]}`"),
                 r[9], r[10], r[11] or "—"]
        p.append("| " + " | ".join(cells) + " |")
    p.append("")
    open(f"{OUT}/frag_reg_{doc.split('-')[0]}.md", "w", encoding="utf-8").write("\n".join(p) + "\n")
    print(f"frag_reg_{doc.split('-')[0]}.md : {len(rows)} lignes")

# Section Annexe D (jalons)
ms = q("select id, name, date, kind, source_doc from milestones order by date")
p = ["## Annexe D — Planning contractuel (jalons)", "",
 "Jalons issus de l'Annexe D. **CONTRACTUELLE** : jalon contractuel ; **CIBLE** : date cible (non butoir) ; **INDICATIF** : date dérivée, indicative uniquement (règle de l'Annexe C applicable).",
 "",
 "| Jalon | Libellé | Date | Type | Source |", "|---|---|---|---|---|"]
for r in ms:
    p.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | `{r[4]}` |")
p.append("")
open(f"{OUT}/frag_reg_05.md", "w", encoding="utf-8").write("\n".join(p) + "\n")
print("frag_reg_05.md :", len(ms), "jalons")
con.close()
