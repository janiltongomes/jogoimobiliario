from fastapi import APIRouter
from fastapi.responses import JSONResponse
from repository.db import get_connection
from services.jogo import JogoService

router = APIRouter()


@router.get("/jogo/simular")
def simular():
    conn = get_connection()
    service = JogoService(conn)
    resultado = service.simular()
    
    return JSONResponse(content=resultado)
