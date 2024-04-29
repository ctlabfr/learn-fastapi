from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name": "John",
        "age": 17,
        "special": "Math"
    }
}

class Student(BaseModel):
    name: str
    age: int
    special: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    special: Optional[str] = None


@app.get("/")
def index():
    return {"name": "Doe"}

# Utilisation d'un path parameter
# http://localhost/get-student/1
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="ID de l'etudiant dont vous voulez récupérer les infos") ):
    return students[student_id]

# Utilisation d'un query parameter
# http://localhost/get-by-id?id=1
@app.get("/get-by-id")
def get_student(id: int):
    return students[id]

# Query parameter avec champ optionnel
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}") 
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does'nt exist"}
    
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.special != None:
        students[student_id]["special"] = student.special

    return students[student_id]
        
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}
    