#!python


class Graph(object):

    def __init__(self, weighted=False, directed=True):
        """Initialize a graph implemented as an adjacency list."""
        self.graph = {}
        self.weights = {}
        self.weighted = weighted
        self.directed = directed

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
        self.graph[vert] = set()

    def add_edge(self, from_vert, to_vert):
        """Add a new, directed edge to the graph that connects
        two vertices."""
        if self.weighted is True:
            raise TypeError("Cannot call add_edge() on weighted graph")

        if from_vert not in self.graph:
            self.add_vertex(from_vert)

        if to_vert not in self.graph:
            self.add_vertex(to_vert)

        if to_vert not in self.graph[from_vert]:
            self.graph[from_vert].add(to_vert)

            # If the graph can go both ways, add edge going opposite way
            if self.directed is False:
                self.graph[to_vert].add(from_vert)

    def add_weighted_edge(self, from_vert, to_vert, weight):
        """Add a new, weighted, directed edge to the graph that connects
        two vertices."""
        # NOTE: Cannot mix weighted and unweighted edges in a graph
        if self.weighted is False:
            raise TypeError("Cannot call add_weighted_edge() on unweighted graph")

        if from_vert not in self.graph:
            self.add_vertex(from_vert)

        if to_vert not in self.graph:
            self.add_vertex(to_vert)

        # TODO: Weights currently cannot be changed
        if to_vert not in self.graph[from_vert]:
            self.graph[from_vert].add(to_vert)
            self.weights[(from_vert, to_vert)] = weight

            # If the graph can go both ways, add edge going opposite way
            if self.directed is False:
                self.graph[to_vert].add(from_vert)
                self.weights[(to_vert, from_vert)] = weight

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

    def get_edge_list(self):
        """Return a list of edges (with their weights if weighted)"""
        edge_list = set()

        for from_vert in self.graph:
            for to_vert in self.get_neighbors(from_vert):
                if self.weighted:
                    weight = self.weights[(from_vert, to_vert)]

                if self.directed and self.weighted:
                    edge_list.add((from_vert, to_vert, weight))
                if self.directed and not self.weighted:
                    edge_list.add((from_vert, to_vert))
                if not self.directed and self.weighted:
                    if (to_vert, from_vert, weight) not in edge_list:
                        edge_list.add((from_vert, to_vert, weight))
                if not self.directed and not self.weighted:
                    if (to_vert, from_vert) not in edge_list:
                        edge_list.add((from_vert, to_vert))

        return edge_list
