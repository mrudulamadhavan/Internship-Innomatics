import streamlit as st
from PIL import Image
from matplotlib import image
import os

#Title of the home page
st.header(":blue[Laptop Price Predictor Application :desktop_computer]")


#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath('C://Users//Mrudula Madhavan//OneDrive//Desktop//Innomatics//m_asgmt7_laptop//homepage.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "pic1.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

#Using subheader
st.write('By: :green[Mrudula A P]')