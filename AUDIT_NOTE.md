# AUDIT_NOTE.md

## Incohérences actuelles
1) Pas de tests automatisés/CI intégrée
2) README module‑spécifique manquant pour certains POC
3) Versioning non standard (RELEASE_LIST non SemVer)
4) Sécurité déclarée (Merkle, kill‑switch) non démontrée

## Plan d’actions
- CI benchmark (fichier ci_benchmark_ministere.yml à déplacer en .github/workflows/)
- README par POC, exemples paramétrés
- Normaliser CHANGELOG (SemVer) + tags Git
- POC Merkle & kill‑switch humain (journal + rôle Aegis)
