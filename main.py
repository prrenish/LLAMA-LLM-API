from fastapi import FastAPI, Depends, HTTPException, Header
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

model = "llama3.2"

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}
print(API_KEY_CREDITS)
app = FastAPI()

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")

    return x_api_key

@app.get("/health")
def health():
    return {"response": "Live now..."}

@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}
