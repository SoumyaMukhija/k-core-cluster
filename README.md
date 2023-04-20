# k-core-cluser

Created an implementation of the
k-core cluster algorithm.


K-core is a clustering concept in which for an integer k>=1, k-cores of the graph are connected
components left after all vertices of degrees < k are removed from the graph. We keep
iteratively removing vertices until no vertex with a degree < k is left. Each node in the remaining
graph has at least k neighbors within the subset.
Every graph has a unique k-core. In the implementation proposed in this report, we have
generated the largest subgraph possible with each node having k or more than k degrees
