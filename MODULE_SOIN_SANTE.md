# MODULE_SOIN_SANTE.md

## Objet
Souche **SOINS** (santé & protection sociale) : équité d’accès, sécurité clinique, interop **FHIR/openEHR**.

## Fairness Index (exemple)
- Base : 1 − Gini(outcomes)
- Pondération : segments vulnérables (âge, comorbidités, zones sous‑denses)
- Seuil ΔM11.3 : rollback si index < 0.85

## FHIR (exemple minimal)
- Ressources : Patient, Encounter, Observation, Condition, Procedure
- Voir `FHIR_PROFILE_Soin.json`

## openEHR (mapping)
- Voir `openEHR_MAPPING_Soin.md`

## Sécurité clinique (MDR)
- Human‑in‑command
- Journalisation d’alertes & justifications (explainability logs)
- Kill‑switch accessible (Aegis/clinicien)
