#Importing Libraries
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

#import model
st.title("Laptop Price Predictor 💻")

# C:\Users\Mrudula Madhavan\OneDrive\Desktop\Innomatics\m_asgmt7_laptop\Resources\data\laptop_price.csv
#resources path
FILE_DIR1 = os.path.dirname(os.path.abspath("m_asgmt7_laptop/pages/predictor.py"))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data")

#Load data
DATA_PATH1=os.path.join(DATA_PATH, "laptop_price.csv")
df=pd.read_csv(DATA_PATH1)
data=df.copy()
data.drop('Processor', axis=1, inplace=True)

# -------------------------------------------------------------------------------------------------------
# making 3 cols left_column,  right_column
left_column, right_column = st.columns(2)
with left_column:
    # brand input
    brand = st.selectbox("Brand Name", df["Brand"].unique())

with right_column:
    #os input
    osys=st.selectbox("Operating System",df["Operating System"].unique())


# making 2 cols left_column, right_column
left_column, right_column = st.columns(2)
with left_column:
    # Ram type
    ramtype = st.selectbox("RAM Type", df["RAM Type"].unique())

with right_column:
    # Ram size
    ramsize = st.selectbox("RAM Size", df["RAM Size"].unique())

# making 2 cols left_column, right_column
left_column,  right_column = st.columns(2)
with left_column:
    # disctype input
    disctype = st.selectbox("Disc Type", df["Disc Type"].unique())

with right_column:
    # discsize input
    discsize = st.selectbox("Disc Size", df["Disc Size"].unique())

# -------------------------------------------------------------------------------------------------------------------
#Create dataframe using all these values
sample=pd.DataFrame({"Brand":[brand],"Operating System":[osys],
                   "RAM Type":[ramtype], "RAM Size":[ramsize],
                   "Disc Type":[disctype], "Disc Size":[discsize]})

# -----------------------------------------------------------------------------------------------------------------------
#Convert these values to suitable integer form
#Function to change brand to number
def replace_brand(brand):
    if brand=='Lenovo':
        return 1
    elif brand=='ASUS':
        return 2
    elif brand=='HP':
        return 3
    elif brand=='DELL':
        return 4
    elif brand=='RedmiBook':
        return 5
    elif brand=='Realme':
        return 6
    elif brand=='Acer':
        return 7
    elif brand=='MSI':
        return 8
    elif brand=='APPLE':
        return 9
    elif brand=='Infinix':
        return 10
    elif brand=='SAMSUNG':
        return 11
    elif brand=='Ultimus':
        return 12
    elif brand=='Vaio':
        return 13
    elif brand=='GIGABYTE':
        return 14
    elif brand=='Nokia':
        return 15
    elif brand=='ALIENWARE':
        return 16  
data['Brand']=data['Brand'].apply(replace_brand)

#Function to change os to number
def replace_os(os):
    if os=='Windows 11':
        return 1
    elif os=='Windows 10':
        return 2
    elif os=='MAC ':
        return 3
    elif os=='Chrome':
        return 4
    elif os=='DOS':
        return 5
data['Operating System']=data['Operating System'].apply(replace_os)

#Function to change ram type to number
def replace_ram_type(ram_type):
    if ram_type=='DDR4':
        return 1
    elif ram_type=='DDR5':
        return 2
    elif ram_type=='LPDDR4':
        return 3
    elif ram_type=='Unified Memory':
        return 4
    elif ram_type=='LPDDR4X':
        return 5
    elif ram_type=='LPDDR5':
        return 6
    elif ram_type=='LPDDR3':
        return 7   
data['RAM Type']=data['RAM Type'].apply(replace_ram_type)

#Function to change ram size to number
def replace_ram_size(ram_size):
    if ram_size=='8 GB':
        return 1
    elif ram_size=='16 GB':
        return 2
    elif ram_size=='4 GB':
        return 3
    elif ram_size=='32 GB':
        return 4
data['RAM Size']=data['RAM Size'].apply(replace_ram_size)

#Function to disc type to number
def replace_disc_type(disc_type):
    if disc_type=='SSD':
        return 1
    elif disc_type=='HDD':
        return 2
    elif disc_type=='EMMC':
        return 3
data['Disc Type']=data['Disc Type'].apply(replace_disc_type)

#Function to change disc size to number
def replace_disc_size(disc_size):
    if disc_size=='256 GB':
        return 1
    elif disc_size=='512 GB':
        return 2
    elif disc_size=='1 TB':
        return 3
    elif disc_size=='128 GB':
        return 4
    elif disc_size=='64 GB':
        return 5
    elif disc_size=='32 GB':
        return 6
    elif disc_size=='2 TB':
        return 7
data['Disc Size']=data['Disc Size'].apply(replace_disc_size)

#Split data into X and y
X=data.drop('Price', axis=1).values
y=data['Price'].values

#Standarizing the features
std=StandardScaler()
std_fit=std.fit(X)
X=std_fit.transform(X)

#Train the model
xgb=XGBRegressor(learning_rate=0.15, n_estimators=50, max_leaves=0, random_state=42)
xgb.fit(X,y)

#Convert User input to suitable integer form
sample['Brand']=sample['Brand'].apply(replace_brand)
sample['Operating System']=sample['Operating System'].apply(replace_os)   
sample['RAM Type']=sample['RAM Type'].apply(replace_ram_type)
sample['RAM Size']=sample['RAM Size'].apply(replace_ram_size)
sample['Disc Type']=sample['Disc Type'].apply(replace_disc_type)
sample['Disc Size']=sample['Disc Size'].apply(replace_disc_size)

#Standardize the features
sample=sample.values
sample=std_fit.transform(sample)

#Prediction
if st.button('Predict Price', key = "<uniquevalueofsomesort>"):
    price=xgb.predict(sample)
    price=price[0].round(2)    
    st.subheader(":blue[The Predicted Price of Laptop is :] :green[{}]".format("₹"+str(price)))
else:
    pass




















