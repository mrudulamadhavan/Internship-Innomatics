import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="Pub Locator"
)

FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt8_pub//HomePage.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_new.csv")
df = pd.read_csv(DATA_PATH,index_col=False)
df = df[['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing',
       'latitude', 'longitude', 'local_authority']]

# make header
st.header("🍸🍷 :blue[ Pub Locator ] 🍸🍷")

st.write('How many nearby pubs you look for :')
n = st.slider("",1, 20)
st.write('Number of Pubs selected :',n)

st.subheader(" Current Location Details :")
lat = st.number_input('Latitude :')
lon = st.number_input('Longitude :')
button = st.button("Submit")
df_new = df[['latitude', 'longitude']]
new_points = np.array([lat, lon])
# Calculate distance between new_points and all points in df_new
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))
distances = pd.Series(distances, name="min_distance")

st.write("-----------------------------------------------------------------------------------------")

# sort the array using arg partition and keep n elements
# n = 5

min_indices = np.argpartition(distances,n-1)[:n]

if button:
    st.subheader(" :black[ Pubs Near Me :]")
    st.dataframe(df.iloc[min_indices].reset_index(drop=True))    
    st.map(df.iloc[min_indices])
    st.write(">> Minimum distances to each Pub :")    
    st.dataframe(distances.head(n).reset_index(drop=True))
