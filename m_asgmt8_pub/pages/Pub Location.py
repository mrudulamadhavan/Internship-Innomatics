import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="Pub Locations"
)

FILE_DIR = os.path.dirname(os.path.abspath('m_asgmt8_pub//HomePage.py'))
dir_of_interest = os.path.join(FILE_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "open_pubs_new.csv")
df = pd.read_csv(DATA_PATH,index_col=False)
df = df[['fsa_id', 'name', 'address', 'postcode', 'easting', 'northing',
       'latitude', 'longitude', 'local_authority']]


# make header

st.header(" 🍷 :blue[Pub Locations in UK] 🍷")
# enter either postal code or local authority

local_auth = st.selectbox('Choose a Local Authority :', set(df['local_authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['local_authority'] == local_auth)]
    st.write("Pubs in this area: ")
    st.dataframe(df_new.reset_index(drop=True))
    st.map(df_new)
