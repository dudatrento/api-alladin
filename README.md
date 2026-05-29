# API de Preços de Tapetes

Esta é uma API desenvolvida em **FastAPI** que consome dados de um serviço externo de preços de tapetes, enriquecendo-os com informações de data e tratando erros e falhas.

## Funcionalidades
- **Consumo de API Externa:** Integração assíncrona com `httpx`.
- **Validação de Dados:** Uso de tipagem (`date`) para garantir formatos de entrada corretos.
- **Tratamento de erros:** Tratamento de erros de rede (com timeout) e validação de respostas vazias.
- **Documentação:** Interface interativa Swagger disponível automaticamente (recurso nativo do FastAPI).

## Tecnologias Utilizadas
- Python 3.14.4
- FastAPI
- httpx
- uvicorn

## Como rodar o projeto

### Pré-requisitos
- Python instalado em sua máquina.

### Passos
1. Clone este repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente e instale as dependências: `pip install fastapi uvicorn httpx`
4. Inicie a aplicação: `uvicorn main:app --reload`

## Como testar
Após rodar o servidor, acesse a documentação interativa (Swagger) para testar os endpoints: `http://127.0.0.1:8000/docs`
Exemplo de requisição via URL: GET /precos?data=2026-05-28