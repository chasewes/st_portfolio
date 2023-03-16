import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write("I wrote this app to demonstrate how the k means algorithm works!")

#generate 100 random points in 4 clusters

data = np.random.rand(100,2) 