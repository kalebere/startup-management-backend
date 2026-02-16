from fastapi import FastAPI
from app.api.router import router as v1_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"health":"Ok"}

app.include_router(v1_router)

if __name__ == "__main__":
    uvicorn.run(app,port=8000)