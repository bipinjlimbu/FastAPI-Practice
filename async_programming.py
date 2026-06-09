from fastapi import FastAPI, Depends
import asyncio

app = FastAPI()

async def fetch_data():
    await asyncio.sleep(2)
    return {"data": "This is the fetched data"}

@app.get("/data")
async def get_data(data: dict = Depends(fetch_data)):
    return data