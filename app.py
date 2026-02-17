import pickle 
import streamlit as st
import pandas as pd
import numpy as np

# Upload Data
pickle.load(open('model.sav', 'rb'))

# App title
st.markdown("<h1 style='text-align: center; color: red;'> Heart Disease Prediction App </h1>", unsafe_allow_html=True)
st.write("Enter patient details below and click Predict to check the risk of heart disease.")

# Columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Basic Info")
    age = st.number_input("Age", min_value=1, max_value=120, value=45)
    sex = st.selectbox("Sex", ["Male", "Female"])
    dataset = st.selectbox("Dataset Source", ["Cleveland", "Hungarian", "Switzerland", "Long Beach"])

with col2:
    st.subheader("Clinical Measurements")
    cp = st.selectbox("Chest Pain Type (cp)", [0,1,2,3])
    trestbps = st.number_input("Resting BP (trestbps)", min_value=80, max_value=250, value=120)
    chol = st.number_input("Serum Cholesterol (chol)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl (fbs)", [0,1])
    restecg = st.selectbox("Resting ECG (restecg)", [0,1,2])
    thalch = st.number_input("Max Heart Rate (thalch)", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0,1])
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment (slope)", [0,1,2])
    thal = st.selectbox("Thalassemia (thal)", [0,1,2,3])

# Create dictionary of input data
data_dict = {
    "age": [age],
    "sex": [1 if sex=="Male" else 0],
    "dataset": [dataset],
    "cp": [cp],
    "trestbps": [trestbps],
    "chol": [chol],
    "fbs": [fbs],
    "restecg": [restecg],
    "thalch": [thalch],
    "exang": [exang],
    "oldpeak": [oldpeak],
    "slope": [slope],
    "thal": [thal],
    "num": [0]  # placeholder target
}

# Convert dictionary to DataFrame
input_df = pd.DataFrame(data_dict)

# Predict button in center
st.markdown("<hr>", unsafe_allow_html=True)
predict_button = st.button(" Predict Heart Disease Risk ")

if predict_button:
    
    # =========================
    # IMPORTANT: preprocess your input_df here before prediction
    # =========================
    
    # Dummy prediction
    dummy_prediction = np.random.choice(["No Heart Disease", "Heart Disease"])
    
    # Show input data in expander
    with st.expander("See Entered Patient Data"):
        st.write(input_df)
    
    # Show prediction result
    st.markdown("<h2 style='color: green;'>Prediction Result:</h2>", unsafe_allow_html=True)
    if dummy_prediction == "Heart Disease":
        st.error(f"⚠️ {dummy_prediction}")
    else:
        st.success(f"✅ {dummy_prediction}")