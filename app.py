import numpy as np
import streamlit as st
import tensorflow as tf

from PIL import Image


st.set_page_config(
    page_title="Clasificador de Imágenes CIFAR-10",
    page_icon="🤖",
    layout="centered"
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
    }

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .titulo {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: #183153;
        margin-bottom: 8px;
    }

    .subtitulo {
        text-align: center;
        color: #667085;
        font-size: 16px;
        margin-bottom: 28px;
    }

    .resultado {
        background-color: white;
        border: 1px solid #dce3ea;
        border-radius: 16px;
        padding: 22px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
    }

    .prediccion {
        font-size: 30px;
        font-weight: 800;
        color: #183153;
    }

    .confianza {
        font-size: 24px;
        font-weight: 700;
        color: #168052;
        margin-top: 8px;
    }

    .autor {
        text-align: center;
        color: #7a8491;
        font-size: 13px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


@st.cache_resource
def cargar_modelo():
    return tf.keras.models.load_model(
        "modelo_cifar10.keras"
    )


model = cargar_modelo()


class_names = [
    "Avión",
    "Automóvil",
    "Pájaro",
    "Gato",
    "Ciervo",
    "Perro",
    "Rana",
    "Caballo",
    "Barco",
    "Camión"
]


def preparar_imagen(imagen):

    imagen = imagen.convert("RGB")

    imagen = imagen.resize(
        (32, 32)
    )

    imagen = np.array(
        imagen,
        dtype=np.float32
    )

    imagen = imagen / 255.0

    imagen = np.expand_dims(
        imagen,
        axis=0
    )

    return imagen


def predecir_imagen(imagen):

    imagen_preparada = preparar_imagen(
        imagen
    )

    predicciones = model.predict(
        imagen_preparada,
        verbose=0
    )

    indice = int(
        np.argmax(predicciones[0])
    )

    confianza = float(
        np.max(predicciones[0])
    ) * 100

    clase = class_names[indice]

    return clase, confianza


st.markdown(
    """
    <div class="titulo">
        🤖 Clasificador de Imágenes
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitulo">
        Suba una imagen o tome una fotografía para que
        el modelo de Inteligencia Artificial identifique el objeto.
    </div>
    """,
    unsafe_allow_html=True
)


opcion = st.radio(
    "Seleccione una opción:",
    [
        "📁 Subir imagen",
        "📷 Usar cámara"
    ],
    horizontal=True
)


imagen = None


if opcion == "📁 Subir imagen":

    archivo = st.file_uploader(
        "Seleccione una imagen",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    if archivo is not None:

        imagen = Image.open(
            archivo
        )


else:

    foto = st.camera_input(
        "Tome una fotografía"
    )

    if foto is not None:

        imagen = Image.open(
            foto
        )


if imagen is not None:

    st.image(
        imagen,
        caption="Imagen seleccionada",
        use_container_width=True
    )

    if st.button(
        "🔍 Analizar imagen",
        type="primary",
        use_container_width=True
    ):

        with st.spinner(
            "Analizando imagen..."
        ):

            clase, confianza = predecir_imagen(
                imagen
            )

        # NOTA: el HTML va sin indentación en cada línea.
        # Streamlit interpreta el markdown, y las líneas con 4+
        # espacios de sangría se muestran como bloque de código
        # en vez de renderizarse como HTML. Por eso antes se veían
        # las etiquetas <div> como texto plano.
        st.markdown(
            f"""<div class="resultado">
<div>PREDICCIÓN</div>
<div class="prediccion">{clase}</div>
<div class="confianza">Confianza: {confianza:.2f}%</div>
</div>""",
            unsafe_allow_html=True
        )

        st.progress(
            min(
                int(confianza),
                100
            )
        )


st.info(
    "El modelo fue entrenado con CIFAR-10 y puede identificar: "
    "avión, automóvil, pájaro, gato, ciervo, perro, rana, "
    "caballo, barco y camión."
)


st.markdown(
    """
    <div class="autor">
        Desarrollado por: Josue Fabricio Herrera
    </div>
    """,
    unsafe_allow_html=True
)
