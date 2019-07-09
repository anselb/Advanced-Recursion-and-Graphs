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
        pass

    def test_has_vertex(self):
        pass

    def test_get_vertices(self):
        pass

    def test_get_neighbors(self):
        pass


if __name__ == '__main__':
    unittest.main()
