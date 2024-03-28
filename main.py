from enum import Enum
from fastapi import FastAPI
import requests
import convert

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}

@app.get("/convert/")
async def convert_vtt(url:str):
    content = requests.get(url).text

    return await convert.convert_vtt(content)

