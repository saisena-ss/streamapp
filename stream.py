import streamlit as st
import pandas as pd
import os

@st.cache_resource
def load_data():
    folder = os.getcwd()
    # Load your Excel file here
    data = pd.read_csv(folder+'/samp.csv')
    return data

# Load the data only once during deployment
data = load_data()

# Use the loaded data in your app
st.write(data)