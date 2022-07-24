import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle
import random

st.write("""
# Sum Of Two Given Numbers App
""")
#Get Input

st.header('User Input')

def user_input_features():
    
    
    a = st.number_input("First_Input",min_value=random.random(),max_value=random.random())
    b = st.number_input("Second_Input",min_value=random.random(),max_value=random.random())
    c = a+b
    
  
    return c
st.write(c)


#st.subheader('Prediction Probability')
#st.write(prediction_proba)
