import streamlit as st
import pandas as pd
from PIL import Image

def metric(txt_1, txt_2, txt_3, txt_4):

    prediccion_vs_real = Image.open('./imagenes/predicción_vs_real.jpg')
    caracteristicas = Image.open('./imagenes/características_importantes.jpg')
    aprendizaje = Image.open('./imagenes/aprendizaje.jpg')

    metricas = pd.read_parquet('./dataset/metricas.parquet')

    st.write("")
    st.markdown("<h3 style='color: #FFFFFF; text-align: center;'>Evaluación del modelo</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF; text-align: left;'>Métricas</h4>", unsafe_allow_html=True)
    st.dataframe(metricas, use_container_width = True, hide_index = True)
    st.markdown(f"<h5 style='color: #FFFFFF; text-align: center;'>{txt_1}</h5>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='color: #FFFFFF; text-align: left;'>Predicción vs Valor real</h4>", unsafe_allow_html=True)
    st.image(prediccion_vs_real)
    st.markdown(f"<h5 style='color: #FFFFFF; text-align: center;'>{txt_2}</h5>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='color: #FFFFFF; text-align: left;'>Importancia de las variables</h4>", unsafe_allow_html=True)
    st.image(caracteristicas)
    st.markdown(f"<h5 style='color: #FFFFFF; text-align: center;'>{txt_3}</h5>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='color: #FFFFFF; text-align: left;'>Curva de aprendizaje</h4>", unsafe_allow_html=True)
    st.image(aprendizaje)
    st.markdown(f"<h5 style='color: #FFFFFF; text-align: center;'>{txt_4}</h5>", unsafe_allow_html=True)