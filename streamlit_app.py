import streamlit as st
import pandas as pd

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
with st.sidebar.title("Menu"):
    b1 = st.button("Planilha")
    b2 = st.button("Manutenção")
    b3 = st.button("Calibração")
    b4 = st.button("Qualificação")
    print(b1, b2, b3, b4)
st.file_uploader("Pesquisar arquivo")
st.divider()

