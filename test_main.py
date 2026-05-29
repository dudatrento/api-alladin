from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_precos_sucesso():
    response = client.get("/precos?data=2026-05-28")
    assert response.status_code == 200
    assert "precos" in response.json()
    
def test_get_precos_data_invalida():
    response = client.get("/precos?data=2026-13-45")
    assert response.status_code == 422
    
    
    