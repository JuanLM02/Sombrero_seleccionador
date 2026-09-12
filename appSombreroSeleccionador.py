import json
import random
from collections import defaultdict
import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Sombrero Seleccionador de Hogwarts",
    page_icon="🪄",
    layout="centered"
)

CASAS_INFO = {
    "Gryffindor": {
        "icono": "🦁",
        "color": "#740001",
        "secundario": "#D3A625",
        "lema": "Coraje, audacia, temple y caballerosidad.",
        "descripcion": "Perteneces a Gryffindor si tus acciones están guiadas por el valor moral, la determinación inquebrantable y la disposición a dar un paso al frente cuando otros dudan."
    },
    "Slytherin": {
        "icono": "🐍",
        "color": "#1A472A",
        "secundario": "#5D5D5D",
        "lema": "Ambición, astucia, liderazgo y autopreservación.",
        "descripcion": "Perteneces a Slytherin si posees una aguda visión estratégica, buscas la excelencia, sabes utilizar las circunstancias a tu favor y no temes aspirar a la grandeza."
    },
    "Ravenclaw": {
        "icono": "🦅",
        "color": "#0E1A40",
        "secundario": "#946B2D",
        "lema": "Inteligencia, sabiduría, curiosidad e individualidad.",
        "descripcion": "Perteneces a Ravenclaw si tu motor principal es el entendimiento del mundo, el rigor analítico, el pensamiento crítico independiente y la búsqueda constante del saber."
    },
    "Hufflepuff": {
        "icono": "🦡",
        "color": "#ECB939",
        "secundario": "#372E29",
        "lema": "Lealtad, justicia, paciencia y trabajo constante.",
        "descripcion": "Perteneces a Hufflepuff si valoras la integridad incondicional, el bienestar de la comunidad, el trabajo honesto sin buscar protagonismo y la lealtad hacia tus semejantes."
    }
}

@st.cache_data
def cargar_datos(ruta: str = "preguntas.json") -> list:
    """Carga las preguntas del archivo JSON."""
    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos if isinstance(datos, list) else datos.get("preguntas", [])

def obtener_preguntas_estratificadas(banco: list, por_categoria: int = 2) -> list:
    """Selecciona N preguntas por cada una de las categorías disponibles."""
    categorias = defaultdict(list)
    for p in banco:
        cat = p.get("categoria", "general")
        categorias[cat].append(p)
    
    seleccionadas = []
    for grupo in categorias.values():
        cantidad = min(por_categoria, len(grupo))
        seleccionadas.extend(random.sample(grupo, cantidad))
    
    random.shuffle(seleccionadas)
    
    # Barajar también las opciones dentro de cada pregunta seleccionada
    preguntas_preparadas = []
    for p in seleccionadas:
        p_copia = dict(p)
        opciones_mezcladas = list(p["opciones"])
        random.shuffle(opciones_mezcladas)
        p_copia["opciones"] = opciones_mezcladas
        preguntas_preparadas.append(p_copia)
        
    return preguntas_preparadas

def reiniciar_test():
    """Reinicia el estado de sesión para comenzar una nueva ceremonia."""
    banco = cargar_datos()
    st.session_state.preguntas = obtener_preguntas_estratificadas(banco, por_categoria=2)
    st.session_state.indice_actual = 0
    st.session_state.scores = {casa: 0 for casa in CASAS_INFO.keys()}
    st.session_state.hatstall_pendiente = False
    st.session_state.hatstall_casas = []
    st.session_state.terminado = False

# Inicialización de estado en Streamlit
if "preguntas" not in st.session_state:
    reiniciar_test()

