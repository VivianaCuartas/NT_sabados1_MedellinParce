def describir_orden_compra(df):
    print("\n DESCRIPCIÓN ORDEN DE COMPRA\n")
    
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Columnas: {list(df.columns)}\n")
    
    print("Estadísticas:")
    print(df[['TotalCompra']].describe(), "\n")
    
    print("Órdenes únicas:")
    print(df['numeroOrden'].nunique())
    
    print("Usuarios únicos:")
    print(df['usuario_id'].nunique(), "\n")
    
    print("Fechas:")
    print(df['fecha'].min(), df['fecha'].max())