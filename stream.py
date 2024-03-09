import streamlit as st
import pandas as pd
import os

@st.cache
def load_data():
    folder = os.getcwd()
    # Load your Excel file here
    data = pd.read_excel(folder+'/2024 PROJECTIONS.xlsx')
    return data

# Load the data only once during deployment
data = load_data()

# Use the loaded data in your app
st.write(data)