import pandas as pd



def limpiar_datos(data_frame_sucio):
    data_frame_limpio=data_frame_sucio.copy()
    
    #1. Limpiar las columnas String del DF
    columnas_texto=["NombreProducto","cliente","listaProductos","talla","color"]
    for columna in columnas_texto:
        data_frame_limpio[columna]=data_frame_limpio[columna].astype("string").str.strip().str.lower()
        
    #1.1 Definir valores de string esperados 
    valores_validos_CarritoItem=["Camiseta_cuello_redondo","Camiseta_cuello_v","Chompa","Buzo"]
    data_frame_limpio["listaProductos"]=data_frame_limpio["listaProductos"].where(
        data_frame_limpio["listaProductos"].isin(valores_validos_CarritoItem),
        pd.NA
    )
    
    #2. Limpiar las columnas numericas del DF
    data_frame_limpio["CarritoId"]=pd.to_numeric(data_frame_limpio["CarritoId"])
    data_frame_limpio["Cantidad"]=pd.to_numeric(data_frame_limpio["Cantidad"])
    data_frame_limpio["PrecioUnitario"]=pd.to_numeric(data_frame_limpio["PrecioUnitario"])
    data_frame_limpio["Total"]=pd.to_numeric(data_frame_limpio["Total"])
    data_frame_limpio["TotalCompra"]=pd.to_numeric(data_frame_limpio["Total"])
    data_frame_limpio["ProductoId"]=pd.to_numeric(data_frame_limpio["ProductoId"])
    data_frame_limpio["usuario_id"]=pd.to_numeric(data_frame_limpio["usuario_id"])
    data_frame_limpio["numeroOrden"]=pd.to_numeric(data_frame_limpio["numeroOrden"])
    data_frame_limpio["precio"]=pd.to_numeric(data_frame_limpio["precio"])
    
    #2.1 Limpiando campos numericos que no tengan valores validos
    data_frame_limpio=data_frame_limpio[data_frame_limpio["precio"]>=1000]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["ProductoId"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["Cantidad"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["Total"]>0]
    data_frame_limpio=data_frame_limpio[data_frame_limpio["TotalCompra"]>0]
    
    #3. Organizar las columnas de tipo fecha
    data_frame_limpio["fecha"]=pd.to_datetime(data_frame_limpio["fecha"])
    
    #3.1 si una fecha no viene la reemplazamos por un valor  por defecto
    fecha_default=pd.to_datetime("2026-01-01")
    data_frame_limpio["fecha"]=data_frame_limpio["fecha"].fillna(fecha_default)
    
    
    #4 Eliminar registro que tenga datos obligatorios vacios 
    columna_obligatorias=["NombreProducto","numeroOrden","precio","usuario_id"]
    data_frame_limpio=data_frame_limpio.dropna(subset=columna_obligatorias)
    
    #5 Eliminar registros duplicados
    data_frame_limpio=data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio


    