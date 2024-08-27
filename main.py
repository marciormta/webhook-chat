from fastapi import FastAPI, Request, HTTPException
import requests

app = FastAPI()

# Defina o token de verificação
VERIFY_TOKEN = "miscrap"

@app.get("/webhook")
async def verify_webhook(request: Request):
    print("Recebido GET do Facebook para verificação")
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Verificação bem-sucedida!")
            return challenge
        else:
            print("Token de verificação inválido")
            raise HTTPException(status_code=403, detail="Token de verificação inválido")

    print("Requisição inválida")
    raise HTTPException(status_code=400, detail="Requisição inválida")

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)
    # Aqui você pode integrar com o CrewAI e gerar a resposta para o usuário
    return {"status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
