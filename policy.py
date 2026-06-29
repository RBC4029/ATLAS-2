# Patch Atlas v0.6 — Domain Model Assurance

Ajouts :
- modèle métier assurance :
  - Policy
  - Coverage
  - Insured
  - Risk
  - ThirdParty
  - Damage
  - ExpertiseDecision
  - SettlementProposal
  - RecourseDecision
- CoverageAnalyzer
- endpoint `/api/v1/claims/analyze-v4`
- tests moteur contrat / garanties

But :
Ne plus supposer seulement "contrat actif", mais préparer Atlas à recevoir les données du SI assureur.