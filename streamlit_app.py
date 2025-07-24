import streamlit as st
import pandas as pd

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.write(
    "Acompanhamento das Manutenções, Clibrações e Qualificaçoes dos Equipamentos"
)
st.sidebar("Menu")
st.file_uploader("Pesquisar arquivo")
