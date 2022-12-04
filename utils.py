import streamlit as st
import requests
import os
from streamlit_lottie import st_lottie

def display_result(predict_heart_disease, prediction_prob):
    unhealthy_heart = "https://assets6.lottiefiles.com/packages/lf20_pjzyfedu.json"
    healthy_heart = "https://assets5.lottiefiles.com/private_files/lf30_afaxd43w.json"

    if predict_heart_disease == 0:
        st.success(f"✔️ You seem to be fine, the probabilty of you having a heart disease is {prediction_prob} %")
        st.balloons()
        st.snow()
        healthy = load_lottieurl(healthy_heart)
        st_lottie(healthy, key="hello", height = 200, width = 200, quality = "high")

    elif predict_heart_disease == 1:
        st.warning(f"🚨 You seem to have an unhealthy heart, the probabilty of you having a heart disease is {prediction_prob} %")
        unhealthy = load_lottieurl(unhealthy_heart)
        st_lottie(unhealthy, key="hello", height = 200, width = 200, quality = "high")
        st.info("Go here to get more details on how you can get your heart right")
        display_yt_video()

def display_yt_video():
    VIDEO_URL = "https://www.youtube.com/watch?v=NVPSyZU5cro"
    st.video(VIDEO_URL)
        
def display_model_metrics():
    MODEL_METRICS_PATH = "metrics/Model/"
    model_metrics_pic_list = os.listdir(MODEL_METRICS_PATH)
    for pic in [MODEL_METRICS_PATH + i for i in model_metrics_pic_list]:
        st.image(pic)

def display_data_metrics():
    DATA_METRICS_PATH = "metrics/Data/"
    data_metrics_pic_list = os.listdir(DATA_METRICS_PATH)
    for pic in [DATA_METRICS_PATH + i for i in data_metrics_pic_list]:
        st.image(pic)

def display_overall_metrics():
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows in Test Data", "319,795")
    col2.metric("AOC", "0.88")
    col3.metric("Accuracy", "79%")
    
def beta_image_grid():
    from itertools import cycle
    DATA_METRICS_PATH = "metrics/Data/"
    data_metrics_pic_list = os.listdir(DATA_METRICS_PATH)

    filteredImages = [DATA_METRICS_PATH + i for i in data_metrics_pic_list]
    caption = [str(i) for i in range(18)] 
    cols = cycle(st.columns(3)) #since 18 images so i chose 3 columns
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(filteredImage, caption=caption[idx])

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()