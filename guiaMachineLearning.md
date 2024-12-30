
# GUIA MACHINE LEARNING: Sistema de Recomendacion y Analisis de Sentimiento

# 1. Definir objetivos claros y métricas de éxito

## Objetivos

- Asegurar que los modelos de recomendación sean precisos y útiles para los usuarios finales.
- Identificar correctamente los sentimientos expresados en las opiniones de los usuarios.

## Métricas clave

### Para el sistema de recomendación

- **Precisión:** Proporción de recomendaciones relevantes entre las sugeridas.
- **Recall:** Proporción de restaurantes relevantes que fueron recomendados.
- **NDCG (Normalized Discounted Cumulative Gain):** Mide la relevancia de las recomendaciones considerando su orden.

### Para el análisis de sentimiento

- **Precisión, recall y F1-score:** Evaluar la capacidad del modelo para identificar correctamente las categorías de sentimiento.

# 2. Recolección de datos

Este paso implica obtener la información necesaria para entrenar los modelos y realizar los análisis.

## Fuentes principales

- **Yelp API:** Proporciona datos estructurados sobre restaurantes, calificaciones, ubicaciones y reseñas.
- **Google Maps API:** Brinda información complementaria, como reseñas y datos geográficos.

## Parámetros de búsqueda

- Limitar las consultas a los **10 estados más relevantes de la zona este**. Por ejemplo, puedes priorizar estados como Nueva York, Florida, Massachusetts, etc., según la densidad de opiniones.
- Filtrar por **categoría gastronómica**, como restaurantes, cafeterías o bares.

## Estrategias de extracción

- Usar scripts de Python para conectarte a las APIs.
- Definir un proceso de paginación para obtener grandes volúmenes de datos.
- Guardar los datos en formatos estructurados como CSV o bases de datos SQL.

## Contenido recolectado

- Información básica: Nombre del restaurante, dirección, categoría.
- Opiniones: Texto de reseñas, calificación (de 1 a 5 estrellas), fecha de la reseña.
- Datos adicionales: Ubicación geográfica (latitud, longitud), cantidad de reseñas totales.

# 3. Limpieza y exploración de datos

Este paso asegura que los datos sean consistentes, relevantes y listos para el análisis.

## Limpieza de datos

- **Manejar valores faltantes:** Eliminar registros incompletos o imputar valores cuando sea apropiado.
- **Eliminación de duplicados:** Evitar que el mismo restaurante o reseña aparezca múltiples veces.
- **Corrección de formatos:** Estandarizar las fechas, direcciones y texto.

## Exploración inicial

### Generar estadísticas descriptivas

- Distribución de calificaciones (promedio, mediana, desviación estándar).
- Cantidad de reseñas por estado y categoría.

### Visualizaciones iniciales

- Histogramas para calificaciones.
- Mapas de calor para distribución geográfica.

### Identificar posibles outliers

- Reseñas extremadamente largas o cortas.
- Restaurantes con calificaciones atípicas.

# 4. Análisis exploratorio inicial

Este análisis te permite entender mejor los patrones y tendencias en los datos recolectados.

## Preguntas clave

- ¿Qué estados tienen más reseñas y calificaciones promedio más altas?
- ¿Existen diferencias notables entre categorías de restaurantes?
- ¿Cómo varían las calificaciones promedio por estado o ciudad?

## Visualizaciones recomendadas

- Gráficos de barras para comparar la cantidad de reseñas por estado.
- Mapas geográficos interactivos para mostrar la densidad de restaurantes.
- Diagramas de dispersión que relacionen calificaciones promedio con la cantidad de reseñas.

## Transformaciones necesarias

- Normalización o estandarización de atributos, si se requiere.
- Conversión de texto a formatos utilizables, por ejemplo, eliminando caracteres especiales o normalizando el idioma.

# Entregables al final de la Fase 1

- Un conjunto de datos limpio y estructurado, listo para ser utilizado en las fases siguientes.
- Un informe del análisis exploratorio inicial, con visualizaciones que resuman los hallazgos clave.


# Fase 2: Implementación del Sistema de Recomendación

Este componente se centra en desarrollar un sistema que pueda sugerir restaurantes basándose en los datos recolectados y en las preferencias de los usuarios. Esta fase combina métodos de machine learning y procesamiento de datos.

## 4. Selección de enfoques de recomendación

Antes de construir el modelo, es importante definir los métodos que usarás. Los tres enfoques principales son:

### Filtrado colaborativo (Collaborative Filtering)

- **Concepto:** Recomendaciones basadas en el comportamiento de los usuarios (calificaciones previas, patrones de interacción).
- **Métodos comunes:**
  - User-based: Busca usuarios con gustos similares al usuario actual y sugiere los restaurantes que ellos han calificado positivamente.
  - Item-based: Encuentra restaurantes similares a los que el usuario ya calificó bien y recomienda esos.
