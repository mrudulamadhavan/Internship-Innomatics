import streamlit as st
import pandas as pd
import pickle
import os
import plotly.express as px


st.header(":blue[Features vs Price]")

#resourses path
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)
data=df.copy()
data.drop("Price", axis=1, inplace=True)


feature=st.selectbox(
    "Choose any feature to see the relationship with Price of Laptop",
    (data.columns))

fig = px.box(df, x=feature, y='Price', color=feature)
st.plotly_chart(fig) # , use_container_width=True