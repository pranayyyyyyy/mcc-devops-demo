from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
def read_root():
    return {"Hello": "World"}


@app.get("/about")
def about():
    return {"msg": "About Us"}