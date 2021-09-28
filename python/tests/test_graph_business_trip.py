import pytest
from graphs.graph import Graph, Vertex, Edge
from graphs.graph_business_trip import flights

def test_instantiate_graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}

def test_instantiate_vertex():
    vertex = Vertex()
    assert vertex
