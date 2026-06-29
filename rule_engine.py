# Sprint v0.5 — Plateforme industrielle

## Ajouts

### Cycle de vie
Le dossier suit maintenant des statuts :
- CREATED
- DOCUMENTS_RECEIVED
- QUALIFIED
- CONVENTION_CHECKED
- COMPLETENESS_CHECKED
- EXPERTISE_DECIDED
- RECOURSE_CHECKED
- READY_FOR_MANAGER

### Journal d’audit
Chaque étape ajoute une trace :
- étape ;
- message ;
- données ;
- horodatage.

### Rule Engine
Les règles métier peuvent être placées dans `knowledge-base/rules`.

Exemple :
- recours DDE MRH si montant > 1600 €
- IRSA / IDA si auto avec tiers

## Valeur industrielle
Cette architecture permet :
- traçabilité ;
- audit ;
- configuration par assureur ;
- évolution sans réécrire le moteur.