import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return ["Caro", "Kevo", "Missy"]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola, soy Kevo</h1>
        <p1>¡Que chimba!</p1>
    """

def run():
    store.get_categories()

if __name__ == "__main__":
    run()
