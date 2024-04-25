<h1 align="center"> AUTOMARKET Model </h1>

## Introducción

Con el fin de brindar una herramienta para que los comerciantes de vehículos usados puedan ofrecer precios justos y libres de especulaciones a sus clientes, se desarrolló una aplicación web que permitirá obtener el precio del vehículo a partir de las diferentes características que suministre el usuario. Esta aplicación podrá ser consumida tanto por dueños de negocios para saber el precio en el que deben ofertar sus vehículos, como por los compradores que deseen conocer cuánto dinero necesitan para adquirir un vehículo.

## Acceso a la App

La aplicación web se encuentra disponible en Streamlit cloud.

## Modo de uso

La aplicación está dividida en tres subpáginas:

1.	Home: acá podemos encontrar una breve descripción del modelo empleado para realizar la predicción de los precios de los vehículos.
2.	Métricas: acá podemos observar las métricas empleadas para evaluar el modelo desarrollado, así como gráficas que permiten observar lo confiable y fiable que es el modelo.
3.	Modelo: acá están las diferentes características para que el usuario las ingrese y presione el botón de calcular el precio para generarlo. El precio arrojado por el modelo está en USD.

## Modelo

Se utilizó un modelo de regresión para calcular el precio del vehículo, específicamente se empleó el XGBoostRegressor. Este modelo se basa en el algoritmo de aumento de árboles en gradiente, que es una técnica poderosa para construir modelos de predicción precisos. Es conocido por su eficiencia y precisión, y se ha utilizado con éxito en una amplia gama de aplicaciones entre las que se incluye la predicción de precios, análisis de riesgos y detección de anomalías.

El modelo utiliza las siguientes características del vehículo para realizar la predicción:

-	Año del carro.
-	Marca.
-	Modelo.
-	Carrocería.
-	Versión.
-	Transmisión.
-	Estado donde se comprará.
-	Kilometraje.
-	Color.

Las variables categóricas (no numéricas) son convertidas a numéricas para que el modelo pueda realizar la predicción. El valor del precio que se obtiene está en USD.

## Tecnologías

-	Python.
-	Pandas.
-	Streamlit.
-	XGBoost.
-	Scikit-learn.
