import pandas as pd
import os

# 🔹 Simulación
from utils.simulacion_Carrito import simular_carrito
from utils.simulacion_CarritoItem import simular_ordenes as simular_carrito_item
from utils.simulacion_OrdenCompra import simular_ordenes as simular_orden_compra
from utils.simulacion_Productos import simular_productos
from utils.simulacion_Usuario import simular_ordenes_con_usuarios

# 🔹 Limpieza
from utils.limpieza import limpiar_datos

# 🔹 Descripción (RESPETANDO TUS NOMBRES)
from utils.descripcion_Carrito import describir_carrito
from utils.descripcion_CarritoItem import describir_carrito_item
from utils.descripcion_OrdenCompra import describir_orden_compra
from utils.descripcion_Productos import describir_productos
from utils.descripcion_Usuario import describir_usuario

# 🔹 Guardado
from utils.guardado_JSON_CSV import guardado_data


print("INICIANDO PROCESO...\n")

# ===============================
# 1. SIMULACIÓN
# ===============================

simulacion_carrito = simular_carrito(20)
simulacion_carrito_item = simular_carrito_item(20)
simulacion_orden_compra = simular_orden_compra(20)
simulacion_productos = simular_productos(20)
simulacion_usuarios = simular_ordenes_con_usuarios(20)

# ===============================
# 2. DATAFRAMES
# ===============================

data_frame_carrito = pd.DataFrame(simulacion_carrito)
data_frame_carrito_item = pd.DataFrame(simulacion_carrito_item)
data_frame_orden_compra = pd.DataFrame(simulacion_orden_compra)
data_frame_productos = pd.DataFrame(simulacion_productos)
data_frame_usuarios = pd.DataFrame(simulacion_usuarios)

# ===============================
# 3. LIMPIEZA
# ===============================

data_frame_carrito_limpio = limpiar_datos(data_frame_carrito)
data_frame_carrito_item_limpio = limpiar_datos(data_frame_carrito_item)
data_frame_orden_compra_limpio = limpiar_datos(data_frame_orden_compra)
data_frame_productos_limpio = limpiar_datos(data_frame_productos)
data_frame_usuarios_limpio = limpiar_datos(data_frame_usuarios)

# ===============================
# 4. DESCRIPCIÓN
# ===============================

describir_carrito(data_frame_carrito_limpio)
describir_carrito_item(data_frame_carrito_item_limpio)
describir_orden_compra(data_frame_orden_compra_limpio)
describir_productos(data_frame_productos_limpio)
describir_usuario(data_frame_usuarios_limpio)

# ===============================
# 5. GUARDADO
# ===============================

guardado_data(data_frame_carrito_limpio, "carrito_limpio", "data")
guardado_data(data_frame_carrito_item_limpio, "carrito_item_limpio", "data")
guardado_data(data_frame_orden_compra_limpio, "orden_compra_limpio", "data")
guardado_data(data_frame_productos_limpio, "productos_limpio", "data")
guardado_data(data_frame_usuarios_limpio, "usuarios_limpio", "data")


print("\nPROCESO FINALIZADO")