- **Ventajas:** No requiere datos específicos de los restaurantes, solo calificaciones de usuarios.
- **Desventajas:** Necesita suficientes datos para evitar el problema de arranque en frío.

### Filtrado basado en contenido (Content-based Filtering)

- **Concepto:** Recomendaciones basadas en atributos de los restaurantes (categoría, ubicación, palabras clave en reseñas).
- **Métodos comunes:**
  - Utilizar técnicas como TF-IDF o embeddings para representar las reseñas.
  - Similaridad de coseno para calcular la relación entre restaurantes.
- **Ventajas:** Funciona bien para nuevos usuarios si se tienen sus preferencias iniciales.
- **Desventajas:** Puede limitar las recomendaciones a opciones similares a las ya exploradas.

### Modelo híbrido

- **Concepto:** Combina filtrado colaborativo y basado en contenido.
- **Métodos comunes:**
  - Ponderar las salidas de ambos métodos.
  - Usar modelos más complejos como redes neuronales profundas para integrar ambas fuentes de información.
- **Ventajas:** Supera las limitaciones individuales de cada método.
- **Desventajas:** Mayor complejidad y demanda de recursos.

## 5. Preparación y preprocesamiento de datos

Antes de entrenar los modelos, los datos deben ser organizados y transformados adecuadamente.

### Matriz usuario-restaurante

- Crear una matriz donde las filas sean usuarios y las columnas sean restaurantes, y los valores sean las calificaciones.
- Si un usuario no ha calificado un restaurante, deja el valor como vacío o 0.

### Representación de atributos de contenido

- Procesar las reseñas usando técnicas de NLP:
  - Tokenización y lematización para limpiar texto.
  - Vectorización con TF-IDF, Word2Vec, o embeddings preentrenados como BERT.
  - Extraer atributos como ubicación geográfica, categoría y calificación promedio.

### Reducción de dimensionalidad (opcional)

- Usar métodos como PCA o t-SNE para simplificar los vectores de atributos.

## 6. Entrenamiento de los modelos

Entrenar el sistema de recomendación utilizando uno o más de los enfoques seleccionados.

### Filtrado colaborativo

#### Modelo basado en memoria
- Calcular la similitud entre usuarios o entre restaurantes (por ejemplo, usando similaridad de coseno o correlación de Pearson).
- Hacer predicciones basadas en el promedio ponderado de calificaciones de usuarios similares.

#### Modelo basado en factores
- Usar técnicas como ALS (Alternating Least Squares) para descomponer la matriz usuario-restaurante en vectores latentes que representen características implícitas.

#### Entrenamiento
```python
from pyspark.ml.recommendation import ALS
als = ALS(userCol="user_id", itemCol="restaurant_id", ratingCol="rating", coldStartStrategy="drop")
model = als.fit(training_data)
```

### Filtrado basado en contenido
- Crear una matriz de características para cada restaurante.
- Usar un modelo de clasificación (por ejemplo, SVM o Random Forest) o calcular similitudes directas entre vectores.

### Modelo híbrido
- Integrar resultados de ambos métodos usando:
  - Un modelo ponderado.
  - Redes neuronales profundas para aprender combinaciones óptimas.

## 7. Evaluación y ajuste

Una vez entrenado, evalúa el desempeño del modelo.

### Métricas clave
- Precisión: Porcentaje de recomendaciones que fueron relevantes.
- Recall: Proporción de restaurantes relevantes que fueron recomendados.
- RMSE o MAE: Para medir el error entre calificaciones reales y predichas.

### Validación cruzada
- Dividir los datos en conjuntos de entrenamiento y prueba.
- Usar validación cruzada para asegurar que el modelo generaliza bien.

### Ajuste de hiperparámetros
- Usar técnicas como GridSearch o RandomSearch para optimizar parámetros como:
  - Número de factores latentes en ALS.
  - Peso en los modelos híbridos.

## 8. Generación de recomendaciones

### Predicción para usuarios existentes
- Generar una lista de restaurantes recomendados ordenados por puntuación.

### Predicción para nuevos usuarios
- Usar atributos iniciales del usuario (preferencias explícitas, ubicación) para ofrecer recomendaciones basadas en contenido.

## Entregables al final de la Fase 2

- Un sistema de recomendación funcional que puede sugerir restaurantes personalizados.
- Reportes sobre el desempeño del modelo, destacando métricas como precisión y recall.


# Fase 3: Implementación del Análisis de Sentimiento

Este componente se centra en comprender cómo los clientes perciben los restaurantes basándose en las reseñas de usuarios. Este análisis es crucial para predecir el éxito o fracaso potencial de nuevos locales.

## 1. Comprensión del problema

### Objetivo del análisis de sentimiento

- Determinar el tono (positivo, negativo o neutro) de las reseñas de usuarios en Yelp y Google Maps.
- Cuantificar el nivel de satisfacción general y detectar patrones específicos en las opiniones.

