import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write("I wrote this app to demonstrate how the k means algorithm works!")

#generate 100 random points in 4 clusters

data_1 = (np.random.rand(25,2) * 100)
data_2 = (np.random.rand(25,2) * 100) + [50,0]
data_3 = (np.random.rand(25,2) * 100) + [50,25]
data_4 = (np.random.rand(25,2) * 100) + [0,25]

data = np.concatenate((data_1, data_2, data_3, data_4), axis=0)

st.write("Here is the data plotted on a 2d plane")

fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1])
st.pyplot(fig)
