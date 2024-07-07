import streamlit as st
import pandas as pd
# df=st.file_uploader('bshnsbb:', type=['csv','jpg'])
# if(df!=None):
#     dg=pd.read_csv(df)
#     st.table(dg.head())
    
dk=st.file_uploader('shu',type=['jpg'])
if(dk!=None):
    st.image(dk)