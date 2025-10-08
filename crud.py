from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
import models, schemas
from decimal import Decimal
from models import Correntista, Movimentacao  # <-- importar seus modelos


# Listar correntistas
def listar_correntistas(db: Session):
    return db.query(models.Correntista).all()

# Listar movimentações
def listar_movimentacoes(db: Session):
    return db.query(models.Movimentacao).all()

# Extrato
def get_extrato(db: Session, correntista_id: int):
    return db.query(models.Extrato).filter(models.Extrato.CorrentistaID == correntista_id).all()

# --- Operações financeiras ---
def deposito(db: Session, op: schemas.OperacaoBase):
    correntista = db.query(models.Correntista).filter(models.Correntista.CorrentistaID == op.CorrentistaID).first()
    if not correntista:
        return None
    
    # Converter float para Decimal
    valor = Decimal(str(op.ValorOperacao))
    correntista.Saldo += valor

    mov = models.Movimentacao(
        TipoOperacao='D',
        CorrentistaID=op.CorrentistaID,
        ValorOperacao=valor,
        DataOperacao=datetime.now(),
        Descricao=op.Descricao
    )
    db.add(mov)
    db.commit()
    db.refresh(mov)
    return mov



def saque(db: Session, op):
    # Buscar correntista
    correntista = db.query(Correntista).filter_by(CorrentistaID=op.CorrentistaID).first()
    if not correntista:
        raise Exception("Correntista não encontrado")
    
    # Converter valor para Decimal
    valor = Decimal(op.ValorOperacao)
    
    # Verificar saldo
    if correntista.Saldo < valor:
        raise Exception("Saldo insuficiente")
    
    # Atualizar saldo
    correntista.Saldo -= valor
    
    # Registrar movimentação
    mov = Movimentacao(
        TipoOperacao='D',  # 'D' para saque
        CorrentistaID=op.CorrentistaID,
        ValorOperacao=valor,
        DataOperacao=datetime.now(),  # <-- Preencher a data/hora atual
        Descricao='Saque em caixa',
        CorrentistaBeneficiarioID=None
    )
    db.add(mov)
    db.commit()
    db.refresh(mov)
    
    return mov

def pagamento(db: Session, op: schemas.OperacaoBase):
    # Buscar o correntista
    correntista = db.query(Correntista).filter_by(CorrentistaID=op.CorrentistaID).first()
    if not correntista:
        raise ValueError("Correntista não encontrado")
    
    # Garantir que o valor seja Decimal
    valor = Decimal(op.ValorOperacao)
    
    # Atualizar saldo
    if correntista.Saldo < valor:
        raise ValueError("Saldo insuficiente para pagamento")
    correntista.Saldo -= valor
    db.commit()
    
    # Criar movimentação
    mov = Movimentacao(
        TipoOperacao='D',
        CorrentistaID=op.CorrentistaID,
        ValorOperacao=valor,
        DataOperacao=datetime.now(),
        Descricao=f"Pagamento: {op.Descricao}"
    )
    db.add(mov)
    db.commit()
    db.refresh(mov)
    return mov

def transferencia(db, op):
    corr_origem = db.query(Correntista).filter_by(CorrentistaID=op.CorrentistaID).first()
    corr_destino = db.query(Correntista).filter_by(CorrentistaID=op.CorrentistaBeneficiarioID).first()

    valor = Decimal(str(op.ValorOperacao))

    corr_origem.Saldo -= valor
    corr_destino.Saldo += valor

    mov = Movimentacao(
        TipoOperacao='D',
        CorrentistaID=op.CorrentistaID,
        ValorOperacao=valor,
        DataOperacao=datetime.now(),  # <-- garante que não seja NULL
        Descricao='Transferência',
        CorrentistaBeneficiarioID=op.CorrentistaBeneficiarioID
    )

    db.add(mov)
    db.commit()
    db.refresh(mov)
    return mov

