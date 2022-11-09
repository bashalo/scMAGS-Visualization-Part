import numpy as np
import scmags as mg

# Create scMAGS object for demo
pol = mg.datasets.pollen()
pol.filter_genes()
pol.sel_clust_marker()
markers = pol.get_markers(ind_return=True)


# Get built-in data from scMAGS
data = pol.data
labels = pol.labels
gene_ann = pol.gene_ann

unq_labels = np.unique(labels)

# Create dictionary from selected markers
scmags_markers_ind = {}

for i in range(len(unq_labels)):
    list(markers.iloc[1,:])
    scmags_markers_ind[unq_labels[i]] = list(markers.iloc[i,:])
  
# I created the figures with the markers selected by the method to check accuracy.
# I created and checked the same markers with scMAGS.


# Create Visualization Class Object

# Data Info
# The data should be a numpy matrix, rows should correspond to cells 
# and columns should correspond to genes.

# Labels and gene names should be given with a numpy array.


vis = MarkerVis(data,
                labels,
                scmags_markers_ind,
                gene_ann)
# Visualization
# New Class
vis.dot_plot()
vis.markers_heatmap()
vis.knn_classifier()
vis.markers_tSNE()
  
# scMAGS
pol.dot_plot()
pol.markers_heatmap()
pol.knn_classifier()
pol.markers_tSNE()



# Visualization with externally (I randomly create but you can give yours)selected markers
# Create random genes and dictionary for example
sel_markers = {}
sel_markers_ann ={}
sel_markers_ind = {}
nof_marker = 3 # Number of Marker for each cluster
for i in range(len(unq_labels)):
    rand_genes = np.random.randint(1,data.shape[1],nof_marker)
    sel_markers_ind[unq_labels[i]] = list(rand_genes)

# In this part, you can create a dictionary instead of the sel_marker_ind 
#  variable and add and visualize the genes you have chosen. 

vis = MarkerVis(data,
                labels,
                sel_markers_ind,
                gene_ann)
# Visualization
vis.dot_plot()
vis.markers_heatmap()
vis.knn_classifier()
vis.markers_tSNE()



