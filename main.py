# Flight booking backend
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Flight Booking API")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Flight Booking API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
