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

