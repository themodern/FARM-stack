from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from . import models

app = FastAPI()
origins = ['https://127.0.0.1:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# return all todo
@app.get("/api/todo")
async def get_todo(todo):
    return 1

# fet by id
@app.get("/api/todo{id}")
async def get_todo_by_id(todo):
    return 1

@app.post("/api/todo")
async def post_todo(todo):
    return 1

# update todo by id
@app.put("/api/todo{id}")
async def update_todo(id, data):
    return 1

# delete by id
@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1