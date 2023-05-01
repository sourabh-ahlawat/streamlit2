import pandas as pd
import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
import altair as alt


data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
    
)

plt.scatter(data['a'],data['b'])
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)
