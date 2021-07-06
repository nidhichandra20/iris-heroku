import streamlit as st
st.write("Helllo world")
st.header("hiiiiiiii")
for x in range(10):

	st.write("this is coolr")
import pandas as pd
df=pd.DataFrame(data=[1,2,3,4,5,676,7], columns=["numbers"])
st.table(df.head())

