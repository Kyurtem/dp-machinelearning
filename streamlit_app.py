import streamlit as st
import pandas as pd

st.title('🍷🍷🍷 Machine learning Wine stadistic 🍷🍷🍷 lo mejor de lo mejor')
st.info('Esta es un app que nos permite ver las estadistica de los catadores de vino')

df = pd.read_csv('winequality-red.csv')
df 
