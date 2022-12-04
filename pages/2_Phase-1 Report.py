import streamlit as st
import base64

st.set_page_config(page_icon="📕",page_title="Phase-1 Report")

PHASE_1_PDF = "images/Phase1.pdf"

@st.cache
def display_phase1_report():
    with open(PHASE_1_PDF,"rb") as f:
                st.info("Phase 1 Report")
                ph1_pdf = base64.b64encode(f.read()).decode('utf-8')
                ph1_pdf_display = f'<iframe src="data:application/pdf;base64,{ph1_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
                st.markdown(ph1_pdf_display, unsafe_allow_html=True)


display_phase1_report()