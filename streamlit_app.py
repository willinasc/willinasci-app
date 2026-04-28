import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.set_page_config(layout="wide")

st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
          
st.file_uploader("Pesquisar arquivo")
st.divider()
df = pd.read_csv("equipamentos.csv", sep=";")
df = df[["TAG", "DESCRIÇÃO", "MARCA", "STATUS DE USO", "MANUTENÇÃO", "CALIBRAÇÃO", "QUALIFICAÇÃO"]]
Equipamentos = st.sidebar.selectbox("Equipamentos", df["DESCRIÇÃO"].unique(), index=None, placeholder="Selecione o equipamento")
df_filtered = df[df["DESCRIÇÃO"] == Equipamentos]
st.dataframe(df_filtered)

'''
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.bar_chart(df["MANUTENÇÃO"].value_counts())
with col2:
    st.bar_chart(df["CALIBRAÇÃO"].value_counts())
with col3:
    st.bar_chart(df["QUALIFICAÇÃO"].value_counts())
with col4:
    st.bar_chart(df["MARCA"].value_counts())

'''
