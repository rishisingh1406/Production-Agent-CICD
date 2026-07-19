from fastapi import FastAPI

app = FastAPI(
    title="Production Agent API"
)

@app.get("/")
def root():
    return {
        "status": "healthy",
        "message": "Production Agent Running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }