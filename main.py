from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Banco - FastAPI + SQL Server")

@app.get("/correntistas", response_model=list[schemas.CorrentistaResponse])
def get_correntistas(db: Session = Depends(get_db)):
    return crud.listar_correntistas(db)

@app.get("/movimentacoes", response_model=list[schemas.MovimentacaoResponse])
def get_movimentacoes(db: Session = Depends(get_db)):
    return crud.listar_movimentacoes(db)

@app.get("/extrato/{correntista_id}", response_model=list[schemas.ExtratoResponse])
def extrato(correntista_id: int, db: Session = Depends(get_db)):
    extrato_data = crud.get_extrato(db, correntista_id)
    if not extrato_data:
        raise HTTPException(status_code=404, detail="Extrato não encontrado")
    return extrato_data

# --- Operações ---
@app.post("/deposito", response_model=schemas.MovimentacaoResponse)
def rota_deposito(op: schemas.OperacaoBase, db: Session = Depends(get_db)):
    mov = crud.deposito(db, op)
    if not mov:
        raise HTTPException(status_code=400, detail="Depósito falhou")
    return mov

@app.post("/saque", response_model=schemas.MovimentacaoResponse)
def rota_saque(op: schemas.OperacaoBase, db: Session = Depends(get_db)):
    mov = crud.saque(db, op)
    if not mov:
        raise HTTPException(status_code=400, detail="Saque falhou ou saldo insuficiente")
    return mov

@app.post("/pagamento", response_model=schemas.MovimentacaoResponse)
def rota_pagamento(op: schemas.OperacaoBase, db: Session = Depends(get_db)):
    mov = crud.pagamento(db, op)
    if not mov:
        raise HTTPException(status_code=400, detail="Pagamento falhou ou saldo insuficiente")
    return mov

@app.post("/transferencia", response_model=schemas.MovimentacaoResponse)
def rota_transferencia(op: schemas.OperacaoBase, db: Session = Depends(get_db)):
    mov = crud.transferencia(db, op)
    if not mov:
        raise HTTPException(status_code=400, detail="Transferência falhou ou saldo insuficiente")
    return mov
