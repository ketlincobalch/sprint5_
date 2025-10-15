import pandas as pd
import streamlit as st
from utils.pre_process import process_dataframe
import plotly.express as px

# Lê arquivo de dados
df_raw = pd.read_csv(r'data/raw/superstore.csv')

# Faz as limpezas iniciais do arquivo de dados
df = process_dataframe(df_raw)

df.to_csv(r'./data/processed/superstore_clean.csv', index=False)

st.title('Superstore Data')

toogle_amostra = st.toggle("Visualiza Amostra dos dados?")
if toogle_amostra:
    columns = (
        st.multiselect(
            label="Quais colunas você quer visualizar?",
            options=df.columns.tolist(),
            default=['order_id', 'sub_category', 'product_name', 'quantity', 'profit']
        )
    )
    st.dataframe(data=df[columns].sample(10, random_state=42))

graf_barra = px.bar(df, x='sub_category', y='total_net_sales', title='Total de Vendas por Modo de Envio', color='ship_mode', barmode='group')

st.plotly_chart(graf_barra)
