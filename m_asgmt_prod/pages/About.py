import streamlit as st
from matplotlib import image
import pandas as pd

import os

#Adding Image
# FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt_prod/pages/About.py'))
# dir_of_interest = os.path.join(FILE_DIR, "resources")
# IMAGE_PATH = os.path.join(dir_of_interest, "images", "dia1.jpg")

# Diamond Price Predictor Header
# Diamond Price Predictor Header
st.markdown("<h1 style='text-align: center; color: brown;'>💎 Diamond Price Predictor</h1>", unsafe_allow_html=True)

st.markdown("#### **Ever wondered what your diamond is really worth?** ")
st.markdown("""This app uses **machine learning** to predict diamond prices based on key features like:

- 💠 **Carat** (weight)  
- ✂️ **Cut** (quality)  
- 🌈 **Color**  
- 🔍 **Clarity**  
- 📐 **Dimensions** *(x, y, z)*  
""")
st.write("")
# Load and display image (adjust the path as needed)
img_path = 'm_asgmt_prod/resources/images/dia1.jpg'
st.image(img_path,caption="Diamond Anatomy",  use_container_width=False)

# Three-column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### ⚙️ Built Using")
    st.markdown("""
    - Python  
    - Pandas  
    - Scikit-learn  
    - XGBoost  
    - Random Forest  
    - Streamlit  
    """)

with col2:
    st.markdown("#### 💡 Use Cases")
    st.markdown("""
    - Buyers & sellers verifying diamond value  
    - Jewelers pricing inventory  
    - ML learners exploring regression use-cases  
    """)

with col3:
    st.markdown("#### 📈 Model Accuracy")
    st.markdown(""" - 98.05% R² (Random Forest)""")
st.write("")
st.markdown("""<p style="text-align: center; font-weight: bold; font-size: 20px;">✨ <em>Smart pricing for sparkling stones. ✨</em></p>""", unsafe_allow_html=True)
