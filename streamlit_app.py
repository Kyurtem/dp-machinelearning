import streamlit as st
import pandas as pd

st.title('🍷🍷🍷 Machine learning Wine stadistic 🍷🍷🍷 lo mejor de lo mejor')
st.info('Esta es un app que nos permite ver las estadistica de los catadores de vino')

with st.expander('Dataset'):
  st.write('**Datos de muestra**')
  df = pd.read_csv('winequality-red.csv')
  df

st.write('**X**')
X = df.drop('quality', axis=1)
x

st.write('**Y**')
Y = df.quality
Y

with st.expander('Data Visualition')
st.scatter_chart(data=df, x='alcohol', y='pH', color='quality')
