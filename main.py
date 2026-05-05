from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services import app_logic

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummarizeRequest(BaseModel):
    text: str

class FactCheckRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/summarize")
async def summarize(request_data: SummarizeRequest):
    result = app_logic.summarize(request_data.text)
    return {"message": result}


@app.post("/fact-check")
async def fact_check(request_data: FactCheckRequest):
    result = app_logic.fact_check(request_data.text)
    return {"message": result}