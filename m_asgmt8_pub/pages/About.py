import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath("m_asgmt8_pub/pages/About.py"))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


st.header(":green[Problem Statement ]")
st.write('Assume you are on a vacation in the United Kingdom with your friends. For fun, you decided to go to the Pubs nearby for some drinks. Google Map is down because of some issues.')
st.write('While searching the internet, you came across https://www.getthedata.com/open-pubs. On this website, you found all the pub locations (Specifically Latitude and Longitude info).')
st.write('Create a web application using the pub location details to find the nearest pub.')
    
st.header(":green[Overview of Dataset]")
st.write("This dataset contain the details of all pubs located in United Kingdom.") 
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_new.csv")
df = pd.read_csv(DATA_PATH)
df = df[['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing',
       'latitude', 'longitude', 'local_authority']]
st.dataframe(df.head(5))


status = st.radio("Click to know more : ", ('Shape', 'Attributes','Summary','Descriptive Statistics'))
st.write('-----------------------------------------------------------------------------------')
if (status == 'Shape'):
    rows = df.count()[0]
    columns = df.shape[1] - 1
    st.text(f'Number of Rows  : {rows}')
    st.text(f' Number of Columns  : {columns}')
elif (status == 'Attributes'):
    st.write('* fsa_id : Food Standard Agency ID for the pub.') 
    st.write('* name : Name of the pub')
    st.write('* address : Address of pub')
    st.write('* postcode : Postcode of the pub')
    st.write('* easting')
    st.write('* northing') 
    st.write('* latitude') 
    st.write('* longitude') 
    st.write('* local_authority : Local authority for the pub')       
elif (status == 'Summary'):
    IMAGE_PATH2 = os.path.join(dir_of_interest, "images", "info.jpg")
    img = image.imread(IMAGE_PATH2)
    st.image(img)   
else:       
    x = df.describe(include = "object")
    st.table(x)
    y = df.describe()
    st.table(y)



def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

pub = convert_df(df)
st.write('-----------------------------------------------------------------------------------')
st.download_button(
    label="Download Dataset",
    data = pub,
    file_name='open_pubs_new.csv',
    mime='text/csv',
)




