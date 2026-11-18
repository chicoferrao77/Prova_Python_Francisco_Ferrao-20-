import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl as op

df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1", decimal=",")


df.columns = df.columns.str.replace("\ufeff", "", regex=False).str.strip()

df['NOMEUP'] = df['NOMEUP'].str.strip().str.lower()
df['SERIE'] = df['SERIE'].str.strip().str.lower()


df_filtro = df[df['NOMEUP'].isin(['taquaril', 'santa ines'])]
df_filtro = df_filtro[df_filtro['SERIE'] == 'serie historica']
df_filtro = df_filtro[['NOMEUP', 'ANO', 'IQVU']]

st.write("DataFrame filtrado:", df_filtro)

st.title("Painel de Visualização do IQVU")
st.header("Análise dos Bairros Taquaril e Santa Inês")

view_option = st.sidebar.radio("Selecione a visualização:", ["Tabela", "Gráficos"])
st.sidebar.markdown("Fonte: [Prefeitura de Belo Horizonte](https://dados.pbh.gov.br/)")

if view_option == "Tabela":
    st.dataframe(df_filtro)
elif view_option == "Gráficos":
    df_taquaril = df_filtro[df_filtro['NOMEUP'] == 'taquaril']
    fig_taquaril = px.line(df_taquaril, x='ANO', y='IQVU', title="IQVU - Taquaril", markers=True)
    st.plotly_chart(fig_taquaril)

    df_santa_ines = df_filtro[df_filtro['NOMEUP'] == 'santa ines']
    fig_santa_ines = px.line(df_santa_ines, x='ANO', y='IQVU', title="IQVU - Santa Inês", markers=True)
    st.plotly_chart(fig_santa_ines)