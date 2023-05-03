import pandas as pd
import streamlit as st
import os
import importlib

#Para quitar el menu que nos aparece por defecto.
hiden_streamlit_style = """
<style>
#MainMenu {visilibity : hidden;}
footer {visilibity : hidden;}
</style>
"""

st.markdown(hiden_streamlit_style, unsafe_allow_html=True)
url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
dfIris = pd.read_csv(url)

st.title("Análisis estadístico Iris Dataset")
st.dataframe(dfIris.head())

st.header("Estadísticas")
st.write("Filas, columnas")
st.write(dfIris.shape)

st.write("Describe:")
st.dataframe(dfIris.describe())

st.write("Clases:")
st.write(dfIris["variety"].value_counts())


pages = [f[:-3] for f in os.listdir("Pages") if f.endswith(".py")]
selection = st.sidebar.radio("Pages:", pages)
page_module = importlib.import_module(f"Pages.{selection}")
page_module.show()
