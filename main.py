from fastapi import FastAPI

app = FastAPI()


@app.get("/msg")
async def read_item():
    return {"msg": "Hello to Azure"}