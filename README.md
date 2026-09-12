#  Sombrero Seleccionador de Hogwarts

Una aplicación web interactiva desarrollada con **Python** y **Streamlit** que simula la tradicional Ceremonia de Selección de Hogwarts. 

A diferencia de los tests convencionales basados en respuestas obvias o asignaciones 1 a 1, este proyecto implementa un **modelo de evaluación psicométrica multidimensional** con **muestreo estratificado**, **aleatorización anti-sesgo** y un sistema dinámico de resolución de **Hatstalls** (empates históricos).

---

##  Características Principales

- **Muestreo Estratificado por Categorías:** El banco de preguntas está dividido en 6 dimensiones de personalidad (dilemas morales, toma de decisiones, motivación al logro, reacción a la adversidad, relaciones interpersonales y curiosidad abstracta). Cada partida selecciona preguntas de forma balanceada, asegurando que ninguna casa se vea artificialmente favorecida por azar temático.
- **Puntuación Ponderada Multidimensional:** Cada opción de respuesta evalúa la afinidad del usuario distribuyendo pesos diferenciados entre casas primarias y secundarias.
- **Detección y Resolución de *Hatstall*:** Si al concluir el test existe un empate o una diferencia crítica de 1 punto entre los dos primeros puestos, el Sombrero activa una pregunta binaria en tiempo real para definir el destino del usuario.
- **Interfaz Fluida y Temática:** Flujo paso a paso con barra de progreso, diseño estilizado según la heráldica de Hogwarts y visualización final con desglose porcentual de personalidad.
- **Arquitectura Desacoplada:** Separación limpia entre los datos del banco de preguntas (`preguntas.json`) y la lógica de negocio de la aplicación (`app.py`), facilitando la adición de nuevas preguntas sin tocar código.

---

##  Mapeo de Casas y Rasgos Psicológicos

El sistema evalúa las cuatro casas a través de constructos de la personalidad inspirados en el modelo de los Cinco Grandes (*Big Five*):

| Casa | Icono | Virtudes Principales | Enfoque Evaluado |
| :--- | :---: | :--- | :--- |
| **Gryffindor** | 🦁 | Coraje, audacia, justicia y determinación | Acción proactiva ante el conflicto, defensa de principios morales y liderazgo directo. |
| **Slytherin** | 🐍 | Ambición, astucia, pragmatismo y liderazgo | Pensamiento estratégico, optimización de recursos, autopreservación y búsqueda de excelencia. |
| **Ravenclaw** | 🦅 | Sabiduría, intelecto, creatividad y lógica | Curiosidad cognitiva, análisis de primeros principios, escepticismo e innovación abstracta. |
| **Hufflepuff** | 🦡 | Lealtad, trabajo constante, empatía y equidad | Cohesión comunitaria, resistencia paciente, aversión al conflicto injusto y apoyo incondicional. |

---
##  Demo en Vivo

Puedes probar la aplicación interactiva directamente en tu navegador sin instalar nada:  
>>>> **[Acceder al Sombrero Seleccionador en Streamlit](https://sombreroseleccionador-g7kw5katgi7gpskfcqhlrh.streamlit.app/)**
---
##  Estructura del Proyecto

```text
Sombrero_seleccionador/
├── appSombreroSeleccionador.py  # Aplicación web interactiva y lógica principal (Streamlit)
├── preguntas.json               # Banco de preguntas estratificado en formato JSON
├── requirements.txt             # Dependencias necesarias para el despliegue en la nube
└── README.md                    # Documentación técnica y guía de uso

---

##  Instalación y Ejecución Local

### Prerrequisitos
Tener instalado **Python 3.9+** y el gestor de paquetes **pip**.

### 1. Clonar el repositorio
```bash
git clone https://github.com/JuanLM02/Sombrero_seleccionador.git
cd Sombrero_seleccionador
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación web
```bash
streamlit run app.py
```
La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

*(Opcional) Si deseas ejecutar la versión de consola:*
```bash
python sombrero.py
```

---

##  Despliegue en la Nube (Streamlit Cloud)

El proyecto está preparado para desplegarse de forma gratuita y continua en **Streamlit Community Cloud**:

1. Haz un fork o sube este repositorio a tu cuenta de GitHub.
2. Ingresa a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con GitHub.
3. Haz clic en **New app** y selecciona:
   - **Repository:** `JuanLM02/Sombrero_seleccionador`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Haz clic en **Deploy!** y obtendrás una URL pública permanente para compartir.

---

##  Tecnologías Utilizadas

- **Lenguaje:** Python 3
- **Framework Web:** [Streamlit](https://streamlit.io/)
- **Formato de Datos:** JSON
- **Control de Versiones:** Git & GitHub

---

##  Licencia

Este proyecto fue desarrollado con fines recreativos y educativos. El universo de *Harry Potter* y los nombres de las casas de Hogwarts son propiedad intelectual de J.K. Rowling y Warner Bros. Entertainment Inc.
