import streamlit as st
import numpy as np
import pandas as pd

st.title("Tumorous detection!")

st.write("This is a project")
## Hello
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    st.write(str(type(uploaded_file)))
