#!python


class Graph(object):

    def __init__(self):
        """Initialize a graph implemented as an adjacency list."""
        self.data = {}

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.data)

    @property
    def size(self):
        """Return the size of the graph."""
        return len(self.data)

    def add_vertex(self, vert):
        """Add a vertex to the graph."""
        self.data[vert] = []

    def add_edge(self, from_vert, to_vert):
        """Add a new, directed edge to the graph that connects
        two vertices."""
        if not self.data[from_vert]:
            self.add_vertex(from_vert)

        if not self.data[to_vert]:
            self.add_vertex(to_vert)

        self.data[from_vert].append(to_vert)

    def add_weighted_edge(self, from_vert, to_vert, weight):
        """Add a new, weighted, directed edge to the graph that connects
        two vertices."""
        # NOTE: Cannot mix weighted and unweighted edges in a graph
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key. If it exists, return
        True, else return False."""
        if not self.data[vert_key]:
            return False
        return True

    def get_vertices(self):
        """Return the list of all vertices in the graph."""
        return [vertex for vertex in self.data.keys()]

    def get_neighbors(self, from_vert):
        """List all vertices y such that there is an edge from the
        vertex from_vert to the vertex y."""
        if not self.data[from_vert]:
            raise KeyError("{} is not in the Graph".format(from_vert))
        return self.data[from_vert]
