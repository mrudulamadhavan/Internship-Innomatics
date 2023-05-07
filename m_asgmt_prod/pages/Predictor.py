#Importing Libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from matplotlib import image

import warnings 
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Diamond Price Predictor",layout="wide")

#import model
# st.title("Diamond Price Predictor ")


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath("m_asgmt_prod/pages/Predictor.py"))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
#Load data
DATA_PATH = os.path.join(dir_of_interest, "data", "diamonds.csv")
df= pd.read_csv(DATA_PATH)
df1=df.copy()


xgb = pickle.load(open('m_asgmt_prod/diamond.pkl','rb'))


def prediction(cut,color,clarity,x,y,z,carat,depth,table):
    prediction = xgb.predict([[cut,color,clarity,x,y,z,carat,depth,table]])
    print(prediction)
    return prediction


st.subheader("Enter the Diamond details :")
img = image.imread('m_asgmt_prod/resources/images/dia3.jpg')
st.image(img)

left_column,middle_column, right_column = st.columns(3)
with left_column:  
    cut = st.selectbox("Cut Quality", df["cut"].unique())
with middle_column:
    color = st.selectbox("Color", df["color"].unique())
with right_column:
    clarity = st.selectbox("Clarity", df["clarity"].unique())

left_column, middle_column, right_column = st.columns(3)
with left_column:
    carat = st.text_input("Weight / Carat  ",value=0.0) 
with middle_column:
    depth = st.text_input("Depth percentage ",value=0)
with right_column:
    table = st.text_input("Table Percentage  ",value=0)

left_column,middle_column, right_column = st.columns(3)
with left_column:
    x = st.number_input("Length in mm ")
with middle_column:
    y = st.number_input("Width in mm ")
with right_column:
    z = st.number_input("Depth in mm )")
price = ""


#Create dataframe using all these values
sample=pd.DataFrame({"cut":[cut],"color":[color],"clarity":[clarity],
                    "x":[x],"y":[y],"z":[z],
                "carat":float(carat),"depth":float(depth), "table":float(table)})

# Convert these values to suitable integer form
# Function to change clarity
def clarity_fn(clarity):
    if clarity=='I1':
        return 0.0
    elif clarity=='SI2':
        return 1.0
    elif clarity=='SI1':
        return 2.0
    elif clarity=='VS2':
        return 3.0
    elif clarity=='VS1':
        return 4.0
    elif clarity=='VVS2':
        return 5.0
    elif clarity=='VVS1':
        return 6.0  
    elif clarity=='IF':
        return 7.0
df1['clarity']=df1['clarity'].apply(clarity_fn)
sample['clarity']=sample['clarity'].apply(clarity_fn)

#Function to change cut quality
def cut_qlty(cut):
    if cut=='Fair':
        return 0.0
    elif cut=='Good':
        return 1.0
    elif cut=='Ideal':
        return 2.0
    elif cut =='Premium':
        return 3.0
    elif cut =='Very Good':
        return 4.0
df1['cut']=df1['cut'].apply(cut_qlty)
sample['cut']=sample['cut'].apply(cut_qlty)

#Function to change cut quality
def color_fn(color):
    if color=='D':
        return 0.0
    elif color=='E':
        return 1.0
    elif color=='F':
        return 2.0
    elif color =='G':
        return 3.0
    elif color =='H':
        return 4.0
    elif color =='I':
        return 5.0
    elif color =='J':
        return 6.0
df1['color']=df1['color'].apply(color_fn)
sample['color']=sample['color'].apply(color_fn)


#Split data into X and y
X=df1.drop('price', axis=1).values
y=df1['price'].values

#Standarizing the features
scaler=StandardScaler()
std_fit=scaler.fit(X)
X=std_fit.transform(X)

#Train the model
xgb=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=42)
xgb.fit(X,y)


#Convert User input to suitable integer form
sample['clarity']=sample['clarity'].apply(clarity_fn)
sample['cut']=sample['cut'].apply(cut_qlty)
sample['color']=sample['color'].apply(color_fn)

#Standardize the features
sample=sample.values
sample=std_fit.transform(sample)

#Prediction
if st.button('Predict Price'):
    price=xgb.predict(sample)
    price=price[0].round(2)    
    st.subheader(":blue[The Predicted Price is :] :green[{}]".format("$ "+str(price)))
else:
    pass












