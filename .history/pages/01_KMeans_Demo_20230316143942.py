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
centroids = np.random.randint(np.min(data), np.max(data), size=(k,2))
color_map = np.array(range(k)) * 10

st.write("Here are the values of the initial centroids and the plot of the data with the centroids")
#use columns
col1, col2 = st.columns(2)
col1.write(centroids)
#add the centroids to the plot
fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1])
#add the centroids to the plot, give each centroid a different color (based on index), make the centroid points x's, and make them bigger
ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)

col2.pyplot(fig)

st.write("Now we will calculate the distance between each point and each centroid, and assign each point to the centroid with the smallest distance")

labels = np.zeros(len(data))
for i in range(len(data)):
    distances = np.sqrt(np.sum((data[i] - centroids)**2, axis=1))
    labels[i] = np.argmin(distances)

st.write("Here is the plot of the data with the centroids and the points assigned to each centroid")
fig, ax = plt.subplots()    
ax.scatter(data[:,0], data[:,1], c=color_map[labels.astype(int)])
ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)
st.pyplot(fig)


st.write("Now we will recalculate the centroids by taking the mean of all the points assigned to each centroid")

for i in range(k):
    centroids[i] = np.mean(data[labels == i], axis=0)

st.write("Here is the plot of the data with the centroids and the points assigned to each centroid")
fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1], c=color_map[labels.astype(int)])
ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)

st.pyplot(fig)

st.write("Now we will repeat the process of assigning points to centroids and recalculating the centroids until the centroids stop moving. Use the slider to see how many iterations it takes to converge.")




