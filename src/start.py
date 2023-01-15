from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Access home

    Returns:
        json: {message:String}
    """
    return {"message": "Tomato"}
