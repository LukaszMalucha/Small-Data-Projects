from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
async def home_api():
    return {"message": "OK"}