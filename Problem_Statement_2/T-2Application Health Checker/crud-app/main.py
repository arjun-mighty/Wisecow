from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Hello(BaseModel):
    name: str


@app.get("/")
async def hello():
    return "Hello"


@app.post("/")
async def greet(hello: Hello):
    return f"Hello {hello.name}"
