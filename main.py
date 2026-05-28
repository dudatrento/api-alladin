from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/precos")
async def get_precos():
    url = "https://testedefensoriapr.pythonanywhere.com/precos"
    async with httpx.AsyncClient() as client:
        resposta = await client.get(url)
        return resposta.json()
    
    
    