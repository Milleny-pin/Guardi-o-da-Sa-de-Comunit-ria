from fastapi import FastAPI
from app.routers import reports

app = FastAPI(
    title="Guardião Comunitário API",
    description="API para reportar e visualizar problemas de saúde pública.",
    version="0.1.0"
)

# Pendura as rotas do report na aplicação principal
# reports.router é o objeto APIRouter que definimos em reports.py

                                   # Argumento que define o prefixo da URL base que será adicionado as rotas nesse router
app.include_router(reports.router, prefix='/api/v1')
        
              # tags=["Root"]: Diz ao FastAPI para agrupar este endpoint (/) sob o cabeçalho "Root" na documentação do /docs.
@app.get("/", tags=["Root"])
def read_root(): 

    return {"status": "API do Guardião Comunitário está online!"}