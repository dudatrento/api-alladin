from fastapi import FastAPI, HTTPException
from datetime import date
import httpx

app = FastAPI()

@app.get("/precos")
async def get_precos(data: date):
    url = "https://testedefensoriapr.pythonanywhere.com/precos"
    
    try:
        async with httpx.AsyncClient() as client:
            resposta = await client.get(url, timeout=10.0)
            resposta.raise_for_status() 
            dados = resposta.json()
    except httpx.HTTPError:
        raise HTTPException(status_code=503, detail="O serviço de preços não está disponível no momento.")
        
    return {
        "data_consulta": data,
        "precos": dados
    }