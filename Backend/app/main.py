from fastapi import FastAPI

app = FastAPI(
    title="FinGuard AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to FinGuard AI 🚀"}

@app.get("/about")
def about():
    return {
        "project": "FinGuard AI",
        "version": "1.0.0",
        "developer": "Manthan"
    }

@app.get("/health")
def health():
    return {
        "status": "Running",
        "server": "Healthy"
    }