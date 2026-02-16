from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True
)

@app.get("/health")
def health():
    return {"health":"Ok"}

if __name__ == "__main__":
    uvicorn.run(app,port=8000)