# --- CSS personalizado para dar ambiente de Hogwarts ---
st.markdown("""
<style>
    .titulo-hogwarts {
        text-align: center;
        font-family: serif;
        font-size: 2.3rem;
        margin-bottom: 0.2rem;
    }
    .subtitulo-hogwarts {
        text-align: center;
        color: #888;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .badge-cat {
        background-color: #2b2b2b;
        color: #d1d1d1;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("<h1 class='titulo-hogwarts'>🪄 Ceremonia del Sombrero Seleccionador</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo-hogwarts'>El Sombrero explorará tus rasgos psicológicos para asignarte tu verdadera Casa.</p>", unsafe_allow_html=True)

# -------------------------------------------------------------
# FASE 1: Responder preguntas regulares
# -------------------------------------------------------------
if not st.session_state.terminado and not st.session_state.hatstall_pendiente:
    total_p = len(st.session_state.preguntas)
    idx = st.session_state.indice_actual

    if idx < total_p:
        pregunta_actual = st.session_state.preguntas[idx]
        categoria_limpia = pregunta_actual.get('categoria', 'general').replace('_', ' ')

        # Barra de progreso
        progreso = idx / total_p
        st.progress(progreso)
        st.caption(f"Pregunta {idx + 1} de {total_p} • Categoría: **{categoria_limpia.title()}**")

        st.markdown(f"### {pregunta_actual['enunciado']}")

        # Formulario para capturar la opción
        with st.form(key=f"form_pregunta_{idx}"):
            textos_opciones = [op["texto"] for op in pregunta_actual["opciones"]]
            eleccion = st.radio(
                "Selecciona la respuesta que mejor te represente:",
                options=textos_opciones,
                index=None
            )
            
            col_izq, col_der = st.columns([4, 1])
            with col_der:
                siguiente = st.form_submit_button("Continuar →", use_container_width=True)

            if siguiente:
                if eleccion is None:
                    st.warning("Por favor, selecciona una opción para continuar.")
                else:
                    # Encontrar los pesos de la opción elegida
                    for op in pregunta_actual["opciones"]:
                        if op["texto"] == eleccion:
                            for casa, peso in op["pesos"].items():
                                if casa in st.session_state.scores:
                                    st.session_state.scores[casa] += peso
                            break
                    
                    st.session_state.indice_actual += 1
                    
                    # Si completamos todas las preguntas regulares, revisar si hay Hatstall
                    if st.session_state.indice_actual >= total_p:
                        ranking = sorted(st.session_state.scores.items(), key=lambda x: x[1], reverse=True)
                        if (ranking[0][1] - ranking[1][1]) <= 1:
                            st.session_state.hatstall_pendiente = True
                            st.session_state.hatstall_casas = [ranking[0][0], ranking[1][0]]
                        else:
                            st.session_state.terminado = True
                    st.rerun()

# -------------------------------------------------------------
# FASE 2: Desempate interactivo (Hatstall)
# -------------------------------------------------------------
elif st.session_state.hatstall_pendiente and not st.session_state.terminado:
    casa_a, casa_b = st.session_state.hatstall_casas
    info_a = CASAS_INFO[casa_a]
    info_b = CASAS_INFO[casa_b]

    st.warning("⚠️ **¡UN HATSTALL HISTÓRICO!** El Sombrero Seleccionador vacila intensamente en tu mente...")
    st.write(f"Tus cualidades para **{info_a['icono']} {casa_a}** y **{info_b['icono']} {casa_b}** están en perfecto equilibrio.")
    st.markdown("#### Frente a la encrucijada definitiva, ¿qué sendero resuena más en tu espíritu?")

    opciones_hatstall = [
        f"El camino de {casa_a}: guiado por {info_a['lema'].lower()}",
        f"El camino de {casa_b}: guiado por {info_b['lema'].lower()}"
    ]

    with st.form(key="form_hatstall"):
        eleccion_h = st.radio("Tu decisión final:", options=opciones_hatstall, index=None)
        resolver = st.form_submit_button("Confirmar destino ⚡", use_container_width=True)

        if resolver:
            if eleccion_h is None:
                st.warning("Debes tomar una decisión para que el Sombrero pueda concluir.")
            else:
                if casa_a in eleccion_h:
                    st.session_state.scores[casa_a] += 2
                else:
                    st.session_state.scores[casa_b] += 2
                
                st.session_state.hatstall_pendiente = False
                st.session_state.terminado = True
                st.rerun()

# -------------------------------------------------------------
# FASE 3: Presentación de Resultados y Perfil Psicológico
# -------------------------------------------------------------
if st.session_state.terminado:
    st.progress(1.0)
    scores = st.session_state.scores
    total_pts = sum(scores.values())
    ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    casa_ganadora, max_pts = ranking[0]
    ganador_info = CASAS_INFO[casa_ganadora]

    # Banner visual de la casa ganadora
    st.balloons()
    st.markdown(f"""
    <div style="background-color: {ganador_info['color']}; padding: 25px; border-radius: 12px; text-align: center; color: white; margin-top: 10px; margin-bottom: 25px; border: 2px solid {ganador_info['secundario']};">
        <h3 style="margin: 0; color: #f0f0f0; font-size: 1.2rem;">¡EL SOMBRERO HA HABLADO!</h3>
        <h1 style="margin: 5px 0 10px 0; font-size: 3rem; font-family: serif;">{ganador_info['icono']} {casa_ganadora.upper()}</h1>
        <p style="font-style: italic; font-size: 1.1rem; margin: 0; color: #e0e0e0;">"{ganador_info['lema']}"</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"### Perfil del estudiante:\n{ganador_info['descripcion']}")

    st.divider()
    st.markdown("### 📊 Desglose de afinidad multidimensional")

    for casa, pts in ranking:
        porcentaje = (pts / total_pts) * 100
        info = CASAS_INFO[casa]
        
        col_nombre, col_barra, col_num = st.columns([2, 5, 1.2])
        with col_nombre:
            st.markdown(f"**{info['icono']} {casa}**")
        with col_barra:
            st.progress(porcentaje / 100)
        with col_num:
            st.caption(f"{porcentaje:4.1f}% ({pts} pts)")

    st.write("")
    if st.button("🔄 Comenzar una nueva Ceremonia de Selección", use_container_width=True):
        reiniciar_test()
        st.rerun()