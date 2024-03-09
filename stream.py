import streamlit as st
import pandas as pd
import os

folder = os.getcwd()
print(folder)
df = pd.read_excel(folder+'/2024 PROJECTIONS.xlsx')
st.dataframe(df)
