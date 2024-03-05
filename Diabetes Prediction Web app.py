#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:53:13 2024

@author: aabhi
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('/Users/aabhi/Desktop/Deploying Diabeties Prediction/trained_model.sav', 'rb')) 



# Creating a function for Prediction

def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The person is not diabetic'
    else:
      return'The person is diabetic'


def main():
    
    
    # Naming the Tittle for the Webpage
    st.title('Diabetes Prediction Web App')
    
    
    # Getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    
    if st.button('Test your Results'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        