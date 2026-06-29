from app.analyzers.decision_engine_v2 import DecisionEngineV2

def test_atlasclaim_mrh_irsi_recourse():
    engine = DecisionEngineV2()
    result = engine.analyze(
        "Dégât des eaux le 12/06/2026 au 12 rue Victor Hugo. Fuite du voisin du dessus. Photos et devis 2350 euros.",
        "D-TEST"
    )
    assert result["branch"] == "MRH"
    assert result["convention"] == "IRSI"
    assert result["recourse_recommendation"] == "Oui, recours recommandé"

def test_atlasclaim_auto_irsa():
    engine = DecisionEngineV2()
    result = engine.analyze(
        "Accident automobile avec tiers identifié. Constat amiable, photos et devis 980 euros.",
        "A-TEST"
    )
    assert result["branch"] == "AUTO"
    assert "IRSA" in result["convention"]