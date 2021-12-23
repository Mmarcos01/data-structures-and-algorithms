import pytest
from graphs.graph import Graph, Vertex, Edge

def test_instantiate_graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}

def test_instantiate_vertex():
    vertex = Vertex()
    assert vertex

def test_instantiate_edge():
    vertex = Vertex(1)
    edge = Edge(vertex, weight=50)
    assert edge.vertex == vertex
    assert edge.weight == 50

def test_graph_add_node():
    graph = Graph()
    vertex = Vertex(15)
    graph.add_node(vertex)
    result = graph.size()
    assert result == 1

def test_an_edge_can_be_added_to_graph():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_edge(v1, v2, 20)
    v1_list = graph._adjacency_list[v1]
    first_edge = v1_list[0]
    assert first_edge.vertex == v2
    assert first_edge.weight == 20

def test_graph_get_nodes():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    list_of_nodes = graph.get_nodes()
    expected = [1,2,3]
    actual = []
    for i in list_of_nodes:
        actual.append(i.value)
    assert actual == expected

def test_neighbors_can_be_retrieved_for_a_node_with_weights():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_edge(v1, v2, 10)
    graph.add_edge(v1, v3, 20)
    actual = graph.get_neighbors(v1)
    edge1 = actual[0]
    edge2 = actual[1]
    assert edge1.vertex == v2
    assert edge1.weight == 10
    assert edge2.vertex == v3
    assert edge2.weight == 20

def test_size_returns_correct_size():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    actual = graph.size()
    assert actual == 3

