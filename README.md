# API de Preços de Tapetes

API desenvolvida em **FastAPI** que consome dados de um serviço externo de preços de tapetes, enriquecendo-os com a data da consulta e tratando falhas de rede de forma amigável. 

## Funcionalidades
- **Consumo de API Externa:** Integração assíncrona com `httpx`;
- **Validação de dados:** Tipagem com `date` para garantir o formato correto de entrada;
- **Tratamento de erros:** Cobertura de timeout, erros HTTP e indisponibilidade da API externa;
- **Documentação interativa:** Swagger UI gerado automaticamente pelo FastAPI.

## Tecnologias Utilizadas
- Python 3.13+
- FastAPI
- httpx
- uvicorn
- pytest

## Como rodar o projeto

### Pré-requisitos
- Python 3.13 ou superior
- Git

### Passos
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente e instale as dependências: `pip install -r requirements.txt`
4. Inicie a aplicação: `uvicorn main:app --reload`

## Como usar
Acesse a documentação interativa para explorar e testar os endpoints: `http://127.0.0.1:8000/docs`
Exemplo de requisição direta: GET http://127.0.0.1:8000/precos?data=2026-05-28

## Como rodar os testes
Através dp `pytest test_main.py -v`. 
