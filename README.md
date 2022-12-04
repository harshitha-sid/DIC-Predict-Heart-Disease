# DIC-Predict-Heart-Disease

## To access the application on Streamlit Cloud:

This web application has been deployed on Streamlit Cloud. It can be accessed here: [https://harshitha-sid-dic-predict-heart-disease-welcome-kjjo7n.streamlit.app/](https://harshitha-sid-dic-predict-heart-disease-welcome-kjjo7n.streamlit.app/)

## Steps to run the application locally:

1. Clone the code from the Github repository
```
git clone https://github.com/harshitha-sid/DIC-Predict-Heart-Disease.git
```

2. Create a virtual environment
```
python3 -m venv py && source py/bin/activate
```

3. Install the required dependencies (Note: This code is tested with python 3.9 on Intel chip, Mac M1 has issues)
```
pip3 install -r requirements.txt
```

4. Run the web application
```
streamlit run Welcome.py --theme.base "dark"
```

By default, the application will open in the browser on port 8501. Hope you will enjoy interacting with our web application 😊 !
