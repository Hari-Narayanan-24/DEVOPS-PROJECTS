from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

greetings = [
    "Hello",
    "Hi there",
    "Bonjour",
    "Hey ",
    "Greetings"
]

@app.get("/greet/{name}")
def greet(name: str):
    greeting = random.choice(greetings)
    print(f"Route /greet/{name} Success Return Data !!! ---- message:{greeting}, {name}!")
    return {"message": f"{greeting}, {name}!"}
