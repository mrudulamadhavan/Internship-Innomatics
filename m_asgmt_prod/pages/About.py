import streamlit as st
from matplotlib import image
import pandas as pd

import os

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt_prod/pages/About.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "dia1.jpg")

img = image.imread(IMAGE_PATH)
st.image(img)


st.write("* price - price in US dollars (\$326 to \$18,823)")

st.write("* carat  - weight of the diamond (0.2 to 5.01)")
st.write("* cut - quality of the cut (Fair, Good, Very Good, Premium, Ideal)")
st.write("* color - diamond colour, from J (worst) to D (best)")
st.write("* clarity - a measurement of how clear the diamond is .")
st.write(" >>  I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best) ")

st.write("* x - length in mm (0 to 10.74)")
st.write("* y - width in mm (0 to 58.9)")
st.write("* z - depth in mm (0 to 31.8)")

st.write("* depth - total depth percentage (43 to 79)")
st.write(" >>  depth = z / mean(x, y) = 2 * z / (x + y) ")
st.write("* table - width of top of diamond relative to widest point (43 to 95)")
