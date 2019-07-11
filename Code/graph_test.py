#!python

from adjacency_list import Graph
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class GraphTest(unittest.TestCase):

    def test_init(self):
        g = Graph()
        assert g.size == 0

    def test_size(self):
        g = Graph()
        assert g.size == 0
        g.add_vertex('A')
        assert g.size == 1
        g.add_vertex('B')
        assert g.size == 2
        g.add_vertex('C')
        assert g.size == 3

        g.add_edge('A', 'B')
        assert g.size == 3
        g.add_edge('B', 'C')
        assert g.size == 3
        g.add_edge('C', 'D')
        assert g.size == 4

        with self.assertRaises(KeyError):
            g.add_vertex('B')  # Vertex already exists
        assert g.size == 4
        with self.assertRaises(KeyError):
            g.add_vertex('D')  # Vertex already exists
        assert g.size == 4

    def test_add_vertex(self):
        g = Graph()
        assert g.size == 0
        g.add_vertex('A')
        assert g.size == 1
        self.assertCountEqual(g.graph['A'], [])
        g.add_vertex('B')
        assert g.size == 2
        self.assertCountEqual(g.graph['B'], [])
        g.add_vertex('C')
        assert g.size == 3
        self.assertCountEqual(g.graph['C'], [])

        with self.assertRaises(KeyError):
            g.add_vertex('A')  # Vertex already exists
        with self.assertRaises(KeyError):
            g.add_vertex('B')  # Vertex already exists
        with self.assertRaises(KeyError):
            g.add_vertex('C')  # Vertex already exists

    def test_add_edge(self):
        g = Graph()
        g.add_vertex('A')
        self.assertCountEqual(g.graph['A'], [])
        g.add_vertex('B')
        self.assertCountEqual(g.graph['B'], [])
        g.add_vertex('C')
        self.assertCountEqual(g.graph['C'], [])
        assert g.size == 3

        g.add_edge('A', 'B')
        self.assertCountEqual(g.graph['A'], ['B'])  # Item order does not matter
        self.assertCountEqual(g.graph['B'], [])
        g.add_edge('A', 'C')
        self.assertCountEqual(g.graph['A'], ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(g.graph['C'], [])
        g.add_edge('B', 'C')
        self.assertCountEqual(g.graph['B'], ['C'])  # Item order does not matter
        self.assertCountEqual(g.graph['C'], [])

        g.add_edge('B', 'D')
        self.assertCountEqual(g.graph['B'], ['C', 'D'])  # Item order does not matter
        self.assertCountEqual(g.graph['D'], [])
        g.add_edge('E', 'F')
        self.assertCountEqual(g.graph['E'], ['F'])  # Item order does not matter
        self.assertCountEqual(g.graph['F'], [])

        g.add_edge('A', 'C')
        self.assertCountEqual(g.graph['A'], ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(g.graph['C'], [])
        g.add_edge('E', 'F')
        self.assertCountEqual(g.graph['E'], ['F'])  # Item order does not matter
        self.assertCountEqual(g.graph['F'], [])

    def test_has_vertex(self):
        g = Graph()
        assert g.has_vertex('A') is False
        g.add_vertex('A')
        assert g.has_vertex('A') is True
        assert g.has_vertex('B') is False
        g.add_vertex('B')
        assert g.has_vertex('B') is True
        assert g.has_vertex('C') is False
        g.add_vertex('C')
        assert g.has_vertex('C') is True

        assert g.has_vertex('D') is False
        assert g.has_vertex('E') is False
        g.add_edge('D', 'E')
        assert g.has_vertex('D') is True
        assert g.has_vertex('E') is True

    def test_get_vertices(self):
        g = Graph()
        assert g.has_vertex('A') is False
        g.add_vertex('A')
        self.assertCountEqual(g.get_vertices(), ['A'])  # Item order does not matter
        assert g.has_vertex('B') is False
        g.add_vertex('B')
        self.assertCountEqual(g.get_vertices(), ['A', 'B'])  # Item order does not matter
        assert g.has_vertex('C') is False
        g.add_vertex('C')
        self.assertCountEqual(g.get_vertices(), ['A', 'B', 'C'])  # Item order does not matter

        assert g.has_vertex('D') is False
        assert g.has_vertex('E') is False
        g.add_edge('D', 'E')
        self.assertCountEqual(g.get_vertices(), ['A', 'B', 'C', 'D', 'E'])  # Item order does not matter

    def test_get_neighbors(self):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge('A', 'B')
        self.assertCountEqual(g.get_neighbors('A'), ['B'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('B'), [])
        g.add_edge('A', 'C')
        self.assertCountEqual(g.get_neighbors('A'), ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('C'), [])

        g.add_edge('C', 'A')
        self.assertCountEqual(g.get_neighbors('C'), ['A'])  # Item order does not matter
        g.add_edge('C', 'B')
        self.assertCountEqual(g.get_neighbors('C'), ['A', 'B'])  # Item order does not matter

        g.add_edge('A', 'D')
        self.assertCountEqual(g.get_neighbors('A'), ['B', 'C', 'D'])  # Item order does not matter
        self.assertCountEqual(g.get_neighbors('D'), [])  # Item order does not matter

        with self.assertRaises(KeyError):
            g.get_neighbors('E')  # Vertex does not exist
        with self.assertRaises(KeyError):
            g.get_neighbors('F')  # Vertex does not exist


if __name__ == '__main__':
    unittest.main()
