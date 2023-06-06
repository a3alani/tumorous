import streamlit as st
import numpy as np
import pandas as pd
from keras import models
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
from io import BytesIO

model = models.load_model("ali_model")

st.title("Liver Tumor Detection")
st.caption("Latest Update: 2023-06-02")
st.write("This is a project by Ali, Samuel, Nathaphat. We are a team under \
Data Science Student Society at University of California, San Diego.")

def create_mask(pred_mask):
    pred_mask = tf.math.argmax(pred_mask, axis=-1)
    pred_mask = pred_mask[..., tf.newaxis]
    return pred_mask[0]

st.header("Prediction")
uploaded_file = st.file_uploader("Choose a image file", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
    expanded_image = np.expand_dims(image, axis=0)
    resized_image = np.resize(expanded_image, (1, 512, 512, 3))
    prediction = model.predict(resized_image)
    prediction = np.resize(prediction.squeeze(), image.shape)
    pred = np.resize(create_mask(prediction).numpy(), image.shape)
    col1, col2 = st.columns(2)
    with col1:
        st.caption("Input image")
        st.image(image)
    with col2:
        st.caption("Prediction")
        st.image(prediction, clamp=True, channels='RGB')
    buf = BytesIO()
    img = Image.fromarray(prediction.astype('uint8'), 'RGB')
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    btn = st.download_button(label="Download Prediction", data=byte_im,
                             file_name="imagename.png", mime="image/png")
st.divider()
st.write("Any issues? Contact: hsl023@ucsd.edu")
