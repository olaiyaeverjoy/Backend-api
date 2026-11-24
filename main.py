from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hi This is actually super easy to create"}


@app.post("/initializepayment")
def home():
    return {"message": "initialization completed"}


@app.put("/verifypayment")
def home():
    return {"message": "initialization completed"}


@app.delete("/allpayment")
def home():
    return {"message": "initialization completed"}
