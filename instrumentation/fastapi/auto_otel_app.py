from fastapi import FastAPI

app = FastAPI()


def sum(val1: int, val2: int):
    return val1 + val2


@app.get("/sum")
async def foobar(val1: int, val2: int):
    return {
        "sum": sum(val1, val2)
    }
