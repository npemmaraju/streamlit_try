import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



data=pd.read_csv('smoking.csv')
st.write(data.head())
data2=data.iloc[:,:2]
st.write(data2.head())


fig=px.pie(data, values='age', names='Unnamed: 0', title='Data')
st.plotly_chart(fig, use_container_width=True)

st.write('Out first app') 
col1, col2=st.columns(2)
with col1: 
    st.write("India")
with col2: 
    st.write("Bali")
st.markdown("Test")
st.sidebar.radio("Are you a student ", options=['yes', 'no'])

name=st.text_input('Name')
st.write(name)
age_input=st.number_input("Age")
st.write(age_input)
date=st.date_input('date')
st.write(date)
file=st.file_uploader('select a file')

# if file is not None: 
#     a=file.getvalue()
#     st.write(a)


tab1, tab2, tab3, tab4=st.tabs(['a', 'b', 'c', 'd'])
with tab1: 
    st.write('this is tab1')
with tab2:
    st.write('this is tab2')
with tab3: 
    st.write('this is rab3')
with tab4: 
    st.write('this is tab4')


#video: 

x=open('samplevideo.mp4', 'rb')
vi=x.read()
st.video(vi)

from PIL import Image
img=Image.open('photo.jpeg')
st.image(img)