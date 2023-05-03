import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import streamlit.components.v1 as components

def show():
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    dfIris = pd.read_csv(url)

    st.title("Visualización")
    for i in range(0, len(dfIris.columns)):
        st.subheader(dfIris.columns[i])
        fig = px.box(dfIris, y = dfIris.columns[i])
        st.plotly_chart(fig, use_container_width = True)

    st.subheader("Histrogramas")
    for i in range(0, len(dfIris.columns)):
        fig = px.histogram(dfIris, x=dfIris.columns[i])
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Gráfica de correlación")
    fig = px.scatter_matrix(dfIris, dimensions=dfIris.columns[0:4], color="variety")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Grafica de correlación | mapa de calor")
    dfIris = dfIris.drop('variety', axis=1)
    df_corr = dfIris.corr()
    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x = df_corr.columns,
            y = df_corr.index,
            z = np.array(df_corr)
        )
    )
    st.plotly_chart(fig, use_container_width=True)
show()