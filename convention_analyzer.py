# Sprint v0.4 — AtlasClaim

Objectif :
Remplacer la logique dispersée par un objet métier central `AtlasClaim`.

## Pipeline
1. CircumstancesAnalyzer
2. ConventionAnalyzer
3. CompletenessAnalyzer
4. ExpertiseAnalyzer
5. RecourseAnalyzer
6. DecisionEngineV2

## Valeur
Chaque module enrichit le même objet dossier.
Cela prépare Atlas à intégrer plus tard :
- contrats ;
- garanties ;
- OCR ;
- photos ;
- connecteurs GED ;
- SI assureur.