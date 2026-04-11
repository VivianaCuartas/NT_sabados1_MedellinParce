from datetime import datetime, timedelta
import random


def simular_carrito(numero_carritos):
    carritos = []

    for _ in range(numero_carritos):
        carrito={
            "id": random.randint(0, 9999),
            "usuario_id": random.randint(0, 9999),
            "total": random.randint(45000, 150000),
        }
        carritos.append(carrito)
    return carritos

