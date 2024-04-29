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
import fastapi

## FastAPI

```python
from fastapi import FastAPI

app = FastAPI() 
```

## Path
```python
from fastapi import Path

```


