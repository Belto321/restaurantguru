import os
import json
import pandas as pd
import re

def process_metadata_files(input_dir, output_file):
    """
    Procesa archivos JSON de metadatos para extraer información de restaurantes.

    Args:
        input_dir (str): Ruta de la carpeta que contiene los archivos JSON.
        output_file (str): Ruta del archivo de salida en formato Parquet.

    Returns:
        None: Genera un archivo .parquet con los datos procesados.
    """

    # Inicializamos una lista para almacenar los datos procesados
    processed_data = []

    # Función para extraer componentes de la dirección
    def extract_address_components(address, name):
        try:
            # Eliminar el nombre del lugar de la dirección
            address = address.replace(name + ", ", "")
            # Extraer partes de la dirección usando una expresión regular
            match = re.match(r"^(.*),\s*(.*),\s*(\w{2})\s*(\d{5})$", address)
            if match:
                street, city, state, postal_code = match.groups()
                return street, city, state, postal_code
        except Exception:
            pass
        return None, None, None, None

    # Función para leer archivos .json con manejo de errores
    def load_json_file(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)  # Intentar cargar como un único JSON
            except json.JSONDecodeError:
                # Intentar cargar línea por línea si el JSON está separado
                f.seek(0)  # Reiniciar el cursor del archivo
                return [json.loads(line) for line in f if line.strip()]  # Cargar línea por línea

    # Recorremos todos los archivos .json en la carpeta
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(input_dir, file_name)
            raw_data = load_json_file(file_path)

            # Verificar si raw_data es una lista o un diccionario
            if isinstance(raw_data, dict):
                raw_data = [raw_data]  # Convertir a lista si es un único diccionario

            for data in raw_data:
                # Filtrar por categorías que incluyan la palabra "restaurant"
                categories = data.get("category", [])
                if categories is None:
                    categories = []  # Convertimos None a una lista vacía

                if any("restaurant" in category.lower() for category in categories):
                    # Extraer componentes de la dirección
                    street, city, state, postal_code = extract_address_components(data.get("address", ""), data.get("name", ""))

                    # Agregar datos procesados a la lista
                    processed_data.append({
                        "gmap_id": data.get("gmap_id"),
                        "name": data.get("name"),
                        "address": street,
                        "city": city,
                        "state": state,
                        "postal_code": postal_code,
                        "latitude": data.get("latitude"),
                        "longitude": data.get("longitude"),
                        "stars": data.get("avg_rating"),
                        "review_count": data.get("num_of_reviews"),
                        "categories": categories,
                        "hours": data.get("hours")
                    })

    # Convertimos la lista de datos procesados en un DataFrame
    df = pd.DataFrame(processed_data)

    # Exportamos el DataFrame a un archivo .parquet
    df.to_parquet(output_file, index=False)
    print(f"Archivo exportado exitosamente en {output_file}")

def clean_and_merge_reviews(folder_path, output_folder, gmap_id_list):
    # Crear carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Iterar sobre las carpetas (estados)
    for state_folder in os.listdir(folder_path):
        state_path = os.path.join(folder_path, state_folder)
        if os.path.isdir(state_path) and state_folder.startswith("review-"):
            
            state_name = state_folder.replace("review-", "")

            state_data = []

            # Iterar sobre los archivos JSON dentro de cada carpeta de estado
            for file_name in os.listdir(state_path):
                if file_name.endswith(".json"):
                    file_path = os.path.join(state_path, file_name)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        try:
                            for line in f:  # Leer línea por línea para manejar JSON con múltiples objetos
                                state_data.append(json.loads(line))
                        except json.JSONDecodeError:
                            print(f"Error al decodificar el archivo: {file_path}")

            # Crear un DataFrame para los datos de este estado
            state_df = pd.DataFrame(state_data)

            # Filtrar por gmap_id
            state_df = state_df[state_df['gmap_id'].isin(gmap_id_list)]

            # Convertir columnas con listas o diccionarios en cadenas JSON para que sean hashables
            for col in state_df.columns:
                if state_df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                    state_df[col] = state_df[col].apply(json.dumps)

            # Eliminar duplicados solo si toda la fila es duplicada
            initial_rows = state_df.shape[0]
            state_df.drop_duplicates(inplace=True)
            duplicates_removed = initial_rows - state_df.shape[0]
            
            # Eliminar valores nulos en las columnas clave
            initial_rows = state_df.shape[0]
            state_df.dropna(subset=['user_id', 'name', 'time', 'rating', 'gmap_id'], inplace=True)
            nulls_removed = initial_rows - state_df.shape[0]

            # Informar de los datos eliminados
            print(f"En el estado {state_name} se eliminaron {duplicates_removed} duplicados y {nulls_removed} valores nulos.")

            # Guardar los datos del estado en un archivo individual
            state_output_path = os.path.join(output_folder, f"{state_name}_cleaned.parquet")
            state_df.to_parquet(state_output_path, index=False)
            print(f"Datos del estado {state_name} guardados en {state_output_path}")

    # Unir todos los archivos parquet generados
    all_files = [os.path.join(output_folder, file) for file in os.listdir(output_folder) if file.endswith(".parquet")]
    final_df = pd.concat([pd.read_parquet(file) for file in all_files], ignore_index=True)

    # Mostrar la cantidad total de filas
    print(f"Dataset final: {final_df.shape[0]} filas después de limpiar y unir.")
    return final_df

# Ejemplo de uso
if __name__ == "__main__":
    input_directory = "../Datasets/Google/metadata-sitios"
    output_path = "../Data_cleaned/metadatosgoogle/filtered_restaurants.parquet"
    process_metadata_files(input_directory, output_path)
