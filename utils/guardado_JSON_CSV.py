import os

def guardado_data(df, nombre_archivo, carpeta="data"):

    os.makedirs(carpeta, exist_ok=True)

    base = nombre_archivo.replace(".csv", "").replace(".json", "")
    ruta_base = os.path.join(carpeta, base)

    df.to_csv(f"{ruta_base}.csv", index=False)
    df.to_json(f"{ruta_base}.json", orient="records", lines=True, force_ascii=False)