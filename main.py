import pandas as pd

# Datos desde la API
from utils.api_client import obtener_usuarios
from utils.api_client import obtener_productos
from utils.api_client import obtener_ordenes
from utils.api_client import obtener_carritos
from utils.api_client import obtener_carrito_items

# Limpieza
from utils.limpieza import limpiar_datos

# Descripcion
from notebook.descripcion_Carrito import describir_carrito
from notebook.descripcion_CarritoItem import describir_carrito_item
from notebook.descripcion_OrdenCompra import describir_orden_compra
from notebook.descripcion_Productos import describir_productos
from notebook.descripcion_Usuario import describir_usuario

# Guardado
from utils.guardado_JSON_CSV import guardado_data

# Analitica
from utils.analitica import generar_graficos


# 1. OBTENER DATOS DESDE LA API

print("Conectando con la API...")

data_usuarios = obtener_usuarios()
data_productos = obtener_productos()
data_ordenes = obtener_ordenes()
data_carritos = obtener_carritos()
data_carrito_items = obtener_carrito_items()

print(f"  Usuarios: {len(data_usuarios)}")
print(f"  Productos: {len(data_productos)}")
print(f"  Ordenes: {len(data_ordenes)}")
print(f"  Carritos: {len(data_carritos)}")
print(f"  Carrito Items: {len(data_carrito_items)}")


# 2. CREAR DATAFRAMES

df_usuarios = pd.DataFrame(data_usuarios)
df_productos = pd.DataFrame(data_productos)
df_ordenes = pd.DataFrame(data_ordenes)
df_carritos = pd.DataFrame(data_carritos)
df_carrito_items = pd.DataFrame(data_carrito_items)


# 3. LIMPIEZA

df_usuarios_limpio = limpiar_datos(df_usuarios)
df_productos_limpio = limpiar_datos(df_productos)
df_ordenes_limpio = limpiar_datos(df_ordenes)
df_carritos_limpio = limpiar_datos(df_carritos)
df_carrito_items_limpio = limpiar_datos(df_carrito_items)


# 4. DESCRIPCION

describir_usuario(df_usuarios_limpio)
describir_productos(df_productos_limpio)
describir_orden_compra(df_ordenes_limpio)
describir_carrito(df_carritos_limpio)
describir_carrito_item(df_carrito_items_limpio)


# 5. GUARDADO

guardado_data(df_usuarios_limpio, "usuarios", "data")
guardado_data(df_productos_limpio, "productos", "data")
guardado_data(df_ordenes_limpio, "ordenes", "data")
guardado_data(df_carritos_limpio, "carritos", "data")
guardado_data(df_carrito_items_limpio, "carrito_items", "data")


# 6. GRAFICOS

print("\nGenerando graficos...")
generar_graficos(df_ordenes_limpio, df_productos_limpio)


print("\nTerminado!")
