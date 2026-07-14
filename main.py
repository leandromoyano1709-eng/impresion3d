from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

productos = {
    "pelota": {
        "nombre": "Pelota",
        "precio": "$8.000",
        "descripcion": "Mate impreso en 3D apto para agua caliente.",
        "medidas": "12cm x 8cm",
        "material": "PLA",
        "imagen": "pelota.png"
    },
    "matestich": {
        "nombre": "Stich",
        "precio": "$7.000",
        "descripcion": "Mate impreso en 3D apto para agua caliente.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "matestich.png"
    },
    "toystore": {
        "nombre": "Marcianitos",
        "precio": "$7.000",
        "descripcion": "Mate impreso en 3D apto para agua caliente.",
        "medidas": "9cm x 8cm",
        "material": "PLA",
        "imagen": "toystore.png"
    },
    "fernet": {
        "nombre": "Fernet",
        "precio": "$9.000",
        "descripcion": "Juego de Mate impreso en 3D apto para agua caliente.",
        "medidas": "11cm x 8cm",
        "material": "PLA",
        "imagen": "fernet.png"
    },
    "micky": {
        "nombre": "Mickey Mouse",
        "precio": "$8.000",
        "descripcion": "Taza mano de micky.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "micky.png"
    },
    "stich": {
        "nombre": "Stich",
        "precio": "$8.000",
        "descripcion": "Taza stich.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "stich.png"
    },
    "stichnovia": {
        "nombre": "Angela",
        "precio": "$8.000",
        "descripcion": "Taza Angela.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "stichnovia.png"
    },
    "unpocoderuido": {
        "nombre": "Jarra Un Poco De Ruido",
        "precio": "$15.000",
        "descripcion": "Jarra impresa en 3D con vaso de aluminio.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "unpocoderuido.png"
    },
    "goku": {
        "nombre": "Goku",
        "precio": "$8.000",
        "descripcion": "Muñeco goku articulado.",
        "medidas": "13cm x 8cm",
        "material": "PLA",
        "imagen": "goku.png"
    },
    "gohan": {
        "nombre": "Gohan",
        "precio": "$8.000",
        "descripcion": "Muñeco gohan articulado.",
        "medidas": "12cm x 8cm",
        "material": "PLA",
        "imagen": "gohan.png"
    },
    "trunks": {
        "nombre": "Trunks",
        "precio": "$8.000",
        "descripcion": "Muñeco trunks articulado.",
        "medidas": "10cm x 8cm",
        "material": "PLA",
        "imagen": "trunks.png"
    },
    "pokemon": {
        "nombre": "Mewtwo",
        "precio": "$8.000",
        "descripcion": "Muñeco mewtwo con base.",
        "medidas": "15cm x 8cm",
        "material": "PLA",
        "imagen": "pokemon.png"
    },
}

productos_lista = [
    {"id": 1, "nombre": "Prototipado rápido", "material": "PLA / PETG / ABS", "precio": 5000},
    {"id": 2, "nombre": "Piezas personalizadas", "material": "Diseño a medida", "precio": 8000},
    {"id": 3, "nombre": "Figuras decorativas", "material": "Alta resolución", "precio": 3500},
]

@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"productos": productos_lista}
    )

@app.get("/catalogo")
def catalogo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="catalogo.html",
        context={}
    )

@app.get("/producto/{nombre}")
def producto(request: Request, nombre: str):
    prod = productos.get(nombre)
    return templates.TemplateResponse(
        request=request,
        name="producto.html",
        context={"producto": prod, "nombre": nombre}
    )


@app.get("/carrito")
def carrito_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="carrito.html",
        context={}
    )