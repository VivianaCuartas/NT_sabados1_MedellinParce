import os
import matplotlib.pyplot as plt


def generar_graficos(df_ordenes, df_productos):

    os.makedirs("graficos", exist_ok=True)

    # 1. INGRESOS POR MES
    if not df_ordenes.empty and "fecha" in df_ordenes.columns:

        df = df_ordenes.copy()
        df["mes"] = df["fecha"].dt.month

        ingresos_mes = df.groupby("mes")["totalcompra"].sum()

        plt.figure()
        ingresos_mes.plot(kind="bar")
        plt.title("Ingresos por mes")
        plt.xlabel("Mes")
        plt.ylabel("Total COP")
        plt.tight_layout()
        plt.savefig("graficos/ingresos_por_mes.png")
        plt.close()
        print("  Guardado: graficos/ingresos_por_mes.png")

    # 2. ORDENES POR MES
    if not df_ordenes.empty and "fecha" in df_ordenes.columns:

        df = df_ordenes.copy()
        df["mes"] = df["fecha"].dt.month

        ordenes_mes = df.groupby("mes")["numeroorden"].count()

        plt.figure()
        ordenes_mes.plot(kind="bar")
        plt.title("Ordenes por mes")
        plt.xlabel("Mes")
        plt.ylabel("Cantidad de ordenes")
        plt.tight_layout()
        plt.savefig("graficos/ordenes_por_mes.png")
        plt.close()
        print("  Guardado: graficos/ordenes_por_mes.png")

    # 3. TOP 10 CLIENTES POR GASTO
    if not df_ordenes.empty and "usuario_id" in df_ordenes.columns:

        top_clientes = (
            df_ordenes.groupby("usuario_id")["totalcompra"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure()
        top_clientes.plot(kind="bar")
        plt.title("Top 10 clientes por gasto")
        plt.xlabel("Cliente")
        plt.ylabel("Total COP")
        plt.tight_layout()
        plt.savefig("graficos/top_clientes.png")
        plt.close()
        print("  Guardado: graficos/top_clientes.png")

    # 4. DISTRIBUCION DE TOTALES POR ORDEN
    if not df_ordenes.empty and "totalcompra" in df_ordenes.columns:

        plt.figure()
        df_ordenes["totalcompra"].plot(kind="hist", bins=20)
        plt.title("Distribucion de totales por orden")
        plt.xlabel("Total COP")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        plt.savefig("graficos/distribucion_totales.png")
        plt.close()
        print("  Guardado: graficos/distribucion_totales.png")

    # 5. PRECIOS DE PRODUCTOS
    if not df_productos.empty and "precio" in df_productos.columns:

        plt.figure()
        plt.bar(df_productos["nombre"], df_productos["precio"])
        plt.title("Precio por producto")
        plt.xlabel("Producto")
        plt.ylabel("Precio COP")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("graficos/precios_productos.png")
        plt.close()
        print("  Guardado: graficos/precios_productos.png")
