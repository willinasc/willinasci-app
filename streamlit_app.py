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



