#!python

from collections import deque
import string


class Vertex(object):
    """Helper class that defines vertices and vertex neighbors."""

    def __init__(self, vertex_id):
        """Initialize a vertex and its neighbors.

        id: a number or string to identify the vertex
        neighbors: set of vertices adjacent to self, stored in dictionary with:
            key = vertex object
            value = weight of edge between self and neighbor
        """
        self.id = vertex_id
        self.neighbors = {}
        self.parent = None

    def __repr__(self):
        """Return representation of vertex object."""
        return f"Vertex({self.id})"

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f"{self.id} adjacent to {[x.id for x in self.neighbors]}"

    def __hash__(self):
        """Return hash of vertex class, for using this class as a dict key."""
        return hash(self.id)

    def __eq__(self, other):
        """Determine if two vertices are equal."""
        return self.id == other.id

    def __ne__(self, other):
        """Determine if two vertices are not equal."""
        return self.id != other.id

    def add_neighbor(self, vertex, weight=1):
        """Add a neighbor along a weighted edge."""
        # Check if vertex is already a neighbor
        if vertex in self.neighbors:
            # If so, raise KeyError
            raise KeyError(f"{vertex.id} is already a neighbor of {self.id}")
        # If not, add vertex to neighbors and assign weight
        self.neighbors[vertex] = weight

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # Return the neighbors
        return set(self.neighbors.keys())

    def get_id(self):
        """Return the id of this vertex."""
        # Return the id of the vertex
        return self.id

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # Return the weight of the edge from this vertex to the given vertex
        return self.neighbors[vertex]


