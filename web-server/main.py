# Python para Backend: web server con FastAPI

"""
Python para Backend: web server con FastAPI
cd web-server
source env/bin/activate
pip3 install fastapi                    instalar fastapi (libreria)
pip3 install "uvicorn[standard]"        instalar uvicorn (servidor)
pip3 freeze
pip3 freeze > requirements.txt          actualizar arcchivo de dependencias
code .                                  modificamos el main.py

uvicorn main:app --reload               ejecutamos el servidor uvicorn (8000)
uvicorn main:app --reload --port 8080   para ejecutar el servidor uvicorn en otro puerto
http://localhost:8000                   ahora ya podemos ver en el navegador
http://localhost:8000/contact           podemos ver en el navegador
http://127.0.0.1:8000                   ya podemos ver en el navegador
http://127.0.0.1:8000/contact           podemos ver en el navegador
"""

import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()
