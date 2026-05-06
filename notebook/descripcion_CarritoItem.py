def describir_carrito_item(df):
    print("\n DESCRIPCIÓN CARRITO ITEMS\n")

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    print("Estadísticas de cantidades:")
    print(df[["cantidad"]].describe(), "\n")

    print("Productos más agregados al carrito:")
    print(df["productoid"].value_counts(), "\n")

    print(f"Carritos únicos: {df['carritoid'].nunique()}")
    print(f"Productos únicos: {df['productoid'].nunique()}")
