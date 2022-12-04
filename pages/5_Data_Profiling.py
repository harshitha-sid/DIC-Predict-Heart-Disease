import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

@st.cache
def display_pandas_profiler():
    df = pd.read_csv("data/heart_dic_dataset.csv")
    pr = df.profile_report()
    st_profile_report(pr)

display_pandas_profiler()