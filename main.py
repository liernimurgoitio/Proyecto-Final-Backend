from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.article import article
from routes.publication import publication

app = FastAPI()

app.add_middleware(  # esto es para que las peticiones de distintos origenes sean permitidas
    CORSMiddleware,  # se usa la libreria cors
    # se pone * para que se permitan todas las peticiones de cualquier origen
    allow_origins=["http://localhost:3000"],
    # se pone True para que el usuario pueda utilizar las credenciales
    allow_credentials=True,
    # se pone * para que se permitan todas las peticiones (post, get, delete, put)
    allow_methods=['*'],
    # se pone * para que se permitan todas las cabeceras (cookie, content-type, authorization)
    allow_headers=['*']
)


@app.get('/')
def root():
    return 'Welcome to the API'


app.include_router(article)
app.include_router(publication)


