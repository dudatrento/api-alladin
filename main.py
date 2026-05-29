from fastapi import FastAPI, HTTPException, Query
from datetime import date
import httpx

app = FastAPI(
    title="API de Preços de Tapetes",
    description="Consulta preços de tapetes de uma fonte externa e expõe os dados com a data da consulta.",
)

url = "https://testedefensoriapr.pythonanywhere.com/precos"

@app.get("/precos", summary="Consulta preços de tapetes")
async def get_precos(
    data: date = Query(..., description="Data da consulta no formato AAAA-MM-DD. Exemplo: 2026-05-28")
) -> dict:
    """
    Consulta os preços de tapetes disponíveis na API externa
    e retorna os dados junto com a data informada.
    """
    try:
        async with httpx.AsyncClient() as client:
            resposta = await client.get(url, timeout=10.0)
            resposta.raise_for_status() 
            dados = resposta.json()
            
            if not dados:
                raise HTTPException(status_code=404, detail="Nenhum preço encontrado.")
            
            return {
                "data_consulta": data,
                "precos": dados
            }
            
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="A API externa demorou demais para responder. Tente novamente em instantes."
        )
    except httpx.HTTPStatusError:
        raise HTTPException(
            status_code=502,
            detail="A API externa retornou um erro inesperado."
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar à API externa. Tente novamente mais tarde."
        )
    
    