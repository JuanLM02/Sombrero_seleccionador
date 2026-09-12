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
├── app.py              # Aplicación web interactiva en Streamlit (interfaz y flujo)
├── sombrero.py         # Versión alternativa para ejecución en consola (CLI)
├── preguntas.json      # Banco de preguntas estratificado en formato JSON
├── requirements.txt    # Dependencias del entorno de ejecución
└── README.md           # Documentación técnica del proyecto
