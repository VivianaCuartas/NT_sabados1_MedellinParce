import pandas as pd


def limpiar_datos(data_frame_sucio):

    # Copia del DF original
    data_frame_limpio = data_frame_sucio.copy()

    # 0. Normalizar nombres de columnas
    data_frame_limpio.columns = data_frame_limpio.columns.str.strip().str.lower()

    # 1. Limpiar columnas de texto
    columnas_texto = [
        "cliente", "nombre", "talla", "color",
        "descripcion", "listaproductos", "productos_ids"
    ]

    for columna in columnas_texto:
        if columna in data_frame_limpio.columns:
            data_frame_limpio[columna] = (
                data_frame_limpio[columna]
                .astype("string")
                .str.strip()
                .str.lower()
            )

    # 2. Limpiar columnas numéricas
    columnas_numericas = [
        "precio", "totalcompra", "cantidad",
        "cantidad_items", "items", "total"
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

    if "cantidad" in data_frame_limpio.columns:
        data_frame_limpio = data_frame_limpio[data_frame_limpio["cantidad"] > 0]

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

    # 4. Eliminar filas con campos obligatorios vacíos
    columnas_obligatorias = ["usuario_id", "numerorden", "precio", "totalcompra"]
    columnas_presentes = [
        col for col in columnas_obligatorias if col in data_frame_limpio.columns
    ]

    if columnas_presentes:
        data_frame_limpio = data_frame_limpio.dropna(subset=columnas_presentes)

    # 5. Eliminar duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
