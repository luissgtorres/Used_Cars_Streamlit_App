import streamlit as st
import pandas as pd
import xgboost as xgb

# This function extract the unique values from the columns
def unique_values(df):
    
    makes = df['Make'].unique()
    models = df['Model'].unique()
    trims = df['Trim'].unique()
    bodies = df['Body'].unique()
    tranmissions = df['Transmission'].unique()
    states = df['State'].unique()
    colors = df['Color'].unique()

    return makes, models, trims, bodies, tranmissions, states, colors

# This function create a list with the values that the user passes. It also encode the categorical values.
def encode(df, make, model, trim, body, transmission, state, color, car_year, odometer):

    make_num = df.loc[df['Make'] == make, 'make_num'].values[0]
    model_num = df.loc[df['Model'] == model, 'model_num'].values[0]
    trim_num = df.loc[df['Trim'] == trim, 'trim_num'].values[0]
    body_num = df.loc[df['Body'] == body, 'body_num'].values[0]
    transmission_num = df.loc[df['Transmission'] == transmission, 'transmission_num'].values[0]
    state_num = df.loc[df['State'] == state, 'state_num'].values[0]
    color_num = df.loc[df['Color'] == color, 'color_num'].values[0]

    return [[car_year, make_num, model_num, trim_num, body_num, transmission_num, state_num, odometer,color_num]]

def prediction(vector):
    
    prediction = xgb.XGBRegressor()
    prediction.load_model('./modelo/precios_modelo.json')
    precio = prediction.predict(vector)
    precio_redondeado = "{:.2f}".format(precio[0])
    precio_redondeado = float(precio_redondeado)
    if precio_redondeado < 0:
        return 0
    else:
        return precio_redondeado


def model_prediction():
    
    df = pd.read_parquet('./dataset/complete_data.parquet')
    makes, models, trims, bodies, transmissions, states, colors = unique_values(df)
    
    st.write("")
    st.markdown("<h3 style='color: #FFFFFF; text-align: center;'>Modelo</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF; text-align: center;'>Seleccione las características del carro:</h4>", unsafe_allow_html=True)
    st.write("")
    one, two, three = st.columns(3)
    with one:
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Ingresa el año del carro:</label>", unsafe_allow_html=True)
        car_year = st.number_input('.', min_value = 1982, max_value = 2024, step = 1, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona la versión del carro:</label>", unsafe_allow_html=True)
        trim = st.selectbox('Selecciona la versión del carro: ', trims, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona el estado:</label>", unsafe_allow_html=True)
        state = st.selectbox('Selecciona el estado: ', states, label_visibility = 'collapsed')
    with two:
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona la marca del carro:</label>", unsafe_allow_html=True)
        make = st.selectbox('.', makes, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona la carrocería:</label>", unsafe_allow_html=True)
        body = st.selectbox('Selecciona la carrocería: ', bodies, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Ingresa el kilometraje del carro:</label>", unsafe_allow_html=True)
        odometer = st.number_input('Ingresa el kilometraje del carro: ', min_value = 0, max_value = 999999, step = 100, label_visibility = 'collapsed')
    with three:
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona el modelo del carro:</label>", unsafe_allow_html=True)
        model = st.selectbox('Selecciona el modelo del carro: ', models, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona la transmisión:</label>", unsafe_allow_html=True)
        transmission = st.selectbox('Selecciona la transmisión: ', transmissions, label_visibility = 'collapsed')
        st.markdown("<label style='color: #FFFFFF; text-align: center; margin-bottom: 0px;'>Selecciona el color del carro:</label>", unsafe_allow_html=True)
        color = st.selectbox('Selecciona el color del carro: ', colors, label_visibility = 'collapsed')
    
    vector = encode(df, make, model, trim, body, transmission, state, color, car_year, odometer)

    st.write("")
    one, two, three, four, five = st.columns(5)
    with three:
        button = st.button('Calcular precio')
    if button:        
        precio = prediction(vector)
        st.markdown(f"<h4 style='color: #FFFFFF; text-align: center;'>${precio}</h4>", unsafe_allow_html=True)