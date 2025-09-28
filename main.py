from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import engine, get_db

app = FastAPI(title="API Banco - FastAPI + SQL Server")  # <- ESSENCIAL: app

# Exemplos de rotas
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
