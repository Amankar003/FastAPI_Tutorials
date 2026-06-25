from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"Message": "Hello WORLD"}

@app.get("/greet")
def greet():
    return{"Message": "Hello Aman"}

## Path Parameters
@app.get("/greet/{name}")
def greet_name(name: str):
    return {"message": f"Hello {name}"}


## Query Parameter
@app.get("/greets/{name}")
def greet_name(name:str, age: Optional[int] = None):
    return {"Message": f"Hello {name} and you are {age} years old"}

#---------------------------------------------------------------
#----- HTTP Methods ----------------------------------------------

# 1. Post request

class Student(BaseModel):
    name: str
    age: int
    roll: int

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll

    }