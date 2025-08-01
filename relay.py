from fastapi import FastAPI, Request
import httpx

app = FastAPI()

NGROK_URL = "https://0cfb5b6a3ba8.ngrok-free.app"  # ✅ ton tunnel local

@app.post("/shopify-webhook")
async def relay_shopify(request: Request):
    body = await request.body()
    headers = dict(request.headers)

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{NGROK_URL}/shopify-webhook",
            content=body,
            headers=headers,
            timeout=10.0
        )
    return {"status": "relayed", "to": NGROK_URL}
