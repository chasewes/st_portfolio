import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.header("I wrote this app to demonstrate how the k means algorithm works!")



@st.cache
def load_data():
        data_1 = (np.random.rand(25,2) * 100)
        data_2 = (np.random.rand(25,2) * 100) + [150,0]
        data_3 = (np.random.rand(25,2) * 100) + [150,150]
        data_4 = (np.random.rand(25,2) * 100) + [0,150]

        data = np.concatenate((data_1, data_2, data_3, data_4), axis=0)
        return data

data = load_data()

st.write("Here is the data plotted on a 2d plane")

@st.cache
def plot_data(data):
    fig, ax = plt.subplots()
    ax.scatter(data[:,0], data[:,1])
    return fig

st.pyplot(plot_data(data))



st.write("Now we will use the k means algorithm to find the 4 clusters")

st.write("first, we will select the number of clusters (k) to find")

k = st.slider("k", min_value=1, max_value=10, value=4, step=1)

st.write(f"then, we will randomly select {k} points to be the initial centroids")

@st.cache
def get_initial_centroids(data, k):
    centroids = np.random.randint(np.min(data), np.max(data), size=(k,2))
    return centroids

centroids = get_initial_centroids(data, k)
color_map = np.array(range(k)) * 10

@st.cache
def plot_data_with_centroids(data, centroids, color_map):
    fig, ax = plt.subplots()
    ax.scatter(data[:,0], data[:,1])
    ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)
    return fig

st.pyplot()

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

old_centroids = centroids.copy()
for i in range(k):
    centroids[i] = np.mean(data[labels == i], axis=0)

st.write("Here is the plot of the data with the centroids and the points assigned to each centroid")
fig, ax = plt.subplots()
ax.scatter(data[:,0], data[:,1], c=color_map[labels.astype(int)])
ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)

st.pyplot(fig)

st.write("Now we will repeat the process of assigning points to centroids and recalculating the centroids until the centroids stop moving. Use the slider to see how many iterations it takes to converge.")

iterations = 0

figures_over_time = []

while not np.all(old_centroids == centroids):
    old_centroids = centroids.copy()
    for i in range(k):
        centroids[i] = np.mean(data[labels == i], axis=0)
    for i in range(len(data)):
        distances = np.sqrt(np.sum((data[i] - centroids)**2, axis=1))
        labels[i] = np.argmin(distances)

    fig, ax = plt.subplots()
    ax.scatter(data[:,0], data[:,1], c=color_map[labels.astype(int)])
    ax.scatter(centroids[:,0], centroids[:,1], c=color_map, marker='x', s=200)
    iterations += 1

    figures_over_time.append(fig)


st.write(f"It took {iterations} iterations to converge")

if "figures_over_time" not in st.session_state:
    st.session_state.figures_over_time = figures_over_time
else:
    figures_over_time = st.session_state.figures_over_time


#allow the user to select which iteration to view
iteration = st.slider("Iteration", min_value=0, max_value=iterations, value=0, step=1)

st.pyplot(figures_over_time[iteration])












