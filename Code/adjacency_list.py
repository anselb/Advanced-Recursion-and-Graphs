#!python


class Graph(object):

    def __init__(self):
        """Initialize a graph implemented as an adjacency list."""
        self.graph = {}

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.graph)

    @property
    def size(self):
        """Return the size of the graph."""
        return len(self.graph)

    def add_vertex(self, vert):
        """Add a vertex to the graph."""
        if vert in self.graph:
            raise KeyError("{} is already in the Graph".format(vert))
        self.graph[vert] = []

    def add_edge(self, from_vert, to_vert):
        """Add a new, directed edge to the graph that connects
        two vertices."""
        if from_vert not in self.graph:
            self.add_vertex(from_vert)

        if to_vert not in self.graph:
            self.add_vertex(to_vert)

        self.graph[from_vert].append(to_vert)

    def add_weighted_edge(self, from_vert, to_vert, weight):
        """Add a new, weighted, directed edge to the graph that connects
        two vertices."""
        # NOTE: Cannot mix weighted and unweighted edges in a graph
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key. If it exists, return
        True, else return False."""
        if vert_key not in self.graph:
            return False
        return True

    def get_vertices(self):
        """Return the list of all vertices in the graph."""
        return [vertex for vertex in self.graph.keys()]

    def get_neighbors(self, from_vert):
        """List all vertices y such that there is an edge from the
        vertex from_vert to the vertex y."""
        if from_vert not in self.graph:
            raise KeyError("{} is not in the Graph".format(from_vert))
        return self.graph[from_vert]
