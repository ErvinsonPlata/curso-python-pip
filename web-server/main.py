import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
# terminar - uvicorn main(donde esta la app): app(y el nombre de la app) --reload (una bandera que indica que se recarga cada vez que haya un cambio de la app)


@app.get('/')  # decorador - ruta de la web
def get_list():
    return [1, 2, 3]


'''
@app.get('/contact')  # decorador - ruta de la web
def get_list():
    return {'name': 'ErPlaMen'}
'''


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
