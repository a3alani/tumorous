import streamlit as st
import numpy as np
import cv2
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

st.title("Tumorous Detection")

def main():
    file_uploaded = st.file_uploader('Image Uploader', type=['jpg', 'png', 'jpeg'])
    if file_uploaded is not None:
        image = Image.open(file_uploaded)
        fig = plt.figure()
        plt.imshow(image)
        plt.axis("off")
        st.pyplot(fig)

if __name__ == "__main__":
    main()