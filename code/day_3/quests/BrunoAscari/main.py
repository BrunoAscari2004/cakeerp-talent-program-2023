from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"Hello World"}


@app.get("/status/")
async def read_status():
    return {"status":"it's alive"}