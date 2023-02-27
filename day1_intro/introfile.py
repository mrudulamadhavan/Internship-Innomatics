import streamlit as st
from matplotlib import image 


st.title(":red[Data Science Internship] (Feb 2023)")
st.header(":black[_@ Innomatics Research Labs_]")
st.subheader(" :sunglasses: :smile: :sunglasses:")


pic = image.imread('desk_img.jpg')
st.image(pic)