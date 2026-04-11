from datetime import datetime, timedelta
import random

def simular_ordenes(numeroOrdenes):

    # Datos semilla
    listaClientes = ["Juan", "Maria", "Carlos", "Ana", "Pedro"]

    listaProductosDisponibles = [
        {"nombre": "Camiseta_cuello_redondo", "precio": 2500000},
        {"nombre": "Camiseta_cuello_v", "precio": 2500000},
        {"nombre": "Chompa", "precio": 50000},
        {"nombre": "Buzo", "precio": 120000},
    ]

    fechaInicial = datetime(2026, 1, 1)

    ordenes = []

    for _ in range(numeroOrdenes):

        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 365))

        # Generar lista de productos aleatoria
        listaProductos = []
        for _ in range(random.randint(1, 5)):  # entre 1 y 5 productos
            producto = random.choice(listaProductosDisponibles)
            listaProductos.append(producto)

        orden = {
            "numeroOrden": random.randint(1000, 9999),
            "cliente": random.choice(listaClientes),
            "listaProductos": listaProductos,
            "fecha": fechaSimulada.strftime("%Y/%m/%d")
        }

        ordenes.append(orden)

    return ordenes