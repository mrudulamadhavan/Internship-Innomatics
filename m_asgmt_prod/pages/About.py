import streamlit as st
from matplotlib import image
import pandas as pd

import os

#Adding Image
# FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt_prod/pages/About.py'))
# dir_of_interest = os.path.join(FILE_DIR, "resources")
# IMAGE_PATH = os.path.join(dir_of_interest, "images", "dia1.jpg")

# Diamond Price Predictor Header
st.markdown("<h1 style='text-align: center;'>💎 Diamond Price Predictor</h1>", unsafe_allow_html=True)

st.markdown("### 📖 About the Project")
st.markdown("""**Ever wondered what your diamond is really worth?**)  
st.markdown("""This app uses **machine learning** to predict diamond prices based on key features like:

- 💠 **Carat** (weight)  
- ✂️ **Cut** (quality)  
- 🌈 **Color**  
- 🔍 **Clarity**  
- 📐 **Dimensions** *(x, y, z)*  
""")

img = image.imread('m_asgmt_prod/resources/images/dia1.jpg')
st.image(img)

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### ⚙️ Built Using")
    st.markdown("""
    - Python  
    - Pandas  
    - Scikit-learn  
    - XGBoost  
    - Random Forest  
    - Streamlit

    
    """)

with col2:
    st.markdown("### 💡 Use Cases")
    st.markdown("""
    - Buyers & sellers verifying diamond value  
    - Jewelers pricing inventory  
    - ML learners exploring regression use-cases  
    """)
    st.markdown("### 📈 **Best Model Accuracy**:")  
    st.markdown("""**98.05% R² (Random Forest)**""")
 
