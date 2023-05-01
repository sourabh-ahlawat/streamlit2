import pandas as pd
import streamlit as st
import numpy as np 
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["harsh","sourabh"],
    "age":23,
    "city":"noida"
}

data = pd.read_csv("STTM_master_data_XCFEquipmentPlanningMaintenanaceAssignment.csv")

st.dataframe(data,width=100,height=100)

#st.table(data)

st.json(dic)
st.write(data)


#caching in streamlit.
@st.cache
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())
    
if st.checkbox("2"):
    st.write(ret_time())    