from fastapi import FastAPI, Path
from typing import Optional

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

# Utilisation d'un request parameter
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

