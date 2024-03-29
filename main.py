from fastapi import FastAPI

from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_single_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"Error": "Todo not found"}


# Create a new todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"Message": "Todo has been added"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    for item in todos:
        if item.id == todo_id:
            item.id = todo_id
            item.item = todo.item
            return {"Message": "Todo has been updated"}
    return {"Error": "Todo not found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"Message": "Todo has been deleted"}
    return {"Error": "Todo not found"}
