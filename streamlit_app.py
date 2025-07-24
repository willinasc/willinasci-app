import streamlit as st
import pandas as pd

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.set_page_config(layout="wide")

st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
with st.sidebar.title("Menu"):
    st.selectbox('Selecione', ["Equipamentos","Manutenção","Calibração","Qualificação"])
   
st.file_uploader("Pesquisar arquivo")
st.divider()
df = pd.read_csv("equipamentos.csv", sep=";")
df = df[["TAG"], ["DESCRIÇÃO"], ["MARCA"], ["STATUS DE USO"], ["MANUTENÇÃO"], ["CALIBRAÇÃO"], ["QUALIFICAÇÃO"]]
st.write(df)

