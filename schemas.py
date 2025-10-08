from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CorrentistaResponse(BaseModel):
    CorrentistaID: int
    NomeCorrentista: str
    Saldo: float
    class Config:
        orm_mode = True

class MovimentacaoResponse(BaseModel):
    MovimentacaoID: int
    TipoOperacao: str
    CorrentistaID: int
    ValorOperacao: float
    DataOperacao: datetime
    Descricao: str
    CorrentistaBeneficiarioID: Optional[int]
    class Config:
        orm_mode = True

class ExtratoResponse(BaseModel):
    CorrentistaID: int
    NomeCorrentista: str
    TipoOperacao: str
    MovimentacaoID: int
    Descricao: str
    DataOperacao: datetime
    ValorOperacao: float
    BeneficiarioID: Optional[int]
    NomeBeneficiario: Optional[str]
    class Config:
        orm_mode = True

class OperacaoBase(BaseModel):
    CorrentistaID: int
    ValorOperacao: float
    Descricao: str
    CorrentistaBeneficiarioID: Optional[int] = None
