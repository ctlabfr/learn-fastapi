# Learn FastAPI
Ce repository est mon repository expérimental pour apprendre fastAPI et garder une trace de cet apprentissage

# Notes d'apprentissage
FastAPI est basé sur le standard [OpenAPI](https://github.com/OAI/OpenAPI-Specification) 


## Comment lancer uvicorn
> uvicorn <filename_wihoutextension>:<variable_fastapi> --reload
example:
> uvicorn myapi:app --reload

## Fastapi auto-documentation
Fastapi auto-génère une documentation de l'api qui est construite: 
http://127.0.0.1:8000/docs (documentation au format [SwaggerUI](https://github.com/swagger-api/swagger-ui))

http://127.0.0.1:8000/redoc (documentation alternative au format [ReDoc](https://gvithub.com/Rebilly/ReDoc))

Il est également possible de tester l'api directement depuis cette URL.

## FastAPI library
Permet d'importer le package fastapi
```python
import fastapi
```

### FastAPI
Pour importer le module FastAPI du package fastapi et initialiser l'application
```python
from fastapi import FastAPI

app = FastAPI() 
```

### Path
Pour importer le module Path du package fastapi
Ce module permet d'ajouter des validations et des metadatas au chemin (path) de l'API
```python
from fastapi import Path

@app.get("/get-student/{student_id}")
def get_student(student_id: int= Path(description="ID de l'etudiant dont vous voulez récupérer les infos") ):
    return students[student_id]

```
## Parametres
### Path Parameter
Dans la création du endpoint ci-dessus, nous avons utiliser un paramètre de chemin

Il s'agit d'un paramètre passé dans le chemin de l'url.

```python
# http://localhost/get-student/1
@app.get("/get-student/{student_id}")
```

### Query Parameter
On peut également utiliser des paramètres de requêtes qui se trouvent alors à la suite du caractère ? dans le chemin de l'url
```python
# http://localhost/get-student?id=1
@app.get("/get-student) 
def get-student(id: int):
    ...
```


## Ressources:
- [x] [Youtube - FastAPI Course for beginners - 1h04](https://youtu.be/tLKKmouUams?si=b8Hgf7fqUbhE0XbF)
- [ ] [Youtube - Python API Development - 19h00](https://youtu.be/0sOvCWFmrtA?si=EbO0u7TVASEVxduf)
- [ ] [Youtube - Microservice with fastAPI - 1h30](https://youtu.be/Cy9fAvsXGZA?si=fBJ85JWpbtO6bjFJ)
- [ ] [Youtube - Event Driven Architecture with React and FastAPI - 1h40](https://youtu.be/NVvIpqmf_Xc?si=1a6kpALnPVv13j5a)

