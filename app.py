
import streamlit as st
from PIL import Image
from model import model_prediction
from metrics import metric
import path
import sys


# So the file can be found in github
dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# Read the text archive
with open("./modelo/descripcion_del_modelo.txt", "r", encoding="utf-8") as file:
        
    primero = ""
    linea = file.readline()
    while linea.strip():  
        primero += linea
        linea = file.readline()

    segundo = ""
    linea = file.readline()
    while linea.strip():  
        segundo += linea
        linea = file.readline()
    
    tercero = ""
    linea = file.readline()
    while linea.strip():  
        tercero += linea
        linea = file.readline()
    
    cuarto = ""
    linea = file.readline()
    while linea.strip():  
        cuarto += linea
        linea = file.readline()
    
    quinto = ""
    linea = file.readline()
    while linea.strip():  
        quinto += linea
        linea = file.readline()

    sexto = ""
    linea = file.readline()
    while linea:
        sexto += linea
        linea = file.readline()

# Load the image
car = Image.open('./imagenes/Car.jpeg')

# Creating the app
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main
{{
    background-color: black;
    background-size: cover;    
}}

[data-testid="stHeader"]
{{
    background-color: transparent;
}}

[data-testid="stSidebar"] > div:first-child 
{{
    background-color: #323232    
}}

[data-testid="stToolbar"] 
{{
    color: white;
}}

[data-testid="baseButton-header"] 
{{
    color: white;
}}

[data-testid="collapsedControl"] 
{{
    color: white;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='color: #FFFFFF; text-align: center;'>AUTOMARKET</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: #FFFFFF; text-align: center;'>¡Modelo de predicción de precios!</h2>", unsafe_allow_html=True)
st.sidebar.header("")

with st.sidebar:
    st.markdown("<h1 style='color: #FFFFFF; text-align: left;'>AUTOMARKET</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #FFFFFF; text-align: left;'>Web App 🚗</h3>", unsafe_allow_html=True)
    st.image(car)
    st.write("")

menu = ['Home', 'Métricas', 'Modelo']
st.sidebar.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Elige la página</label>", unsafe_allow_html=True)
choice = st.sidebar.selectbox(':Elige la página', menu, label_visibility = 'collapsed')    

if choice == 'Modelo':
    model_prediction()

elif choice == 'Home': 
    st.write("")
    st.markdown("<h3 style='color: #FFFFFF; text-align: center;'>Descripción del modelo</h3>", unsafe_allow_html=True)
    st.write("")
    st.markdown(f"<h5 style='color: #FFFFFF; text-align: center;'>{primero}</h5>", unsafe_allow_html=True)
    st.write("")
    st.markdown(f"<h5 style='color: #FFFFFF;; text-align: center;'>{segundo}</h5>", unsafe_allow_html=True)

elif choice == 'Métricas':        

    metric(tercero, cuarto, quinto, sexto)
