def describir_carrito(df):
    print("\n DESCRIPCIÓN CARRITO\n")
    
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Columnas: {list(df.columns)}\n")
    
    print("Carritos únicos:")
    print(df['CarritoId'].nunique())
    
    print("Usuarios únicos:")
    print(df['usuario_id'].nunique(), "\n")
    
    print("Fechas:")
    print(df['fecha'].min(), df['fecha'].max())