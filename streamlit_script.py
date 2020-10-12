# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:29:33 2020

@author: Pankaj Kumar Sah
@LinkedIn: https://www.linkedin.com/in/pankaj-sah-b7aa39186/
@Github: https://github.com/52punk

"""
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("bank_note_new.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction



def main():
    st.sidebar.subheader("Variance")
    variance = st.sidebar.slider("Variance value",min_value=-5.00,max_value=5.00,step=0.01)
    
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Skewness")
    skewness = st.sidebar.slider("Skewness value",min_value=-5.00,max_value=5.00,step=0.01)
    
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Curtosis")
    curtosis = st.sidebar.slider("Curtosis value",min_value=-5.00,max_value=5.00,step=0.01)
    
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("Entropy")
    entropy = st.sidebar.slider("Entropy value",min_value=-5.00,max_value=5.00,step=0.01)
    
    st.title("Welcome to Bank Note Authentication ML App")
    st.header("Hello folks and welcome to")
    st.text("\nYour values are "+str(variance)+" "+str(skewness)+" "+str(curtosis)+" "+str(entropy))
    res = predict_note_authentication(variance,skewness,curtosis,entropy)
    if res==1:
        st.write("And your result is 1 which means Not Authenticated!!")
    else:
        st.write("And your result is 0 which means Authenticated!!")

if __name__=='__main__':
    main()
    
    