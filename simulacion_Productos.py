from datetime import datetime, timedelta
import random

def simular_productos(numeroProductos):

    # Datos semilla
    listaNombres = ["Camiseta_cuello_redondo", "Camiseta_cuello_v", "Chompa", "Buzo"]
    listaTallas = ["XS","S", "M", "L", "XL","XXL","XXXL"]
    listaColores = ["Rojo", "Azul", "Negro", "Blanco","Verde","Amarillo"]

    productos = []

    for _ in range(numeroProductos):
        producto = {
            "id": random.randint(0, 9999),
            "nombre": random.choice(listaNombres),
            "talla": random.choice(listaTallas),
            "color":random.choice(listaColores),
            "precio":random.randint(45000, 150000)
        }
        productos.append(producto)
    return productos