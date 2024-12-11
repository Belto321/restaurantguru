# Tecnologías utilizadas en el proyecto de sistema de recomendación de restaurantes

## 1. Fuentes de Datos

### **API de Yelp**
- Proporciona información detallada sobre restaurantes, incluyendo reseñas de usuarios, calificaciones y detalles de contacto. Es una fuente primaria de datos para las recomendaciones.

### **API de Google Maps**
- Ofrece datos geográficos y de localización, incluyendo horarios, ubicaciones exactas y opiniones de usuarios. Útil para calcular distancias y sugerir opciones cercanas a los usuarios.

### **Google Drive**
- Se utiliza para almacenar archivos y datos complementarios del proyecto, como datasets iniciales y datos de respaldo.

---

## 2. Procesamiento de Datos

### **Apache Spark**
- Permite realizar el procesamiento distribuido de grandes volúmenes de datos para la extracción, transformación y carga (ETL). Ideal para manejar datos provenientes de múltiples fuentes.

### **Python**
- Lenguaje principal para el desarrollo del sistema, utilizado en todas las etapas del proyecto, desde la extracción de datos hasta el modelado y la visualización.

### **Pandas**
- Biblioteca de Python para manipulación y análisis de datos estructurados. Facilita la limpieza y transformación de datos.

### **Data Lake (Google Cloud BigQuery)**
- Almacén centralizado donde se guardan grandes volúmenes de datos en bruto. BigQuery permite realizar consultas rápidas y escalables sobre estos datos.

---

## 3. Exploración y Análisis de Datos (EDA)

### **NumPy**
- Biblioteca de Python utilizada para cálculos matemáticos y operaciones de álgebra lineal. Es esencial para el análisis numérico.

### **Matplotlib y Seaborn**
- Herramientas de visualización de datos en Python. Matplotlib es ideal para gráficos básicos, mientras que Seaborn facilita gráficos más complejos y estilizados.

### **Plotly**
- Biblioteca de visualización interactiva, utilizada para crear gráficos dinámicos que pueden integrarse en dashboards.

### **Scikit-learn**
- Framework de Python para análisis estadístico y modelado inicial. Se usa para tareas como clustering y regresiones durante el EDA.

---

## 4. Machine Learning

### **Scikit-learn**
- Utilizado para implementar algoritmos de aprendizaje supervisado y no supervisado. Ideal para modelos sencillos de recomendación.

### **TensorFlow/PyTorch**
- Frameworks avanzados de Machine Learning para construir y entrenar redes neuronales profundas. Ideales para modelos complejos y personalizados.

### **NLTK y SpaCy**
- Herramientas de procesamiento de lenguaje natural (NLP). Se utilizan para analizar opiniones y extraer sentimientos de las reseñas de texto.

### **Pickle**
- Biblioteca de Python para serializar modelos de ML, permitiendo guardarlos y cargarlos fácilmente para su implementación.

### **Hugging Face (BERT)**
- Modelo avanzado de NLP basado en transformers. Se usa para análisis de sentimiento y comprensión de texto en las reseñas.

---

## 5. Implementación

### **Google Cloud Run**
- Servicio de Google Cloud para desplegar aplicaciones en contenedores. Permite ejecutar APIs del sistema de recomendación sin gestionar servidores.

### **Google Cloud Build**
- Herramienta de integración y despliegue continuo (CI/CD). Automatiza la construcción, pruebas y despliegue de los componentes del sistema.

---

## 6. Visualización

### **Power BI**
- Herramienta de visualización de datos que permite crear dashboards interactivos y presentar los resultados del análisis a los usuarios o clientes.

### **Looker Studio (antes Google Data Studio)**
- Plataforma de visualización de datos de Google. Proporciona una integración nativa con BigQuery para crear dashboards personalizados.

---

## Resumen
Esta combinación de tecnologías garantiza un flujo de trabajo eficiente y escalable, desde la extracción de datos hasta la presentación de resultados, optimizando cada etapa del sistema de recomendación.

