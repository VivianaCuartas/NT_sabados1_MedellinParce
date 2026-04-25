import pandas as pd

def limpiar_datos(data_frame_sucio):
    
    # Copia del DF original
    data_frame_limpio = data_frame_sucio.copy()
    
    # 0. Normalizar nombres de columnas
    data_frame_limpio.columns = data_frame_limpio.columns.str.strip().str.lower()
    
    # 1. Limpiar columnas de texto (si existen)
    columnas_texto = ["nombreproducto", "cliente", "listaproductos", "talla", "color", "nombre"]
    
    for columna in columnas_texto:
        if columna in data_frame_limpio.columns:
            data_frame_limpio[columna] = (
                data_frame_limpio[columna]
                .astype("string")
                .str.strip()
                .str.lower()
            )
    
    # 1.1 Validar valores esperados
    valores_validos = [
        "camiseta_cuello_redondo",
        "camiseta_cuello_v",
        "chompa",
        "buzo"
    ]
    
    if "listaproductos" in data_frame_limpio.columns:
        data_frame_limpio["listaproductos"] = data_frame_limpio["listaproductos"].where(
            data_frame_limpio["listaproductos"].isin(valores_validos),
            pd.NA
        )
    
    if "nombreproducto" in data_frame_limpio.columns:
        data_frame_limpio["nombreproducto"] = data_frame_limpio["nombreproducto"].where(
            data_frame_limpio["nombreproducto"].isin(valores_validos),
            pd.NA
        )
    
    # 2. Limpiar columnas numéricas (si existen)
    columnas_numericas = [
        "carritoid", "cantidad", "preciounitario", "total",
        "totalcompra", "productoid", "usuario_id",
        "numeroorden", "precio"
    ]
    
    for columna in columnas_numericas:
        if columna in data_frame_limpio.columns:
            data_frame_limpio[columna] = pd.to_numeric(
                data_frame_limpio[columna],
                errors="coerce"
            )
    
    # 2.1 Validaciones de negocio
    if "precio" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["precio"] >= 1000]
    
    if "productoid" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["productoid"] > 0]
    
    if "cantidad" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]
    
    if "total" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["total"] > 0]
    
    if "totalcompra" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["totalcompra"] > 0]
    
    # 3. Manejo de fechas
    if "fecha" in data_frame_limpio.columns:
        data_frame_limpio["fecha"] = pd.to_datetime(
            data_frame_limpio["fecha"],
            errors="coerce"
        )
        
        fecha_default = pd.to_datetime("2026-01-01")
        data_frame_limpio["fecha"] = data_frame_limpio["fecha"].fillna(fecha_default)
    
    # 4. Eliminar registros con datos obligatorios (solo si existen)
    columnas_obligatorias = ["nombreproducto", "numeroorden", "precio", "usuario_id"]
    
    columnas_presentes = [
        col for col in columnas_obligatorias if col in data_frame_limpio.columns
    ]
    
    if columnas_presentes:
        data_frame_limpio = data_frame_limpio.dropna(subset=columnas_presentes)
    
    # 5. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio