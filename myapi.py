from fastapi import FastAPI

app = FastAPI()

students = {
    1:{
        "name": "John",
        "age": 17,
        "class": "Math"
    }
}

@app.get("/")
def index():
    return {"name": "Doe"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]