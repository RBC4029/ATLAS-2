# Patch Atlas v0.4 — AtlasClaim Architecture

Ce patch ajoute :
- un objet métier central `AtlasClaim`
- des analyseurs séparés :
  - CircumstancesAnalyzer
  - ConventionAnalyzer
  - CompletenessAnalyzer
  - ExpertiseAnalyzer
  - RecourseAnalyzer
  - DecisionEngine
- un nouvel endpoint : `POST /api/v1/claims/analyze-v2`
- un test métier v0.4

## Comment appliquer

Dans GitHub :
1. Ouvre ton dépôt ATLAS-2.
2. Upload le contenu de ce dossier patch.
3. Commit message : `Add AtlasClaim architecture v0.4`.