class Graph:
    """Demonstrates the essential facts and functionalities of graphs."""

    def __init__(self, weighted=False, directed=True):
        """Initialize a graph object with an empty dictionary.

        vert_list: a dictionary of the vertices in this graph where:
            key = the id of a vertex
            value = a vertex object with an id that matches the key
        num_vertices: number of vertices in the graph
        """
        self.vert_list = {}
        self.num_vertices = 0
        self.weighted = weighted
        self.directed = directed

    def __iter__(self):
        """Iterate over the vertex objects in the graph.

        to use sytax: for v in g
        """
        return iter(self.vert_list.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key.

        Return the vertex if the vertex is new, else raise KeyError.
        """
        # Raise error if key already exists in graph
        if key in self.vert_list:
            raise KeyError(f"Vertex({key}) is already in the Graph")
        # Increment the number of vertices
        self.num_vertices += 1
        # Create a new vertex
        new_vertex = Vertex(key)
        # Add the new vertex to the vertex list
        self.vert_list[key] = new_vertex
        # Return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists, else raise KeyError."""
        # Raise error if key does not exist in graph
        if key not in self.vert_list:
            raise KeyError(f"Vertex({key}) is not in the Graph")
        # Return the vertex if it is in the graph
        return self.vert_list[key]

    def add_edge(self, from_key, to_key, weight=1):
        """Add edge from vertex with key `from_key` to vertex with key `to_key`.

        If a weight is provided, use that weight.
        """
        if weight != 1 and not self.weighted:
            print(f"Detected weight of {weight} in unweighted graph.")
            print("Graph is now weighted, all previous vertices have weight 1")
            self.weighted = True

        # Add from_key vertex if it is not in the graph
        if from_key not in self.vert_list:
            self.add_vertex(from_key)

        # Add to_key vertex if it is not in the graph
        if to_key not in self.vert_list:
            self.add_vertex(to_key)

        # Get vertices from keys
        from_vert = self.vert_list[from_key]
        to_vert = self.vert_list[to_key]

        # When both vertices in graph, make from_vert a neighbor of to_vert
        from_vert.add_neighbor(to_vert, weight)
        # If the graph undirected, add connection back from to_vert to from_key
        if not self.directed:
            to_vert.add_neighbor(from_vert, weight)

    def get_vertices(self):
        """Return all the vertices in the graph."""
        return set(self.vert_list.values())

    def make_graph_from_file(self, file_name):
        """Read graph data from a file, and create a graph based on it."""
        valid_types = "gGdD"

        graph_type = ""
        vertices = ""
        edge_list = []
        directed = False
        weighted = False

        with open(file_name, 'r') as f:
            for line in f.readlines():
                # Strip trailing whitespace
                line = line.rstrip()

                # Find graph type
                if line[0] in string.ascii_letters:
                    if line[0] in valid_types:
                        graph_type = line[0].upper()
                    else:
                        raise ValueError("Looking for type 'G' or 'D'")

                # Find list of vertices
                if line[0] in string.digits:
                    vertices = line

                # Find edges
                if line[0] == "(":
                    edge_list.append(line)

        # See if graph is a digraph
        if graph_type == "D":
            directed = True
        # See if graph is weighted
        if len(edge_list[0].split(",")) == 3:
            weighted = True

        # Set the graph type if it has not been set yet
        if self.num_vertices == 0:
            self.weighted = weighted
            self.directed = directed

        # Add vertices to graph
        # TODO: Does not handle string vertex names
        for vertex in vertices.split(","):
            self.add_vertex(int(vertex))

        # Add edges to graph
        # TODO: Does not handle string vertex names or decimal weights
        for edge in edge_list:
            # Remove parenthesis
            data = edge[1:-1]
            # Turn data into array by splitting on commas
            data = data.split(",")

            # Split the tuple correctly
            if weighted:
                # Remove parenthesis from strings, and convert strings to ints
                self.add_edge(int(data[0]), int(data[1]), int(data[2]))
            else:
                # Remove parenthesis from strings, and convert strings to ints
                self.add_edge(int(data[0]), int(data[1]))

    def get_edge_list(self):
        """Return a list of edges (with their weights if weighted)."""
        edge_list = set()

        for from_vert in self.get_vertices():
            for to_vert in from_vert.get_neighbors():
                # If the graph is weighted, store the edge weight in a graph
                if self.weighted:
                    weight = from_vert.neighbors[to_vert]

                # If the graph is directed, as to edge list as normal
                if self.directed and self.weighted:
                    edge_list.add((from_vert.id, to_vert.id, weight))
                if self.directed and not self.weighted:
                    edge_list.add((from_vert.id, to_vert.id))

                # If the graph is undirected, make sure only one edge between
                # two vertices is counted. My implementation stores a directed
                # edge from and to both vertices for easier traversals.
                if not self.directed and self.weighted:
                    if (to_vert.id, from_vert.id, weight) not in edge_list:
                        edge_list.add((from_vert.id, to_vert.id, weight))
                if not self.directed and not self.weighted:
                    if (to_vert.id, from_vert.id) not in edge_list:
                        edge_list.add((from_vert.id, to_vert.id))

        return edge_list

    def breadth_first_search(self, vertex, n, only_new=True):
        """Find all vertices n edges away from the passed in vertex."""
        # Raise error if non vertex object is passed in as vertex
        if not isinstance(vertex, Vertex):
            raise TypeError("vertex parameter must be of type Vertex")

        # Raise error if vertex not in the graph
        if vertex not in self.get_vertices():
            raise ValueError(f"{vertex} is not in the Graph")

        # If the search is looking for vertices only accessible at level n,
        if only_new:
            # Create a set of vertices that have already been visited
            seen_vertices = set([vertex])

        # Create deque with passed in vertex
        vertex_deque = deque([vertex])
        # n_counter tracks the current level
        n_counter = 0
        # counter tracks how many vertices from level n are still in the deque
        counter = 1

        # Keep looping until there are no more vertices to go through, or
        # until the nth level has been reached
        while len(vertex_deque) > 0 and n_counter < n:
            # Grab a vertex from the front of the deque
            popped_vertex = vertex_deque.popleft()

            # Queue vertices if they will be seen for the first time
            if only_new:
                # Go through the neighbors of the popped_vertex
                for vert in popped_vertex.get_neighbors():
                    # If this vertex is new, allow it to be traversed
                    if vert not in seen_vertices:
                        # Set the parent of this vertex as the popped vertex
                        vert.parent = popped_vertex
                        # Add vertex to back of the deque
                        vertex_deque.append(vert)
                        # Mark that the vertex has been seen
                        seen_vertices.add(vert)
            # Otherwise, just add all vertices
            else:
                # Add all vertices that vert can reach to the back of the deque
                vertex_deque.extend(popped_vertex.get_neighbors())
            # Remove one from the counter because a vertex was just popped
            counter -= 1

            # When all nodes from the current level are removed
            if counter == 0:
                # Set the current level that all the current vertices are on
                n_counter += 1
                # Track how many vertices can be reached on this level
                counter = len(vertex_deque)

        # If the loop above ends early due to lack of levels,
        if n_counter < n:
            # Return empty set because no vertices exist n edges away
            return set()
        # Return a set of all the vertices that can be reached at the nth level
        return set(vertex_deque)

    def find_shortest_path(self, start, end):
        """Find the shortest path between two vertices."""
        # Raise error if start or end does not exist in graph
        if start not in self.vert_list:
            raise KeyError(f"Vertex({start}) is not in the Graph")
        if end not in self.vert_list:
            raise KeyError(f"Vertex({end}) is not in the Graph")

        # Set the starting and ending vertices, using start and end keys
        start_vert = self.vert_list[start]
        end_vert = self.vert_list[end]

        # Get the vertices one edge away from starting vertex
        level = 1
        verts_at_n_level = self.breadth_first_search(start_vert, level)
        # Keep searching levels there is nothing, or the end vertex is found
        while end_vert not in verts_at_n_level:
            # If there are no more vertices to search
            if len(verts_at_n_level) == 0:
                # Return None because there is no path between the vertices
                return None
            # Get the vertices one more edge away from the starting vertex
            level += 1
            verts_at_n_level = self.breadth_first_search(start_vert, level)

        # Create a path list and the ending vertex
        path = [end_vert]
        parent = end_vert
        # Go through the parents of each vertex, until start vertex is reached
        while start_vert != parent:
            # Move to the parent of the current vertex, and add it to the path
            parent = parent.parent
            path.append(parent)

        # Reverse the path, and return it
        path[:] = reversed(path)
        return path


# Driver code
if __name__ == "__main__":

    # Challenge 1: Create the graph and output the vertices & edges
    g = Graph()

    # Add your friends
    g.add_vertex("Myself")
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")
    g.add_vertex("Friend 4")
    g.add_vertex("Friend 5")
    g.add_vertex("Friend 6")
    g.add_vertex("Friend 7")
    g.add_vertex("Friend 8")
    g.add_vertex("Friend 9")

    # Add connections (non weighted edges for now)
    g.add_edge("Myself", "Friend 1")
    g.add_edge("Myself", "Friend 2")
    g.add_edge("Myself", "Friend 3")
    g.add_edge("Myself", "Friend 4")
    g.add_edge("Myself", "Friend 5")
    g.add_edge("Myself", "Friend 6")
    g.add_edge("Myself", "Friend 7")
    g.add_edge("Myself", "Friend 8")
    g.add_edge("Myself", "Friend 9")

    g.add_edge("Friend 1", "Friend 9")
    g.add_edge("Friend 1", "Myself")
    g.add_edge("Friend 1", "Friend 3")

    g.add_edge("Friend 2", "Friend 8")
    g.add_edge("Friend 2", "Friend 7")
    g.add_edge("Friend 2", "Myself")
    g.add_edge("Friend 2", "Friend 5")

    g.add_edge("Friend 3", "Friend 1")
    g.add_edge("Friend 3", "Myself")

    g.add_edge("Friend 4", "Myself")
    g.add_edge("Friend 4", "Friend 7")
    g.add_edge("Friend 4", "Friend 6")
    g.add_edge("Friend 4", "Friend 5")

    g.add_edge("Friend 5", "Friend 4")
    g.add_edge("Friend 5", "Friend 2")
    g.add_edge("Friend 5", "Myself")
    g.add_edge("Friend 5", "Friend 9")
    g.add_edge("Friend 5", "Friend 6")

    g.add_edge("Friend 6", "Friend 5")
    g.add_edge("Friend 6", "Friend 4")
    g.add_edge("Friend 6", "Myself")
    g.add_edge("Friend 6", "Friend 7")

    g.add_edge("Friend 7", "Friend 6")
    g.add_edge("Friend 7", "Friend 4")
    g.add_edge("Friend 7", "Myself")
    g.add_edge("Friend 7", "Friend 2")
    g.add_edge("Friend 7", "Friend 9")

    g.add_edge("Friend 8", "Myself")
    g.add_edge("Friend 8", "Friend 2")

    g.add_edge("Friend 9", "Friend 7")
    g.add_edge("Friend 9", "Friend 5")
    g.add_edge("Friend 9", "Myself")
    g.add_edge("Friend 9", "Friend 1")

    # Print vertices
    print(f"The vertices are: {g.get_vertices()} \n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f"( {v.get_id()} , {w.get_id()} )")
