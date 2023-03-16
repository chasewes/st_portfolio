import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("I wrote this app to demonstrate how the k means algorithm works!")

#generate 100 random points in 4 clusters

#if this is the first time the app is run, generate the data
#otherwise, load the data from the cache
if "data" not in st.session_state:
    data_1 = (np.random.rand(25,2) * 100)
    data_2 = (np.random.rand(25,2) * 100) + [150,0]
    data_3 = (np.random.rand(25,2) * 100) + [150,150]
    data_4 = (np.random.rand(25,2) * 100) + [0,150]

    data = np.concatenate((data_1, data_2, data_3, data_4), axis=0)

    st.session_state.data = data
else:
    data = st.session_state.data


st.write("Here is the data plotted on a 2d plane")

fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1])
st.pyplot(fig)

st.write("Now we will use the k means algorithm to find the 4 clusters")

st.write("first, we will select the number of clusters (k) to find")
k = st.slider("k", min_value=1, max_value=10, value=4, step=1)

st.write(f"then, we will randomly select {k} points to be the initial centroids")

#centroids should be between the min and max of each dimensino
centroids = np.random.randint(np.min(data), np.max(data), size=(4,2))

st.write("Here are the values of the initial centroids and ")

st.write(centroids)




