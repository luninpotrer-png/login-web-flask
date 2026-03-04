import json
from json import JSONDecodeError
import hashlib

def cargar_datos():
    try:
        with open("datos.json", "r") as datos:
            return json.load(datos)
    except (JSONDecodeError,FileNotFoundError):
        return {}

def guardar_datos(datos):
    with open("datos.json", "w") as d:
        return json.dump(datos,d,indent=4)

def hashear(password):
    return hashlib.sha256(password.encode()).hexdigest()