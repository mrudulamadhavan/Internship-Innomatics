import streamlit as st
from matplotlib import image
import os

#Title of the home page
st.header(":blue[Diamond Price Predictor Application ]")


#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt_prod/Home.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "dia2.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

#Using subheader
st.write('By: :green[Mrudula A P]')






