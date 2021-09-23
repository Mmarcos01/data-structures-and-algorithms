import pytest
from graphs.graph import Graph, Vertex, Edge
from graphs.graph_breadth_first import graph_breadth_first

def test_instantiate_graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}

def test_graph_breadth_first():
    pass
