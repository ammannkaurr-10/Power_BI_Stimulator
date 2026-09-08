import streamlit as st 
import pandas as pd 
st.title("data upload and preview")
file = st.file_uploader("Upload your CSV file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.head())