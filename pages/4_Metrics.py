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
tab1, tab2, tab3, tab4 = st.tabs(["Overall Metrics", "Model Metrics", "Data Metrics", "Image Grid"])

with tab1:
    st.header("Overall Metrics")
    display_overall_metrics()

with tab2:
    st.header("Model Metrics")
    st.write("These are the visualisations that we had added for K-Nearest Neighbours Model in Phase-2.")
    display_model_metrics()

with tab3:
    st.header("Data Metrics")
    display_data_metrics()
   
with tab4:
    st.header("Beta imagegrid")
    beta_image_grid()

