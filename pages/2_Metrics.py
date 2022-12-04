import streamlit as st
import numpy as np
from utils import display_model_metrics, display_data_metrics, display_overall_metrics, beta_image_grid

st.set_page_config(page_icon="📊",page_title="Project Metrics")
st.markdown('# Project Metrics')
st.write(
    """
    We have uploaded some important observations or visualisations that we captured while doing this Project.
    """
)
tab1, tab2, tab3 = st.tabs(["Overall Metrics", "Model Metrics", "Data Metrics"])

with tab1:
    st.header("Overall Metrics")
    display_overall_metrics()

with tab2:
    st.header("Model Metrics")
    st.write("These are the visualisations generated for model metrics.")
    display_model_metrics()
   
with tab3:
    st.header("Data Metrics")
    st.write("These are the visualisations generated for data metrics.")
    beta_image_grid()

