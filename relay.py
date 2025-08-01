from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# URL de ton bot local accessible via Ngrok
NGROK_URL = "https://0cfb5b6a3ba8.ngrok-free.app/shopify-webhook"

@app.post("/shopify-webhook")
async def relay_shopify(request: Request):
    try:
        body = await request.body()
        headers = dict(request.headers)

        async with httpx.AsyncClient() as client:
            response = await client.post(
                NGROK_URL,
                content=body,
                headers=headers,
                timeout=10.0
            )

        print(f"✅ Webhook relayed → {NGROK_URL} (status {response.status_code})")
        return {"status": "relayed", "response_status": response.status_code}

    except Exception as e:
        print(f"❌ Erreur pendant le relay : {e}")
        return {"status": "error", "details": str(e)}
