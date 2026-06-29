id: MRH-DDE-RECOURS-001
name: Recours DDE MRH si responsable identifié et montant supérieur au seuil
conditions:
  branch: MRH
  claim_type: Dégât des eaux
  third_party: Oui
  amount:
    gt: 1600
actions:
  recourse_recommendation: Oui, recours recommandé
explanation: Responsable identifié et montant supérieur au seuil paramétré : recours recommandé.