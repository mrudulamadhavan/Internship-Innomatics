import streamlit as st
from matplotlib import image
import os

#Title of the home page
st.markdown("<h1 style='text-align: center; color: brown;'>💎 Diamond Price Predictor</h1>", 
            unsafe_allow_html=True)

st.write("")
st.markdown("""<p style='text-align: center; font-weight: bold; font-size: 18px;'>🔥 <em>Shine a light on your diamond’s true value — with AI.</em></p>
""", unsafe_allow_html=True)


#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt_prod/Home.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "dia2.jpg")

img = image.imread(IMAGE_PATH1)

# Center image with container trick
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(img, width=700)
st.markdown("</div>", unsafe_allow_html=True)


#Using subheader
st.write('By: **:green[Mrudula A P]**')






