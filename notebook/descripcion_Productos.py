def describir_productos(df):
    print("\n DESCRIPCIÓN PRODUCTOS\n")

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    print("Estadísticas de precios:")
    print(df[["precio"]].describe(), "\n")

    print("Productos disponibles:")
    print(df[["productoid", "nombre", "talla", "color", "precio"]].to_string(index=False), "\n")

    print(f"Productos únicos: {df['productoid'].nunique()}")
