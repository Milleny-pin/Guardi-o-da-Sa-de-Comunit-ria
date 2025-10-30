from fastapi import APIRouter, File, UploadFile, Form
from typing import Annotated
import shutil
from pathlib import Path

#  Instância
router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

# Cria um diretório temporário para salvar os arquivos recebidos
UPLOAD_DIR = Path("temp_uploads")
UPLOAD_DIR.mkdir(exist_ok=True) # Cria a pasta caso não existir

# Rota que recebe a foto ou localização
@router.post("/submit")
async def submit_report(
    # latitude: nome do parâmetro da função
    # Float: tipo de dado que deve ter
    # Form: Função especial do FASTAPI
    # Annotated: Recurso do python que permite adicionar metadados a um tipo
    latitude: Annotated[float, Form()],
    longitude: Annotated[float, Form()],
    user_id: Annotated[str, Form()] = 'anonymous',
    file: UploadFile = File(...)
):
    # Salva o arquivo temporariamente no disco para processamento
    file_path = UPLOAD_DIR / file.filename # Cria o caminho completo

    # Abre o caminho de destino em modo binário de escrita
    with file_path.open('wb') as buffer:
        # Copia o conteúdo do UploadFile para o arquivo no disco
        # Usa o read() e write() de forma assíncrona para ser mais performático

        shutil.copyfileobj(file.file, buffer)

        # file_path agr contém o caminho para o arquivo salvo

        # CHAMADA DA IA

        # SALVAR O BANCO

        # file_path.unlink() # Deleta o arquivo temporário

        return {
        "message": "Denúncia processada e IA pronta para agir!",
        "filename": file.filename,
        "latitude": latitude,
        }