def describir_carrito_item(df):
    print("\n DESCRIPCION CARRITO ITEMS\n")

    if df.empty:
        print("  No hay items de carrito disponibles.\n")
        return

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    if "cantidad" in df.columns:
        print("Estadisticas de cantidades:")
        print(df[["cantidad"]].describe(), "\n")

    if "productoid" in df.columns:
        print("Productos mas agregados al carrito:")
        print(df["productoid"].value_counts(), "\n")

    if "carritoid" in df.columns:
        print(f"Carritos unicos: {df['carritoid'].nunique()}")

    if "productoid" in df.columns:
        print(f"Productos unicos: {df['productoid'].nunique()}")
