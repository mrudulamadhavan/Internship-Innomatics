import streamlit as st
from matplotlib import image 


st.title("My Portfolio ! 👋")
st.header(":red[Mrudula A P]")
st.subheader("Datascience intern :blue[ @ Innomatics Research Labs].")


st.write("* Dedicated and detail-oriented early career Data Science and Machine Learning enthusiast who is determined for data analyst and data scientist roles.")
st.write("* I have good knowledge and hands on experience in data analysis tools like Excel (Advanced), SQL(Advanced), PostgreSQL , Statistics, Mathematics , Python programming language and data visualization tools like Tableau & Power BI.")


st.subheader("_Let's Explore my works_..:sunglasses:")
btn_click = st.button("Click here!")
if btn_click == True:
    st.success('Loading....!', icon="✅")
    st.balloons()