from fastapi import FastAPI  # type: ignore[import-not-found]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/")
def read_api():
    return {"Message": "You're at the root of API route"}
