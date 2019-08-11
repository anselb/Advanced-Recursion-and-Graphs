from graph import Graph
import sys


def main():
    """Run the challenge with a passed in graph file name."""
    if len(sys.argv) < 4:
        print("Please enter a file name, a start vertex, and an end vertex")
    graph_file = sys.argv[1]
    start_vert = int(sys.argv[2])
    end_vert = int(sys.argv[3])

    graph = Graph()
    graph.make_graph_from_file(graph_file)
    path = graph.find_path(start_vert, end_vert)

    if path is None:
        print(f"There exists a path between \
vertex {start_vert} and {end_vert}: FALSE")
        print(f"Vertices in the path: {path}")
        return

    for index in range(len(path)):
        path[index] = path[index].id

    print(f"There exists a path between \
vertex {start_vert} and {end_vert}: TRUE")
    print(f"Vertices in the path: {path}")


if __name__ == '__main__':
    main()
