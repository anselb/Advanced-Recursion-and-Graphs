#!python


class Graph(object):

    def __init__(self):
        """Initialize a graph implemented as an incidence matrix."""
        self.graph = []
        self.name_to_index = {}
        self.index_to_name = {}
        self.edge_count = 0

    def __repr__(self):
        """Return a string representation of this graph."""
        return 'Graph({!r})'.format(self.graph)

    @property
    def size(self):
        """Return the size of the graph."""
        return len(self.graph)

    def add_vertex(self, vert):
        """Add a vertex to the graph."""
        if vert in self.name_to_index:
            raise KeyError("{} is already in the Graph".format(vert))

        self.name_to_index[vert] = self.size
        self.index_to_name[self.size] = vert

        self.graph.append([0 for edge in range(self.edge_count)])

    def add_edge(self, from_vert, to_vert):
        """Add a new, directed edge to the graph that connects
        two vertices."""
        if from_vert not in self.name_to_index:
            self.add_vertex(from_vert)

        if to_vert not in self.name_to_index:
            self.add_vertex(to_vert)

        from_vert_index = self.name_to_index[from_vert]
        to_vert_index = self.name_to_index[to_vert]

        self.graph[from_vert_index][to_vert_index] = 1

        # If the to_vert is not already directed toward the from_vert, mark
        # that the to_vert has a directed edge from the from_vert with a -1
        if self.graph[to_vert_index][from_vert_index] != 1:
            self.graph[to_vert_index][from_vert_index] = -1

    def add_weighted_edge(self, from_vert, to_vert, weight):
        """Add a new, weighted, directed edge to the graph that connects
        two vertices."""
        # NOTE: Cannot mix weighted and unweighted edges in a graph
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key. If it exists, return
        True, else return False."""
        if vert_key not in self.name_to_index:
            return False
        return True

    def get_vertices(self):
        """Return the list of all vertices in the graph."""
        return [vertex for vertex in self.name_to_index.keys()]

    def get_neighbors(self, from_vert):
        """List all vertices y such that there is an edge from the
        vertex from_vert to the vertex y."""
        if from_vert not in self.name_to_index:
            raise KeyError("{} is not in the Graph".format(from_vert))

        from_vert_index = self.name_to_index[from_vert]
        neighbors = set()

        for index, edge in enumerate(self.graph[from_vert_index]):
            if edge == 1:
                neighbors.add(self.index_to_name[index])

        return neighbors
