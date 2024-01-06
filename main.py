from fastapi import FastAPI

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

# Create a new todo

# Update a todo

# Delete a todo