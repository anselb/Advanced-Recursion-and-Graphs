from graph import Graph
import sys


def print_graph_path_data(path):
    """Print out the data of the graph."""
    for index in range(len(path)):
        path[index] = path[index].id

    print(f"Vertices in shortest path: {path}")
    print(f"Number of edges in shortest path: {len(path) - 1}")


def main():
    """Run the challenge with a passed in graph file name."""
    if len(sys.argv) < 4:
        raise RuntimeError("Expecting file name, start vertex, and end vertex")
    graph_file = sys.argv[1]
    start_vert = int(sys.argv[2])
    end_vert = int(sys.argv[3])

    graph = Graph()
    graph.make_graph_from_file(graph_file)
    shortest_path = graph.find_shortest_path(start_vert, end_vert)

    print_graph_path_data(shortest_path)

if __name__ == '__main__':
    main()
