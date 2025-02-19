import pandas as pd
from typing import Optional, Union

def load_file(ruta: str, separador: str = ',', encoding: Optional[str] = None) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame de pandas.

    Parámetros:
    path (str): Ruta del archivo CSV.
    separator (str, opcional): Separador de columnas en el CSV (por defecto `,`).
    encoding (str, opcional): Codificación del archivo (ejemplo: "utf-8", "latin1").

    Retorna:
    pd.DataFrame: DataFrame con los datos cargados.
    """
    return pd.read_csv(ruta, sep=separador, encoding=encoding)
    #"""Carga un archivo en formato CSV, Excel o JSON y lo retorna como un dataframe de Pandas."""
    # try:
    #     # Verifica la extensión del archivo y carga los datos según corresponda
    #     if ruta.endswith('.csv'):
    #         data = pd.read_csv(ruta)  # Carga archivo CSV
    #     elif ruta.endswith('.xlsx') or ruta.endswith('.xls'):
    #         data = pd.read_excel(ruta)  # Carga archivo Excel
    #     elif ruta.endswith('.json'):
    #         data = pd.read_json(ruta)  # Carga archivo JSON
    #     else:
    #         raise ValueError("Archivo no valido")  # Imprime error si la extensión no es soportada
    #     return data  # Retorna los datos cargados como dataframe
    # except Exception as e:
    #     print(f"Error al cargar archivo: {e}")  # Imprime el error si ocurre una excepción
    #     return None  # Retorna None en caso de error

        # Mostrar las filas con datos nulos
    print("Filas con datos nulos:")
    filas_nulas = df[df.isnull().any(axis=1)]
    if filas_nulas.empty:
        print("No hay filas con datos nulos.")
    else:
        print(filas_nulas)
    print("-------------------------")