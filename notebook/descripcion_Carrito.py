def describir_carrito(df):
    print("\n DESCRIPCIÓN CARRITOS\n")

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    print("Carritos únicos:")
    print(df["carritoid"].nunique(), "\n")

    print("Usuarios únicos con carrito:")
    print(df["usuario_id"].nunique(), "\n")

    if "fecha" in df.columns:
        print("Rango de fechas:")
        print(f"  Desde: {df['fecha'].min()}")
        print(f"  Hasta: {df['fecha'].max()}")
