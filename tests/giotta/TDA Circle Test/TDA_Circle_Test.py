# Importing libraries
from gtda.homology import VietorisRipsPersistence
from gtda.diagrams import PersistenceEntropy

import numpy as np

from gtda.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Plotting functions
from gtda.plotting import plot_diagram, plot_point_cloud, plot_heatmap

#Generating various examples. 

# Representing the circle in 3d with parametric equations.
circle = np.asarray([[np.sin(t),np.cos(t),0] for t in range(400)])
plot_point_cloud(circle)

# Twisting the circle with a cosine function with angle pi/2.
twistedcircle1 = np.asarray([[np.sin(t),np.cos(t),np.cos(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),np.cos(t),-np.cos(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# Twisting the circle with a cosine function with angle 3pi/2. 
twistedcircle1 = np.asarray([[np.sin(t),np.cos(t),np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),np.cos(t),-np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# Twisting the circle with a sin function with angle pi/2.
twistedcircle1 = np.asarray([[np.sin(t),np.cos(t),np.sin(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),np.cos(t),-np.sin(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# Twisting the circle with a sin function with angle 3pi/2.
twistedcircle1 = np.asarray([[np.sin(t),np.cos(t),np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),np.cos(t),-np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# # Twisting the circle with sine and cosine and angle 3pi/2 projected onto x. 
twistedcircle1 = np.asarray([[np.sin(t),np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2),np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),-np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2),-np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# Twisting the circle with sine and cosine and angle 3pi/2 projected onto y. 
twistedcircle1 = np.asarray([[np.cos(t),np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2),np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.cos(t),-np.cos((3*(np.arctan(np.cos(t)/np.sin(t))))/2),-np.sin((3*(np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)


#Consider a specific example. 
twistedcircle1 = np.asarray([[np.sin(t),np.cos(t),np.cos(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle2 = np.asarray([[np.sin(t),np.cos(t),-np.cos(((np.arctan(np.cos(t)/np.sin(t))))/2)] for t in range(1,400)])
twistedcircle = np.concatenate((twistedcircle1,twistedcircle2))
plot_point_cloud(twistedcircle)

# The homology ranks we choose to consider
homology_dimensions = (0, 1)
VR = VietorisRipsPersistence(metric='euclidean', max_edge_length=10, homology_dimensions=homology_dimensions)

# Creating persistence diagrams, one per point cloud in the input.
diagrams = VR.fit_transform([twistedcircle])
print(f'diagrams.shape = {diagrams.shape}')

# Plotting the persistence diagram of the twisted circle. 
plot_diagram(diagrams[0])

