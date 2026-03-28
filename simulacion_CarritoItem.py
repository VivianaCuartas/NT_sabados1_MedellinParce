from datetime import datetime, timedelta
import random

def simular_ordenes(numeroItem):
    listaProductosDisponibles = [
        {"id": 101, "nombre": "Camiseta_cuello_redondo", "precio": 25000},
        {"id": 102, "nombre": "Camiseta_cuello_v", "precio": 25000},
        {"id": 103, "nombre": "Chompa", "precio": 50000},
        {"id": 104, "nombre": "Buzo", "precio": 120000},
    ]

    fechaInicial = datetime(2026, 1, 1)
    ordenes = []

    for _ in range(numeroItem):
       
        productoAleatorio = random.choice(listaProductosDisponibles)
        cantidad = random.randint(1, 5)
        
      
        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 365))

        ordenCarrito = {
            "CarritoId": random.randint(1000, 9999),
            "ProductoId": productoAleatorio["id"],
            "NombreProducto": productoAleatorio["nombre"],
            "Cantidad": cantidad,
            "PrecioUnitario": productoAleatorio["precio"],
            "Total": productoAleatorio["precio"] * cantidad,
            "Fecha": fechaSimulada.strftime("%Y-%m-%d")
        }

        ordenes.append(ordenCarrito)

    return ordenes

# print(simular_ordenes(3))