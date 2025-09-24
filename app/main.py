from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.request import CareerQuery
from app.agent.career_agent import run_career_agent
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
@app.get("/")
def root():
    return {"message": "Runing....."}

@app.post("/suggest")
def suggest_career(query:CareerQuery):
    result=run_career_agent(query.interest)
    return result
    