from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class CorrentistaResponse(BaseModel):
    CorrentistaID: int
    NomeCorrentista: str
    Saldo: Decimal

    model_config = {"from_attributes": True}  # Pydantic V2

class MovimentacaoResponse(BaseModel):
    MovimentacaoID: int
    TipoOperacao: str
    CorrentistaID: int
    ValorOperacao: Decimal
    DataOperacao: datetime
    Descricao: str
    CorrentistaBeneficiarioID: Optional[int]

    model_config = {"from_attributes": True}

class ExtratoResponse(BaseModel):
    CorrentistaID: int
    NomeCorrentista: str
    TipoOperacao: str
    MovimentacaoID: int
    Descricao: str
    DataOperacao: datetime
    ValorOperacao: Decimal
    BeneficiarioID: Optional[int]
    NomeBeneficiario: Optional[str]

    model_config = {"from_attributes": True}
