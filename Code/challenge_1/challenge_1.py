from adjacency_list import Graph
import strings
import sys


def read_graph_file(file_name):
    """Reads in graph data from a file, and creates a graph based on it"""
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
    if len(edge_list[0]) == 3:
        weighted = True

    # Create graph
    graph = Graph(weighted, directed)

    # Add edges to graph
    for edge in edge_list:
        data = edge.split(",")

        if weighted == False:
            graph.add_edge(data[0], data[1])
        else:
            graph.add_weighted_edge(data[0], data[1], data[2])

    return graph


def print_graph_data(graph):
    """Prints out the data of the graph"""
    print(f"# Vertices: {graph.size}\n")
    print(f"# Edges: {len(graph.get_edge_list())}\n")
    print("Edge List:\n")
    for edge in graph.get_edge_list():
        print(edge)


def main():
    """Runs the challenge with a passed in graph file name"""
    graph_file = sys.argv[1]
    graph = read_graph_file(graph_file)
    print_graph_data(graph)


if __name__ == '__main__':
    main()
