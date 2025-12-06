from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"msg": "root ok"}

@app.get("/about")
def about():
    return {"msg": "about ok"}

 