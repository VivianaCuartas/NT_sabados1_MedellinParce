import pandas as pd
from utils.simulacion_Carrito import simular_carrito
from utils.simulacion_CarritoItem import simular_ordenes
from utils.simulacion_OrdenCompra import simular_ordenes
from utils.simulacion_Productos import simular_productos
from utils.simulacion_Usuario import simular_ordenes_con_usuarios
from utils.guardado_JSON_CSV import guardado_data
import os



simulaciones_carrito = simular_carrito(20)
simulaciones_carrito_item = simular_ordenes(20)
simulaciones_orden = simular_ordenes(20)
simulaciones_productos = simular_productos(20)
simulaciones_usuarios = simular_ordenes_con_usuarios(20)

df_simulaciones_carrito = pd.DataFrame(simulaciones_carrito)
df_simulaciones_carrito_item = pd.DataFrame(simulaciones_carrito_item)
df_simulaciones_orden = pd.DataFrame(simulaciones_orden)
df_simulaciones_productos = pd.DataFrame(simulaciones_productos)
df_simulaciones_usuarios = pd.DataFrame(simulaciones_usuarios) 


guardado_data(df_simulaciones_carrito, "simulacion_carrito","data")
guardado_data(df_simulaciones_carrito_item, "simulacion_carrito_item","data")
guardado_data(df_simulaciones_orden, "simulacion_orden","data")
guardado_data(df_simulaciones_productos, "simulacion_productos","data")
guardado_data(df_simulaciones_usuarios, "simulacion_usuarios","data")