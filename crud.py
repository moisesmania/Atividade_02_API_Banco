from sqlalchemy.orm import Session
import models


def listar_movimentacoes(db: Session):
    return db.query(models.Movimentacao).all()

def listar_correntistas(db: Session):
    return db.query(models.Correntista).all()

def get_extrato(db: Session, correntista_id: int):
    return db.query(models.Extrato).filter(models.Extrato.CorrentistaID == correntista_id).all()
