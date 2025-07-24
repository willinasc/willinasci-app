import streamlit as st
import pandas as pd

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.set_page_config(layout="wide")

st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
          
st.file_uploader("Pesquisar arquivo")
st.divider()
df = pd.read_csv("equipamentos.csv", sep=";")
df = df[["TAG", "DESCRIÇÃO", "MARCA", "STATUS DE USO", "MANUTENÇÃO", "CALIBRAÇÃO", "QUALIFICAÇÃO"]]
Equipamentos = st.sidebar.selectbox("Equipamentos", df["DESCRIÇÃO"].unique())
df_filtered = df[df["DESCRIÇÃO"] == Equipamentos]
st.write(df_filtered)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("TAG", df_filtered["MANUTENÇÃO"].counter()
with col2:
   st.metric("CALIBRAÇÃO", df_filtered["CALIBRAÇÃO"].counter()
with col3:
   st.metric("QUALIFICAÇÃO", df_filtered["QUALIFICAÇÃO"].counter()
with col4:
    st.metric("MARCA", df_filtered["MARCA"].counter()


