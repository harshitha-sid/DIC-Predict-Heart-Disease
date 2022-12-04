import streamlit as st
import base64
from utils import load_lottieurl
from streamlit_lottie import st_lottie

HEART_IMAGE = "images/sidebar_heart.gif"
lottie_url_hello = "https://assets8.lottiefiles.com/packages/lf20_hqlvpwat.json"

pages = st.source_util.get_pages('Welcome.py')

new_page_names = {
  '1_Predict Heart Disease': '1_🫀_Predict Heart Disease',
  '2_Phase-1 Report': '2_📕_Phase-1 Report',
  '3_Phase-2 Report': '3_📗_Phase-2 Report',
  '4_Metrics': '4_📈_Metrics'
}

for key, page in pages.items():
  if page['page_name'] in new_page_names:
    page['page_name'] = new_page_names[page['page_name']]

st.set_page_config(layout="wide",initial_sidebar_state="collapsed",page_icon="images/heart-icon.png",page_title="App Predicting Heart Disease")

st.write("# Welcome to our Heart Disease Prediction Project!👋")

with open("images/heart-rate.gif", "rb") as file_:
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="heart rate gif" width=100% height=150>',
    unsafe_allow_html=True,
)

st.info("👈 Select an option from the sidebar")

col1, col2 = st.columns([1,3])

with col1:
  lottie_hello = load_lottieurl(lottie_url_hello)
  st_lottie(lottie_hello, key="hello", height = 400, width = 350, quality = "high")

with col2:
  st.markdown(
      """
      ### Worried about your heart's health ?

      You need not worry as you are in the right place ! This app can help in predicting the probability of you getting a heart disease or not within seconds.

      Here, we are using XGBoost machine learning model on a survey data of over 300k US residents collected by CDC.

      To predict the chances of you getting a heart disease, just click on the "Predict Heart Disease" option from the sidebar and enter the parameters that best describe you. And click "Predict" button.
      

      ### Team Members

      - Abhi Vijayakumar **(UBIT: vijayak2)**
      - Harshitha Siddaramaiah **(UBIT: hsiddara)**
  """, unsafe_allow_html=True
  )

  st.warning(
      """
      **Disclaimer**: Note that these results are not equivalent to that of medical diagnosis. Hence, take it with a grain of salt.
      If the app predicts that you have a chance of getting a heart disease, please consult a doctor.
      """)