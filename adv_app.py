import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('linear_reg.sav', 'rb'))

st.title('Hospital Total Cost Prediction App')

# Input features
Age = st.number_input('Age', min_value=0.0)
Body Weight = st.number_input('Body Weight', min_value=0.0)
Body Height = st.number_input('Body Height', min_value=0.0)
BP High = st.number_input('BP High', min_value=0.0)
BP Low = st.number_input('BP Low', min_value=0.0)
HB = st.number_input('HB', min_value=0.0)
UREA = st.number_input('UREA', min_value=0.0)
Creatine = st.number_input('Creatine', min_value=0.0)

# Make prediction
if st.button('Predict Hospital Total Cost'):
    input_data = np.array([[Age, Body Weight, Body Height, BP High, BP Low, HB, UREA, Creatine]])
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Hospital Cost: {prediction:.2f}')
