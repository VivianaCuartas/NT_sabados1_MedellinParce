import requests

BASE_URL = "http://localhost:8080"


def obtener_usuarios():
    #Obtener usuarios desde la API
    res = requests.get(f"{BASE_URL}/usuarios")
    res.raise_for_status()
    datos = res.json()

    usuarios = []
    for u in datos:
        usuarios.append({
            "usuario_id":       u.get("idCliente"),
            "cliente":          u.get("nombreCliente"),
            "correo":           u.get("correoElectronico"),
            "direccion":        u.get("direccionEnvio"),
            "telefono":         u.get("numeroTelefono"),
            "activo":           u.get("activo"),
        })

    return usuarios


def obtener_productos():
    #Obtener productos desde la API
    res = requests.get(f"{BASE_URL}/productos")
    res.raise_for_status()
    datos = res.json()

    productos = []
    for p in datos:
        productos.append({
            "ProductoId":       p.get("idProducto"),
            "nombre":           p.get("nombreProducto"),
            "talla":            p.get("talla"),
            "color":            p.get("color"),
            "precio":           p.get("precio"),
            "descripcion":      p.get("descripcion"),
        })

    return productos


def obtener_ordenes():

    #Obtiene todas las órdenes de compra desde la API. Y separa los datos
    
    res = requests.get(f"{BASE_URL}/ordenCompra")
    res.raise_for_status()
    datos = res.json()

    ordenes = []
    for o in datos:
        # Calcular cantidad total de items desde listaProductos
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
    #Obtiene todos los carritos desde la API
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


def obtener_carrito_items():
    #Obtiene todos los items de carrito desde la API.
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
