README.md completo e pronto, formatado em Markdown:
# API Banco - Rotas GET

Na sua API você possui apenas **2 rotas GET** para consulta:

---

### 1️⃣ Listar Correntistas
- **Método:** GET  
- **URL:** `/correntistas`  
- **Descrição:** Retorna todos os correntistas cadastrados no banco.  

**Exemplo de resposta:**
```json
[
  {
    "CorrentistaID": 1,
    "NomeCorrentista": "Moisés",
    "Saldo": 1000.00
  },
  {
    "CorrentistaID": 2,
    "NomeCorrentista": "João",
    "Saldo": 500.00
  }
]


# API de Movimentações Bancárias

Esta API permite consultar correntistas, visualizar extratos e realizar operações financeiras: depósito, saque, pagamento e transferência.

---

## 🔹 ROTAS GET (somente consulta / leitura)

### 1️⃣ Listar todos os correntistas
- **Método:** GET  
- **URL:** `http://127.0.0.1:8000/correntistas`  
- **Body:** nenhum  

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

2️⃣ Listar todas as movimentações / extrato de um correntista

Método: GET

URL: http://127.0.0.1:8000/extrato/{correntista_id}
(substitua {correntista_id} pelo ID do correntista)

Body: nenhum

Exemplo de resposta:

[
  {
    "CorrentistaID": 1,
    "NomeCorrentista": "Pedro",
    "TipoOperacao": "Depósito",
    "MovimentacaoID": 1,
    "Descricao": "Depósito inicial",
    "DataOperacao": "2025-10-07T21:00:00",
    "ValorOperacao": 500.0,
    "BeneficiarioID": null,
    "NomeBeneficiario": null
  }
]

🔹 ROTAS POST (criação / alteração de dados)
3️⃣ Depósito

Método: POST

URL: http://127.0.0.1:8000/deposito

Body → raw → JSON:

{
  "CorrentistaID": 1,
  "ValorOperacao": 500.00,
  "Descricao": "Depósito em caixa"
}

4️⃣ Saque

Método: POST

URL: http://127.0.0.1:8000/saque

Body → raw → JSON:

{
  "CorrentistaID": 1,
  "ValorOperacao": 100.00,
  "Descricao": "Saque em caixa"
}

5️⃣ Pagamento

Método: POST

URL: http://127.0.0.1:8000/pagamento

Body → raw → JSON:

{
  "CorrentistaID": 1,
  "ValorOperacao": 150.00,
  "Descricao": "Pagamento fatura cartão"
}

6️⃣ Transferência

Método: POST

URL: http://127.0.0.1:8000/transferencia

Body → raw → JSON:

{
  "CorrentistaID": 5,
  "CorrentistaBeneficiarioID": 1,
  "ValorOperacao": 200.00,
  "Descricao": "Transferência do correntista 5 para 1"
}


⚠️ Importante: Não é possível usar GET para criar ou alterar dados — apenas para listar/consultar.

⚡ Dicas de Teste

Use o Postman ou outro cliente HTTP para testar os endpoints.

Sempre use GET para consultas (listar correntistas ou extrato).

Sempre use POST para operações financeiras (depósito, saque, pagamento, transferência).

Para transferências, certifique-se de que o correntista de origem tenha saldo suficiente.

📌 Exemplo de fluxo

Listar correntistas → GET /correntistas

Depositar → POST /deposito

Sacar → POST /saque

Pagar fatura → POST /pagamento

Transferir → POST /transferencia

Verificar extrato → GET /extrato/{correntista_id}
