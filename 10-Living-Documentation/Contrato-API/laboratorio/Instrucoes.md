## Executando a API 
No terminal, dentro da pasta do projeto, execute os comandos:
```bash
python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Depois, acesse os seguintes endereços:

### Swagger UI 
`http://127.0.0.1:8000/docs` \
Interface interativa para visualizar e testar os endpoints.

### OpenAPI JSON
`http://127.0.0.1:8000/openapi.json` \
Documento estruturado que descreve o contrato da API.

### ReDoc
`http://127.0.0.1:8000/redoc` \
Outra interface para consultar a documentação gerada
a partir do OpenAPI.

---

## Referências Oficiais
FastAPI: https://fastapi.tiangolo.com/

OpenAPI Specification: https://spec.openapis.org/oas/latest.html

Swagger UI: https://swagger.io/tools/swagger-ui/

ReDoc: https://redocly.com/docs/redoc
