import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

ch=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','f'])
chart=alt.Chart(ch).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','f'])
st.altair_chart(chart)
