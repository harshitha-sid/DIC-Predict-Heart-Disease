import streamlit as st
import base64

st.set_page_config(page_icon="📗",page_title="Phase-2 Report")

PHASE_2_PDF = "images/Phase2.pdf"

@st.cache
def display_phase2_report():
    with open(PHASE_2_PDF,"rb") as f:
                st.info("Phase 2 Report")
                ph2_pdf = base64.b64encode(f.read()).decode('utf-8')
                ph2_pdf_display = f'<iframe src="data:application/pdf;base64,{ph2_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
                st.markdown(ph2_pdf_display, unsafe_allow_html=True)

display_phase2_report()