#!python


class Graph(object):

    def __init__(self):
        """Initialize a graph implemented as an adjacency list."""
        self.data = {}

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.data)

    def add_vertex(vert):
        """Add a vertex to the graph."""
        pass

    def add_edge(from_vert, to_vert):
        """Add a new, directed edge to the graph that connects
        two vertices."""
        pass

    def add_weighted_edge(from_vert, to_vert, weight):
        """Add a new, weighted, directed edge to the graph that connects
        two vertices."""
        # NOTE: Cannot mix weighted and unweighted edges in a graph
        pass

    def get_vertex(vert_key):
        """Find the vertex in the graph named vert_key."""
        pass

    def get_vertices():
        """Return the list of all vertices in the graph."""
        pass

    def get_neighbors(from_vert):
        """List all vertices y such that there is an edge from the
        vertex from_vert to the vertex y."""
        pass
