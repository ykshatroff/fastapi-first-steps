from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return "Hello World"


@app.get("/hi/{name}")
def hi_name(name: str):
    return f"Hello {name}"
