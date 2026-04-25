# 📊 Análisis de Reseñas de Usuarios

## 📌 Descripción

Este proyecto corresponde al **Trabajo Práctico 1** de la materia *Taller 2*, cuyo objetivo es realizar un **análisis exploratorio de un dataset real de reseñas de usuarios** utilizando Python.

Se desarrolló un flujo que permite:

* Explorar la estructura del dataset
* Analizar métricas clave (ratings y texto)
* Generar visualizaciones
* Construir un informe en formato Markdown

---

## 🧠 Objetivos del proyecto

* Manipular datos utilizando `pandas`
* Realizar análisis exploratorio
* Generar visualizaciones con `matplotlib` y `seaborn`
* Interpretar resultados de forma fundamentada

---

## 📂 Estructura del proyecto

```
tp1/
│
├── data/
│   └── dataset.csv
│
├── analysis/
│   ├── analysis.py
│   └── modules/
│       ├── ratings.py
│       ├── text.py
│       ├── cases.py
│       └── visualization.py
│
├── reports/
│   ├── exploration_report.md
│   ├── analysis_report.md
│   └── *.png
│
├── scriptExploratorio.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación y ejecución

### 1. Crear entorno virtual

```bash
python -m venv venv
```

### 2. Activar entorno

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

### 🔍 Exploración inicial

* El dataset contiene reseñas de usuarios con texto y puntuaciones asociadas.

Genera un reporte con:

* estructura del dataset
* tipos de datos
* valores faltantes

```bash
python scriptExploratorio.py
```

>[!Tip]
>Opciones disponibles:
> - `--overwrite` → sobreescribir el reporte anterior
> - `--timestamp` → generar un reporte con timestamp
```
python scriptExploratorio.py --overwrite

python scriptExploratorio.py --timestamp
```

Salida:

```
reports/exploration_report.md
```

---

### 📊 Análisis completo

Ejecuta todos los análisis requeridos:

* ratings
* texto
* casos
* visualizaciones

```bash
python analysis/analysis.py
```

Salida:

```
reports/analysis_report.md
reports/*.png
```

---

## 📊 Resultados

Los resultados se exportan en:

* Markdown (`.md`) → informe principal
* Imágenes (`.png`) → visualizaciones

---

## 🧪 Tecnologías utilizadas

* Python
* pandas
* matplotlib
* seaborn

---

## 📌 Notas

* El proyecto está diseñado como un **análisis puntual (one-shot)**.

---

## 👨‍💻 Autor

Trabajo realizado con fines académicos por Mateo Márquez.
