import streamlit as st
import pandas as pd

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
with st.sidebar.title("Menu")
    b1 = st.button("Manutenção")
print(b1)
st.file_uploader("Pesquisar arquivo")
st.divider()

