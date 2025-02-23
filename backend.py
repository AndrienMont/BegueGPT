from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
import os

# Initialize FastAPI app
app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production!)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
print("Loading model...")
generator = pipeline("text-generation", model="Khmarigou/Begue")
print("Model loaded successfully.")

# Request model
class TextRequest(BaseModel):
    text: str

# Define API endpoint
@app.post("/generate")
async def generate_text(request: TextRequest):
    try:
        output = generator(request.text, max_length=200, do_sample=True)
        return {"response": output[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve frontend.html
@app.get("/")
async def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend.html")
    return FileResponse(frontend_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
