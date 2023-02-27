import streamlit as st
from matplotlib import image
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath("C://Users//Mrudula Madhavan//OneDrive//Desktop//Innomatics//m_asgmt1//pages//dataanalysis.py"))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

st.title(":blue[Exploratory Data Analysis]")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "spend.jpg")
img = image.imread("C://Users//Mrudula Madhavan//OneDrive//Desktop//Innomatics//m_asgmt1//resources//images//spend.jpg")
st.image(img)

st.subheader(":green[Overview of Dataset]")
DATA_PATH = os.path.join(dir_of_interest, "data", "Credit card transactions - India - Simple.csv")
df = pd.read_csv('C://Users//Mrudula Madhavan//OneDrive//Desktop//Innomatics//m_asgmt1//resources//data//Credit card transactions - India - Simple.csv')
df = df.drop(columns='index')
st.dataframe(df.head(8))

st.subheader(":green[Data Visualization]")
df[['Year', 'Month', 'Day']] = df['Date'].str.split("-", expand=True)
df.drop(['Day', 'Year'], axis=1, inplace=True)



col1, col2 = st.columns(2)

fig_1 = px.histogram(df,x='Card Type', marginal='box', nbins=47, title='Distribution of Card Type')
fig_1.update_layout(bargap=0.2)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.histogram(df,x='Exp Type',marginal='box', nbins=47,color_discrete_sequence=['violet'],
                title='Distribution of Expenditure Types')
fig_2.update_layout(bargap=0.1)
col2.plotly_chart(fig_2, use_container_width=True)

df[['City', 'Country']] = df['City'].str.split(',', expand=True)
df = df.drop(['Country'], axis=1)
z = df.groupby('City', as_index=False)[['Amount']].sum().rename({'Amount' : 'Amount spent'}, axis=1).sort_values(by='Amount spent',ascending=False)
fig_3=px.bar(z[:10],x='City',y='Amount spent',color='City',
           labels={'City':'City','Amount spent':'Number of transactions'},template='seaborn' ,title="Top 10 Cities with high spending behaviour")
fig_3.update_layout(bargap=0.3)
st.plotly_chart(fig_3, use_container_width=True)


col3,col4 = st.columns(2)

e = df.groupby('Exp Type', as_index=False)[['Amount']].sum().rename({'Amount' : 'Amount sum'}, axis=1)
fig_4=px.pie(e,names='Exp Type',values='Amount sum',color='Exp Type',hole=0.7,labels={'Exp Type':'Expense Type','Amount sum':'Number of transactions'}
        ,template='seaborn',title='Total credit card transactions by Expense type')
fig_4.update_layout(title_x=0.05)
col4.plotly_chart(fig_4, use_container_width=True)

z = df.groupby('Gender', as_index=False)[['Amount']].sum().rename({'Amount' : 'Amount sum'}, axis=1)
fig_5=px.pie(z,names='Gender',values='Amount sum',color='Gender',hole=0.4,labels={'Gender':'Gender','Amount sum':'Number of transactions'}
    ,template='seaborn',title='Total of credit card transactions by Gender')
fig_5.update_layout(title_x=0.1)
col3.plotly_chart(fig_5, use_container_width=True)




cardtype = st.selectbox("Select the Card Type:", df['Card Type'].unique())
col1, col2 = st.columns(2)
fig_1 = px.bar(df,x='Card Type',y="Amount" , title='Distribution of Card Type in transactions')
fig_1.update_layout(bargap=0.2)
col1.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df[df['Card Type'] == cardtype], y="Amount")
col2.plotly_chart(fig_2, use_container_width=True)

exptype = st.selectbox("Select the Expense Type:", df['Exp Type'].unique())
col3, col4 = st.columns(2)
fig_3 = px.bar(df,x='Exp Type',y="Amount" , title='Distribution of Expense Category in transactions')
fig_3.update_layout(bargap=0.2)
col3.plotly_chart(fig_3, use_container_width=True)
fig_4 = px.box(df[df['Exp Type'] == exptype], y="Amount")
col4.plotly_chart(fig_4, use_container_width=True)

exptype = st.selectbox("Select the Gender Type:", df['Gender'].unique())
col5, col6 = st.columns(2)
fig_3 = px.bar(df,x='Gender',y="Amount" , title='Distribution of Gender in transactions')
fig_3.update_layout(bargap=0.2)
col5.plotly_chart(fig_3, use_container_width=True)
fig_4 = px.box(df[df['Gender'] == exptype], y="Amount")
col6.plotly_chart(fig_4, use_container_width=True)



st.header(":green[Insights : ]")
st.write("* Females used the Silver card type were as male have used the platinum card types more")
st.write("* Silver card types were most preferred credit card in the payments.") 
st.write("* In Fuel and Food expenses were most counts paid by the cards.") 
st.write("* Bengaluru ,Greater Mumbai, Ahmedabad, Delhi are the Top 4 Cities were card usage were more.")
st.write("* Females were more depend on credit cards as they spend more amount on credit cards than men.")
st.write("* Females and Males mostly spend amount on Bills and Food using credit card.")
st.write("* Males spend the highest amount with Platinum card type and Females spend the highest amount with Silver card type.")
st.write("* In Greater Mumbai females spends were highest were as males spends were highest in Ahmedabad.")
st.write("* The amount gathered by bills payment is the highest compared to other expense types")




st.header(":red[Thank You] :smile:")
