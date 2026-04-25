def describir_usuario(df):
    print("\n DESCRIPCIÓN USUARIO\n")
    
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print(f"Columnas: {list(df.columns)}\n")
    
    print("Estadísticas:")
    print(df[['usuario_id']].describe(), "\n")
    
    print("Clientes:")
    print(df['cliente'].value_counts(), "\n")
    
    print("Fechas:")
    print(df['fecha'].min(), df['fecha'].max())