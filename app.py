import streamlit as st
import numpy as np
st.title("Laptop Predictor")
#import model
import pickle
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))
#brand
brand=st.selectbox('Select Brand',df['Company'].unique())
#type of laptop
laptop_type=st.selectbox('Select Type',df['TypeName'].unique())
#ram
ram=st.selectbox('Select RAM(in GB)',[2,4,6,8,12,16,24,32,64])
#Weight
weight=st.number_input('Weight of Laptop')
#Touchscreen
touchscreen=st.selectbox('Touchscreen?',['No','Yes'])
#IPS
ips=st.selectbox('IPS?',['No','Yes'])
#screen size
screen_size=st.number_input('Screen Size')
# CPU Brand
cpu=st.selectbox('Select CPU Brand',df['Cpu Brand'].unique())
#resolution
resolution=st.selectbox('Select Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
#hdd
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
#ssd
ssd=st.selectbox('SSD(in GB)',[0,8,16,32,64,128,256,512,1024])
#gpu
gpu=st.selectbox('Select GPU Brand',df['Gpu brand'].unique())
#os
os=st.selectbox('Select OS',df['os'].unique())
#predict button
if st.button('Predict Price'):
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1
    else:
        ips=0
    X_res=int(resolution.split('x')[0])
    Y_res=int(resolution.split('x')[1])
    ppi=((X_res**2)+(Y_res**2))**0.5/screen_size

    import pandas as pd

    query = pd.DataFrame([{
        'Company': brand,
        'TypeName': laptop_type,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'IPS': ips,
        'ppi': ppi,
        'Cpu Brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])



    st.title("The predicted price of this configuration is Rs. "+str(int(np.exp(pipe.predict(query)[0]))))


