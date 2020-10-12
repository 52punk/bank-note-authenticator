# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:26:21 2020

@author: HP
"""


import streamlit as st

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

st.title("Hello! and Welcome to Bank Note Authentication ML App")
st.write("Your values are "+str(variance)+" "+str(skewness)+" "+str(curtosis)+" "+str(entropy))
st.write("And your result is 1 which means Not Authenticated!!")
