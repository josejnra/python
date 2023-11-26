from fastapi import FastAPI

from logger import logger

app = FastAPI()


@app.get("/page-1")
async def page1():
    logger.info("processing page - 1")
    return {"message": "page-1"}


@app.get("/page-2")
async def page2():
    logger.info("processing page - 2")
    return {"message": "page-2"}


# uvicorn my_api:app --host 0.0.0.0 --port 8000 --reload
