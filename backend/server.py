from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import Agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = Agent()

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: Query):
    result = agent.execute(query.message)

    return {
        "response": result
    }