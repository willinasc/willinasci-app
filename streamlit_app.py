import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import seaborn as sns

st.title("🎈 Gestão de Equipamentos Controle de Qualidade")
st.set_page_config(layout="wide")

st.info(
    "Acompanhamento das Manutenções, Calibrações e Qualificaçoes dos Equipamentos"
)
          
arquivo = st.file_uploader("Pesquisar arquivo")
if arquivo:
    df = pd.read_excel(arquivo, sheet_name='LISTA MESTRA DE EQUIPAMENTOS', engine="openpyxl", nrows=301, usecols="A:W")
    df


st.divider()

df.groupby('STATUS DE USO').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()


df = pd.read_csv("equipamentos.csv", sep=";")
df = df[["TAG", "DESCRIÇÃO", "MARCA", "STATUS DE USO", "MANUTENÇÃO", "CALIBRAÇÃO", "QUALIFICAÇÃO"]]
Equipamentos = st.sidebar.selectbox("Equipamentos", df["DESCRIÇÃO"].unique(), index=None, placeholder="Selecione o equipamento")
df_filtered = df[df["DESCRIÇÃO"] == Equipamentos]
st.dataframe(df_filtered)



