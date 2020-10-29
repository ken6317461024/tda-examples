# Importing libraries
from gtda.homology import VietorisRipsPersistence
from gtda.diagrams import PersistenceEntropy

import numpy as np

from gtda.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# Plotting functions
from gtda.plotting import plot_diagram, plot_point_cloud, plot_heatmap

# Representing the circle in 3d with parametric equations.
circle = np.asarray([[np.sin(t),np.cos(t),0] for t in range(400)])
plot_point_cloud(circle)

# Representing the sphere in 3d with parametric equations
sphere = np.asarray([[np.cos(s)*np.cos(t),np.cos(s)*np.sin(t),np.sin(s)] for t in range(20) for s in range(20)])
plot_point_cloud(sphere)

# Representing the torus in 3d with parametric equations
torus = np.asarray([[(2+np.cos(s))*np.cos(t),(2+np.cos(s))*np.sin(t),np.sin(s)] for t in range(20) for s in range(20)])
plot_point_cloud(torus)

# Saving the results into an array
topological_spaces = np.asarray([circle,sphere,torus])

# The homology ranks we choose to consider
homology_dimensions = (0, 1, 2)
VR = VietorisRipsPersistence(
    metric='euclidean', max_edge_length=10, homology_dimensions=homology_dimensions)

# Array of persistence diagrams, one per point cloud in the input
diagrams = VR.fit_transform(topological_spaces)
print(f'diagrams.shape = {diagrams.shape}')

# Plotting the persistence diagram of the circle
plot_diagram(diagrams[0])

