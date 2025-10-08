# API Banco - Consulta e Operações Financeiras

Esta API permite consultar correntistas, visualizar extratos e realizar operações financeiras: depósito, saque, pagamento e transferência.

---

## 🔹 ROTAS GET (somente consulta / leitura)

### 1️⃣ Listar todos os correntistas
- **Método:** GET  
- **URL:** `http://127.0.0.1:8000/correntistas`  
- **Body:** nenhum  

**Descrição:** Retorna todos os correntistas cadastrados no banco.

**Exemplo de resposta:**
```json
[
  {
    "CorrentistaID": 1,
    "NomeCorrentista": "Pedro",
    "Saldo": 1000.00
  },
  {
    "CorrentistaID": 2,
    "NomeCorrentista": "João",
    "Saldo": 500.00
  }
]
2️⃣ Listar todas as movimentações
Método: GET

URL: http://127.0.0.1:8000/movimentacoes

Body: nenhum

Descrição: Retorna todas as movimentações realizadas por todos os correntistas.

Exemplo de resposta:

json
Copiar código
[
  {
    "MovimentacaoID": 1,
    "TipoOperacao": "D",
    "CorrentistaID": 1,
    "ValorOperacao": 500.0,
    "DataOperacao": "2025-10-07T21:00:00",
    "Descricao": "Depósito inicial",
    "CorrentistaBeneficiarioID": null
  },
  {
    "MovimentacaoID": 2,
    "TipoOperacao": "S",
    "CorrentistaID": 1,
    "ValorOperacao": 100.0,
    "DataOperacao": "2025-10-07T22:00:00",
    "Descricao": "Saque em caixa",
    "CorrentistaBeneficiarioID": null
  }
]
3️⃣ Listar extrato de um correntista específico
Método: GET

URL: http://127.0.0.1:8000/extrato/{correntista_id}
(substitua {correntista_id} pelo ID do correntista)

Body: nenhum

Descrição: Retorna todas as movimentações realizadas pelo correntista, incluindo depósitos, saques, pagamentos e transferências.

Exemplo de resposta:

json
Copiar código
[
  {
    "MovimentacaoID": 1,
    "CorrentistaID": 1,
    "NomeCorrentista": "Pedro",
    "TipoOperacao": "Depósito",
    "Descricao": "Depósito inicial",
    "DataOperacao": "2025-10-07T21:00:00",
    "ValorOperacao": 500.0,
    "BeneficiarioID": null,
    "NomeBeneficiario": null
  }
]
🔹 ROTAS POST (criação / alteração de dados)
4️⃣ Depósito
Método: POST

URL: http://127.0.0.1:8000/deposito

Body → raw → JSON:

json
Copiar código
{
  "CorrentistaID": 1,
  "ValorOperacao": 500.00,
  "Descricao": "Depósito em caixa"
}
5️⃣ Saque
Método: POST

URL: http://127.0.0.1:8000/saque

Body → raw → JSON:

json
Copiar código
{
  "CorrentistaID": 1,
  "ValorOperacao": 100.00,
  "Descricao": "Saque em caixa"
}
6️⃣ Pagamento
Método: POST

URL: http://127.0.0.1:8000/pagamento

Body → raw → JSON:

json
Copiar código
{
  "CorrentistaID": 1,
  "ValorOperacao": 150.00,
  "Descricao": "Pagamento fatura cartão"
}
7️⃣ Transferência
Método: POST

URL: http://127.0.0.1:8000/transferencia

Body → raw → JSON:

json
Copiar código
{
  "CorrentistaID": 5,
  "CorrentistaBeneficiarioID": 1,
  "ValorOperacao": 200.00,
  "Descricao": "Transferência do correntista 5 para 1"
}
⚠️ Importante
Não é possível usar GET para criar ou alterar dados — apenas para listar/consultar.

Para transferências, certifique-se de que o correntista de origem tenha saldo suficiente.

Use Postman ou outro cliente HTTP para testar os endpoints.

📌 Exemplo de fluxo de uso da API
Listar correntistas → GET /correntistas

Listar todas as movimentações → GET /movimentacoes

Depositar → POST /deposito

Sacar → POST /saque

Pagar fatura → POST /pagamento

Transferir → POST /transferencia

Verificar extrato → GET /extrato/{correntista_id}

