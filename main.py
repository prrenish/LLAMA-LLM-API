from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import ollama
import os
from choma import collection

load_dotenv()

model = "llama3.2"

API_KEY_CREDITS = {os.getenv("API_KEY"): 5}

app = FastAPI()


def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    if credits <= 0:
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")
    return x_api_key

@app.get("/health")
def health():
    return {"response": "Live now..."}

class Document(BaseModel):
    id: str
    content: str

@app.post("/add_document")
def add_document(doc: Document, x_api_key: str = Depends(verify_api_key)):
    # Add the document to the ChromaDB collection
    collection.add(
        documents=[doc.content],
        ids=[doc.id],
        metadatas=[{"source": "user"}]
    )
    return {"message": "Document added successfully."}

@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return {"response": response["message"]["content"]}

@app.post("/generateRag")
def generateRag(prompt: str, x_api_key: str = Depends(verify_api_key)):
    # Retrieve relevant documents from the vector store
    results = collection.query(query_texts=[prompt], n_results=3)
    retrieved_docs = results['documents'][0]
    context = "\n".join(retrieved_docs)

    # Combine the retrieved context with the user's prompt
    augmented_prompt = f"Context:\n{context}\n\nQuestion: {prompt}"

    print("Augmented Prompt:", augmented_prompt)

    # Generate a response using Ollama
    response = ollama.chat(model=model, messages=[{"role": "user", "content": augmented_prompt}])
    API_KEY_CREDITS[x_api_key] -= 1
    return {"response": response["message"]["content"]}
