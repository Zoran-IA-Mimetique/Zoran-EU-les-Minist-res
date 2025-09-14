# openEHR_MAPPING_Soin.md

- Demographics.person.name → FHIR Patient.name
- EHR.composition.care_entry.problem_diagnosis → FHIR Condition
- Observation.laboratory-test → FHIR Observation(code, value, unit)
