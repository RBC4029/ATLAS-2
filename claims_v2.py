from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass
class AtlasClaim:
    claim_id: str
    raw_text: str

    branch: str = "UNKNOWN"
    claim_type: str = "Non identifié"
    cause: str = "Inconnue"
    origin: str = "Inconnue"
    third_party: str = "Inconnu"
    probable_responsible: str = "Inconnu"

    contract_active: bool = True
    guarantee_probable: bool = False
    convention: Optional[str] = None
    amount: Optional[int] = None

    documents: Dict[str, bool] = field(default_factory=dict)
    missing_documents: List[str] = field(default_factory=list)

    confidence: int = 0
    completeness_score: int = 0

    expertise_recommendation: str = "À vérifier"
    settlement_recommendation: str = "Non"
    recourse_recommendation: str = "Non"
    decision_path: str = "Analyse gestionnaire"

    explanation: List[str] = field(default_factory=list)
    next_actions: List[str] = field(default_factory=list)

    def explain(self, message: str):
        self.explanation.append(message)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "claim_id": self.claim_id,
            "branch": self.branch,
            "claim_type": self.claim_type,
            "cause": self.cause,
            "origin": self.origin,
            "third_party": self.third_party,
            "probable_responsible": self.probable_responsible,
            "contract_active": self.contract_active,
            "guarantee_probable": self.guarantee_probable,
            "convention": self.convention,
            "amount": self.amount,
            "documents": self.documents,
            "missing_documents": self.missing_documents,
            "confidence": self.confidence,
            "completeness_score": self.completeness_score,
            "expertise_recommendation": self.expertise_recommendation,
            "settlement_recommendation": self.settlement_recommendation,
            "recourse_recommendation": self.recourse_recommendation,
            "decision_path": self.decision_path,
            "explanation": self.explanation,
            "next_actions": self.next_actions,
        }