def describir_productos(df):
    print("\n DESCRIPCIÓN PRODUCTOS\n")
    
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Columnas: {list(df.columns)}\n")
    
    print("Estadísticas:")
    print(df[['precio']].describe(), "\n")
    
    print("Productos:")
    print(df['nombre'].value_counts(), "\n")
    
    print(f"Productos únicos: {df['ProductoId'].nunique()}")