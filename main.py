from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hola"}

@app.get("/id/{id}")
def ids(id: int):
  return {"id": id}
