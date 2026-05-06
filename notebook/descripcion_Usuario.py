def describir_usuario(df):
    print("\n DESCRIPCIÓN USUARIOS\n")

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    print("Usuarios únicos:")
    print(df["usuario_id"].nunique(), "\n")

    print("Usuarios activos vs inactivos:")
    if "activo" in df.columns:
        print(df["activo"].value_counts(), "\n")

    print("Muestra de clientes:")
    print(df[["usuario_id", "cliente"]].head(10).to_string(index=False))
