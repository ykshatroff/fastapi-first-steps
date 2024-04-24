from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return "Hello World"


@app.get("/hi/{name}")
def hi_name(name: str):
    return f"Hello {name}"


class Todo(BaseModel):
    name: str
    when: str


@app.post("/todos")
def add_todo(todo: Todo):
    return {"name": todo.name, "when": todo.when}
