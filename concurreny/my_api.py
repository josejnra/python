from fastapi import FastAPI

app = FastAPI()


@app.get("/page-1")
def page1():
    return {"message": "page-1"}


@app.get("/page-2")
def page2():
    return {"message": "page-2"}


# uvicorn my_api:app --host 0.0.0.0 --port 8000 --reload
