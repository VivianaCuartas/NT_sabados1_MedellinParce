def describir_orden_compra(df):
    print("\n DESCRIPCIÓN ÓRDENES DE COMPRA\n")

    print(f"Filas:    {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Nombres:  {list(df.columns)}\n")

    print("Estadísticas de totales:")
    print(df[["totalcompra"]].describe(), "\n")

    print("Órdenes únicas:")
    print(df["numeroorden"].nunique(), "\n")

    print("Clientes únicos que compraron:")
    print(df["usuario_id"].nunique(), "\n")

    print("Rango de fechas:")
    print(f"  Desde: {df['fecha'].min()}")
    print(f"  Hasta: {df['fecha'].max()}", "\n")

    print("Ingresos por mes:")
    if "fecha" in df.columns:
        df["mes"] = df["fecha"].dt.month
        print(df.groupby("mes")["totalcompra"].sum().apply(
            lambda x: f"${x:,.0f}"
        ), "\n")

    print("Top 5 clientes por gasto total:")
    print(df.groupby("usuario_id")["totalcompra"].sum()
          .sort_values(ascending=False)
          .head(5)
          .apply(lambda x: f"${x:,.0f}"), "\n")