### Preguntas clave

- ¿Qué porcentaje de opiniones es positivo/negativo en cada estado o ciudad?
- ¿Cuáles son las palabras clave asociadas con opiniones negativas o positivas?
- ¿Cómo se correlacionan los sentimientos con las calificaciones (1-5 estrellas)?

## 2. Preparación de los datos

El primer paso es organizar los datos de reseñas para que sean utilizables en modelos de análisis de sentimiento.

### Preprocesamiento del texto

- Convertir texto a minúsculas.
- Eliminar caracteres especiales, números y signos de puntuación.
- Eliminar palabras irrelevantes (stopwords) como "el", "de", "a", etc.
- Lematización para reducir las palabras a su forma raíz (por ejemplo, "comiendo" → "comer").

### Creación de etiquetas

- Usar calificaciones como proxy para el sentimiento:
  - 1-2 estrellas: Sentimiento negativo.
  - 3 estrellas: Sentimiento neutral.
  - 4-5 estrellas: Sentimiento positivo.
- Para reseñas sin calificaciones explícitas, se pueden etiquetar manualmente o usar un modelo preentrenado.

### Vectorización del texto

- Convertir el texto en representaciones numéricas:
  - TF-IDF (Term Frequency-Inverse Document Frequency): Pondera palabras según su importancia en las reseñas.
  - Embeddings preentrenados: Usar modelos como Word2Vec, GloVe, o BERT para capturar significado contextual.

Ejemplo de TF-IDF:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(reviews)
```

## 3. Entrenamiento del modelo de análisis de sentimiento

### Modelos clásicos de clasificación

- Modelos como Logistic Regression, SVM (Support Vector Machines), o Random Forest.
- Entrenamiento:
  - Entrada: Características vectorizadas (TF-IDF o Bag of Words).
  - Salida: Etiquetas de sentimiento (positivo, negativo, neutral).

Ejemplo:
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
```

### Modelos basados en aprendizaje profundo

- Usar redes neuronales recurrentes (RNN), redes neuronales convolucionales (CNN), o modelos transformadores como BERT.

Ejemplo con BERT (usando Hugging Face Transformers):
```python
from transformers import BertTokenizer, BertForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
```

Ventajas:
- Captura relaciones contextuales más complejas en las reseñas.
- Funciona mejor con grandes volúmenes de datos.

## 4. Evaluación del modelo

### Métricas clave

- Precisión: Proporción de predicciones correctas entre todas las predicciones.
- Recall: Proporción de sentimientos correctamente identificados.
- F1-score: Media armónica de precisión y recall, útil en clases desbalanceadas.
- Matriz de confusión: Muestra cómo se clasificaron las etiquetas.

### Validación cruzada

- Dividir los datos en conjuntos de entrenamiento, validación y prueba.
- Usar validación cruzada para evaluar la estabilidad del modelo.

## 5. Análisis y visualización de resultados

### Cuantificación de sentimientos

- Proporción de opiniones positivas, negativas y neutras por estado, ciudad o restaurante.
- Evolución temporal de los sentimientos (por ejemplo, por trimestre o año).

### Detección de palabras clave

- Usar técnicas como análisis de frecuencia de palabras o n-gramas para identificar términos asociados con sentimientos.

Visualización con nubes de palabras:
```python
from wordcloud import WordCloud
wordcloud = WordCloud().generate(positive_reviews)
```

### Análisis geográfico

- Mapas interactivos que muestren el sentimiento promedio por ubicación geográfica.

## 6. Aplicación para predecir éxito o fracaso de nuevos locales

### Factores predictores

- Opiniones positivas recientes en un área específica.
- Palabras clave frecuentes relacionadas con "buena atención", "calidad", "ambiente", etc.
- Relación entre sentimientos y calificaciones.

### Predicción

- Entrenar un modelo supervisado (por ejemplo, XGBoost) con atributos como:
  - Promedio de sentimientos en un área.
  - Número de opiniones.
  - Categoría del restaurante.
- Salida: Probabilidad de éxito en una ubicación específica.

## Entregables al final de la Fase 3

- Un sistema de recomendación de comidas diseñado para asistir al usuario en la selección del establecimiento ideal y fomente la exploración de nuevos sabores y platos con confianza.
- Un modelo de análisis de sentimiento con métricas validadas que proporcione a la gerencia una visión clara de la percepción de los usuarios, identificando áreas de mejora y fortalezas a potenciar.
- Un sistema que pueda predecir el éxito potencial de un nuevo local basado en patrones de sentimiento.
- Insights clave sobre las opiniones de los usuarios, organizados por región, categoría y restaurante. Estos podrian ser mostrados en el Dashboard.
- Visualizaciones como nubes de palabras, gráficos de barras y mapas interactivos. Estos podrian ser mostrados en el Dashboard.
