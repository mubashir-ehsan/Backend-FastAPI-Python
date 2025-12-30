from fastapi import FastAPI
import uvicorn 
app = FastAPI()
@app.get("/gettodos")
def getTodos():
    print("GetTodos Called")
    return"todos called"

@app.post("/gettodos")
def getTodosPost():
    print("PostTodos Called")
    return"Post todos called"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Single Todo Called")
    return"Single Todo Called here"
def start():
    uvicorn.run(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    start()