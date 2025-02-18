import pandas as pd

def load_file(ruta):
    """Carga un archivo en formato CSV, Excel o JSON dependiendo de su extension y lo retorna como un dataframe de Pandas."""
    try:
        # Verifica la extensión del archivo y carga los datos según corresponda
        if ruta.endswith('.csv'):
            data = pd.read_csv(ruta)  # Carga archivo CSV
        elif ruta.endswith('.xlsx') or ruta.endswith('.xls'):
            data = pd.read_excel(ruta)  # Carga archivo Excel
        elif ruta.endswith('.json'):
            data = pd.read_json(ruta)  # Carga archivo JSON
        else:
            raise ValueError("Archivo no valido")  # Imprime error si la extensión no es soportada
        return data  # Retorna los datos cargados como dataframe
    except Exception as e:
        print(f"Error al cargar archivo: {e}")  # Imprime el error si ocurre una excepción
        return None  # Retorna None en caso de error
    