# Hypothèses du bootstrap

| # | Hypothèse | Impact si fausse |
|---|-----------|------------------|
| A1 | Les 5 fichiers de `workspace/contract/` constituent le corpus contractuel complet (contrat principal + Annexes A, B, C, D). | Le registre serait incomplet ; à signaler comme information manquante, pas à inventer. |
| A2 | L'ordre de préséance du contrat principal §2.1 (contrat > Annexe A > Annexe B > Annexe C > Annexe D) s'applique à toutes les contradictions explicites. | La résolution des conflits changera ; les conflits devront rester ouverts en VALIDATION_HUMAINE. |
| A3 | Les dates du planning (Annexe D) sont des dates calendaires de baseline ; les rappels GFE/GFI y sont indicatifs (règle explicite du planning). | Le croisement des échéances devra marquer « indicatif ». |
| A4 | Aucun calendrier de jours fériés n'est disponible : les calculs en JO restent des règles contractuelles, pas des dates exactes. | Aucune date exacte ne doit être produite pour des délais en JO à partir d'un événement futur. |
| A5 | Les jalons A1/A2 sont des « acceptations contractuelles cible » (cible, pas effective). | Toute échéance dérivée (CDRL-018…021) doit rester attachée au jalon, pas à une date figée. |
| A6 | Le POC tourne avec les outils locaux pi-office (PDF/XLSX) et pi-alchemy/DuckDB, sans Internet. | Le processus d'ingestion devra s'adapter si un outil manque. |
| A7 | « ~80 obligations de référence » : le compte de référence effectif établi lors du bootstrap est d'environ 95–100 obligations (voir evaluator/ground-truth.md). Le seuil MVP de 80 % de couverture reste applicable. | Seuil de succès à recalibrer si besoin. |
