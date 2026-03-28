from datetime import datetime, timedelta
import random
import string

def generar_password_vacia(longitud=8):
 
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def simular_ordenes_con_usuarios(numeroItem):
    
    listaProductosDisponibles = [
        {"id": 101, "nombre": "Camiseta_cuello_redondo", "precio": 25000},
        {"id": 102, "nombre": "Camiseta_cuello_v", "precio": 25000},
        {"id": 103, "nombre": "Chompa", "precio": 50000},
        {"id": 104, "nombre": "Buzo", "precio": 120000},
    ]

    # 2. Datos de usuarios simulados
    usuarios = [
        {"id": 1, "nombre": "Juan Perez", "telefono": "3001234567", "direccion": "Calle 10 #25-10"},
        {"id": 2, "nombre": "Maria Lopez", "telefono": "3109876543", "direccion": "Carrera 45 #12-30"},
        {"id": 3, "nombre": "Carlos Ruiz", "telefono": "3205554433", "direccion": "Avenida Siempre Viva 123"},
        {"id": 4, "nombre": "Ana Gomez", "telefono": "3152228899", "direccion": "Circular 4 #70-15"},
    ]

    fechaInicial = datetime(2026, 1, 1)
    ordenes = []

    for _ in range(numeroItem):
        # Seleccionar un usuario y un producto al azar
        usuario = random.choice(usuarios)
        producto = random.choice(listaProductosDisponibles)
        cantidad = random.randint(1, 3)
        
       
        fechaSimulada = fechaInicial + timedelta(days=random.randint(0, 365))

       
        ordenCompleta = {
            "CarritoId": random.randint(1000, 9999),
            "Fecha": fechaSimulada.strftime("%Y-%m-%d"),
        
            "UsuarioId": usuario["id"],
            "NombreCliente": usuario["nombre"],
            "Telefono": usuario["telefono"],
            "DireccionEnvio": usuario["direccion"],
            "PasswordAcceso": generar_password_vacia(), # Simulación de contraseña
         
            "ProductoId": producto["id"],
            "NombreProducto": producto["nombre"],
            "Cantidad": cantidad,
            "PrecioUnitario": producto["precio"],
            "TotalCompra": producto["precio"] * cantidad
        }

        ordenes.append(ordenCompleta)

    return ordenes

