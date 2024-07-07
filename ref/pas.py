import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df=pd.DataFrame(np.random.randn(20,3),columns=['li1','l2','l3'])
st.line_chart(df)
st.area_chart(df)

df=pd.read_csv('/Users/vaibhavahlawat/streamlit/ref/Dataset.csv')
st.dataframe(df)
fig=plt.figure(figsize=(15,8))
df['month_number'].value_counts().plot(kind= 'pie')
st.pyplot(fig)

fig=plt.figure(figsize=(15,8))
sns.distplot(df['month_number'])
st.pyplot(fig)