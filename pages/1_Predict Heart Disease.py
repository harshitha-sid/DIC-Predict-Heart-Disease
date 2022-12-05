import streamlit as st
import pandas as pd
import _pickle as cPickle
import numpy as np
from utils import display_result
import time 
import random
import base64
import pickle


st.set_page_config(page_icon="images/heart-icon.png",page_title="Predict Heart Disease")

@st.cache   
def load_model(MODEL_PATH):
     with open(MODEL_PATH, 'rb') as fid:
         adaboost_model = cPickle.load(fid)
     return adaboost_model

def BMICheck(x):
    if x < 18.5:
        return 0
    elif x >= 18.5 and x <= 25.0:
        return 1
    elif x >25.0 and x < 30.0:
        return 2
    elif x >= 30.0:
        return 3

def AgeCheck(x):
    if x =='18-24':
        return 0
    elif x=='25-29':
        return 1
    elif x=='30-34':
        return 2
    elif x=='35-39':
        return 3
    elif x=='40-44':
        return 4
    elif x=='45-49':
        return 5
    elif x=='50-54':
        return 6
    elif x=='55-59':
        return 7
    elif x=='60-64':
        return 8
    elif x=='65-69':
        return 9
    elif x=='70-74':
        return 10
    elif x=='75-79':
        return 11
    elif x=='80 or older':
        return 12
    else:
        return 100



def DiabeticCheck(x):
    if x=="No":
        return 0
    elif x=="Yes":
        return 1
    elif x=="No, borderline diabetes":
        return 2
    elif x=="Yes (during pregnancy)":
        return 3
    else:
        return 100


def RaceCheck(x):
    if x=="White":
        return 1
    elif x=="Black":
        return 2
    elif x=="Hispanic":
        return 3
    elif x=="Asian":
        return 4
    elif x=="American Indian/Alaskan Native":
        return 5
    elif x=="Other":
        return 6
    else:
        return 100


def GenCheck(x):
    if x=="Very good":
        return 1
    elif x=="Good":
        return 2
    elif x=="Excellent":
        return 3
    elif x=="Fair":
        return 4
    elif x=="Poor":
        return 5
    else:
        return 100


def get_user_input():  
    age_cat = st.selectbox("**Select your Age category**", options=["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"])
    sleep_time = st.slider("How many hours of sleep do you get in a day?", 0, 24, 0)
    gen_health = st.selectbox("How can you define your general health?",options=["Excellent", "Very good", "Good", "Fair", "Poor"])
    phys_health = st.slider("For how many days during the past 30 days was your physical health not good?", 0, 30, 0)
    ment_health = st.slider("For how many days during the past 30 days was your mental health not good?", 0, 30, 0)
    stroke = st.radio("Have you had a stroke in the past?", options=("No", "Yes"))
    diff_walk = st.radio("Do you have serious difficulty while walking or climbing stairs?", options=("No", "Yes"))
    diabetic = st.selectbox("Have you ever had diabetes?", options=["Yes", "Yes (during pregnancy)", "No", "No, borderline diabetes"])
    kid_dis = st.radio("Have you had a kidney disease in the past?", options=("No", "Yes"))
    
    features = pd.DataFrame({
            "Stroke": [stroke],
            "PhysicalHealth": [phys_health],
            "MentalHealth": [ment_health],
            "DiffWalking": [diff_walk],                            
            "AgeCategory": [age_cat],
            "Diabetic": [diabetic],
            "GenHealth": [gen_health],
            "SleepTime": [sleep_time], 
            "KidneyDisease": [kid_dis]
    })
    st.dataframe(features)
    return features


st.markdown("# Predict Heart Disease 🫀")
st.markdown("## Fill out the below questionaire ")
st.write(
    """
    At the end you will get answers from our Machine Learning Models.
    """
)
    
df2 = get_user_input()


predict_button = st.button("Predict",type="primary")

if predict_button:
    df2['Stroke'] = df2['Stroke'].replace({'Yes':1, 'No':0})
    df2['DiffWalking'] = df2['DiffWalking'].replace({'Yes':1, 'No':0})
    df2['KidneyDisease'] = df2['KidneyDisease'].replace({'Yes':1, 'No':0})
    df2['PhysicalHealth'] = df2['PhysicalHealth'].astype("float")
    df2['MentalHealth'] = df2['MentalHealth'].astype("float")
    df2['SleepTime'] = df2['SleepTime'].astype("float")
    df2['GenHealth'] = df2['GenHealth'].astype("string")
    df2['AgeCategory'] = df2['AgeCategory'].apply(AgeCheck)
    df2['Diabetic'] = df2['Diabetic'].apply(DiabeticCheck)
    df2['GenHealth'] = df2['GenHealth'].apply(GenCheck)
    
    print(df2)
    
    with st.spinner(text="Running Prediction ..."):
        time.sleep(2)
            
    with st.spinner(text="Hold on ..."):
        time.sleep(2)
        
        #pickled_model = pickle.load(open('model/model_DT.pkl', 'rb'))
        #predict_heart_disease = (pickled_model.predict(df2))
        #prediction_prob = pickled_model.predict_proba(df2)

        
        #print(predict_heart_disease)
        #print(prediction_prob)
        #display_result(predict_heart_disease, round(prediction_prob[0][1] * 100, 2))

        pickled_DT = pickle.load(open('model/model_DT.pkl', 'rb'))
        predict_heart_DT = (pickled_DT.predict(df2))
        prediction_prob_DT = pickled_DT.predict_proba(df2)
        pickled_KNN = pickle.load(open('model/model_knn.pkl', 'rb'))
        predict_heart_KNN = (pickled_DT.predict(df2))
        prediction_prob_KNN = pickled_DT.predict_proba(df2)
        
        pickled_ada = pickle.load(open('model/model_ada.pkl', 'rb'))
        predict_heart_ada = pickled_ada.predict(df2)
        if(predict_heart_ada == 1):
            if(prediction_prob_DT > prediction_prob_KNN):
                display_result(predict_heart_ada, {round(prediction_prob_DT[0][1] * 100, 2)})
            else:
                display_result(predict_heart_ada, {round(prediction_prob_KNN[0][1] * 100, 2)})
        else:
            display_result(predict_heart_ada, {round(prediction_prob_DT[0][1] * 100, 2)})
