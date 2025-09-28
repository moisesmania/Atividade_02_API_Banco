from sqlalchemy import Column, Integer, String, CHAR, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Correntista(Base):
    __tablename__ = "Correntistas"
    CorrentistaID = Column(Integer, primary_key=True, index=True)
    NomeCorrentista = Column(String(50), nullable=False)
    Saldo = Column(Numeric(18,2), nullable=False)

    movimentacoes = relationship(
        "Movimentacao",
        back_populates="correntista",
        foreign_keys="Movimentacao.CorrentistaID"
    )

class Movimentacao(Base):
    __tablename__ = "Movimentacoes"
    MovimentacaoID = Column(Integer, primary_key=True, index=True)
    TipoOperacao = Column(CHAR(1), nullable=False)
    CorrentistaID = Column(Integer, ForeignKey("Correntistas.CorrentistaID"))
    ValorOperacao = Column(Numeric(18,2), nullable=False)
    DataOperacao = Column(DateTime, nullable=False)
    Descricao = Column(String(50), nullable=False)
    CorrentistaBeneficiarioID = Column(Integer, ForeignKey("Correntistas.CorrentistaID"), nullable=True)

    correntista = relationship(
        "Correntista",
        back_populates="movimentacoes",
        foreign_keys=[CorrentistaID]
    )

    beneficiario = relationship(
        "Correntista",
        foreign_keys=[CorrentistaBeneficiarioID],
        viewonly=True
    )

# --- Somente leitura para a view de extrato ---
class Extrato(Base):
    __tablename__ = "vwExtrato"
    __table_args__ = {"extend_existing": True}

    CorrentistaID = Column(Integer, primary_key=True)
    NomeCorrentista = Column(String(50))
    TipoOperacao = Column(String(10))
    MovimentacaoID = Column(Integer)
    Descricao = Column(String(50))
    DataOperacao = Column(DateTime)
    ValorOperacao = Column(Numeric(18,2))
    BeneficiarioID = Column(Integer, nullable=True)
    NomeBeneficiario = Column(String(50), nullable=True)
