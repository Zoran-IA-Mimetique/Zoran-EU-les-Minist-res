# TEST_PLAN.md

- `python3 POC_FairDispatch_Sante.py` → vérifier allocations + Fairness
- `FAIRNESS=0.80 python3 POC_EquityRollback.py` → ΔM11.3 déclenché
- `python3 benchmark_copilote_ministere.py` → génère benchmark_report.json
- (CI) déplacer `ci_benchmark_ministere.yml` en `.github/workflows/`
