"""
api_client.py
Modulo para consumir los datos reales desde la API de Medellin Parce.
Reemplaza los archivos de simulacion anteriores.

Requisitos:
    pip install requests
"""

import requests

BASE_URL = "http://localhost:8080"


def obtener_usuarios():
    """Obtiene todos los usuarios desde la API."""
    res = requests.get(f"{BASE_URL}/usuarios")
    res.raise_for_status()
    datos = res.json()

    usuarios = []
    for u in datos:
        usuarios.append({
            "usuario_id":   u.get("idCliente"),
            "cliente":      u.get("nombreCliente"),
            "correo":       u.get("correoElectronico"),
            "direccion":    u.get("direccionEnvio"),
            "telefono":     u.get("numeroTelefono"),
            "activo":       u.get("activo"),
        })

    return usuarios


def obtener_productos():
    """Obtiene todos los productos desde la API."""
    res = requests.get(f"{BASE_URL}/productos")
    res.raise_for_status()
    datos = res.json()

    productos = []
    for p in datos:
        productos.append({
            "ProductoId":   p.get("idProducto"),
            "nombre":       p.get("nombreProducto"),
            "talla":        p.get("talla"),
            "color":        p.get("color"),
            "precio":       p.get("precio"),
            "descripcion":  p.get("descripcion"),
        })

    return productos


def obtener_ordenes():
    """
    Obtiene todas las ordenes de compra desde la API.
    Expande listaProductos (formato 'PROD001:2,PROD002:1') en columnas separadas.
    """
    res = requests.get(f"{BASE_URL}/ordenCompra")
    res.raise_for_status()
    datos = res.json()

    ordenes = []
    for o in datos:
        lista_str = o.get("listaProductos", "")
        cantidad_total = 0
        productos_ids = []

        if lista_str:
            for item in lista_str.split(","):
                partes = item.strip().split(":")
                productos_ids.append(partes[0])
                if len(partes) == 2:
                    try:
                        cantidad_total += int(partes[1])
                    except ValueError:
                        cantidad_total += 1
                else:
                    cantidad_total += 1

        ordenes.append({
            "numeroOrden":      o.get("idCompra"),
            "usuario_id":       o.get("cliente"),
            "listaProductos":   lista_str,
            "productos_ids":    ",".join(productos_ids),
            "cantidad_items":   cantidad_total,
            "fecha":            o.get("fecha"),
            "TotalCompra":      o.get("total"),
        })

    return ordenes


def obtener_carritos():
    """
    Obtiene todos los carritos desde la API.
    Si el endpoint falla retorna lista vacia para no detener el pipeline.
    """
    try:
        res = requests.get(f"{BASE_URL}/carritos")
        res.raise_for_status()
        datos = res.json()

        carritos = []
        for c in datos:
            carritos.append({
                "CarritoId":    c.get("idCarrito"),
                "usuario_id":   c.get("mUsuario", {}).get("idCliente"),
                "fecha":        c.get("fecha"),
                "items":        c.get("items"),
                "total":        c.get("total"),
            })

        return carritos

    except Exception as e:
        print(f"  ⚠️  No se pudieron obtener carritos: {e}")
        return []


def obtener_carrito_items():
    """
    Obtiene todos los items de carrito desde la API.
    Si el endpoint falla retorna lista vacia para no detener el pipeline.
    """
    try:
        res = requests.get(f"{BASE_URL}/carritoItems")
        res.raise_for_status()
        datos = res.json()

        items = []
        for i in datos:
            items.append({
                "CarritoId":    i.get("id", {}).get("idCarritoFK"),
                "ProductoId":   i.get("id", {}).get("idProductoFK"),
                "Cantidad":     i.get("cantidad"),
            })

        return items

    except Exception as e:
        print(f"  ⚠️  No se pudieron obtener carrito items: {e}")
        return []
