import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write("I wrote this app to demonstrate how the k means algorithm works!")

#generate 100 random points in 4 clusters

data = np.random.rand(100,2) / [50,50] + [35.69, 139.70]
data2 = np.random.rand(100,2) / [50,50] + [35.69, 139.70]
data3 = np.random.rand(100,2) / [50,50] + [35.69, 139.70]
data4 = np.random.rand(100,2) / [50,50] + [35.69, 139.70]

data = np.concatenate((data, data2, data3, data4), axis=0)

st.write("Here is the data plotted on a 2d plane")

plt.scatter(data[:,0], data[:,1])
st.pyplot()
