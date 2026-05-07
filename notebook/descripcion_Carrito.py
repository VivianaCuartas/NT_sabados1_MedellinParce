def describir_carrito(df):
    print("\n DESCRIPCION CARRITOS\n")

    if df.empty:
        print("  No hay carritos disponibles.\n")
        return

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    if "carritoid" in df.columns:
        print("Carritos unicos:")
        print(df["carritoid"].nunique(), "\n")

    if "usuario_id" in df.columns:
        print("Usuarios unicos con carrito:")
        print(df["usuario_id"].nunique(), "\n")

    if "fecha" in df.columns:
        print("Rango de fechas:")
        print(f"  Desde: {df['fecha'].min()}")
        print(f"  Hasta: {df['fecha'].max()}")
