import pytest
from stacks_queues.stacks_queues import Node, Queue
from graphs.graph import Graph, Vertex
# from graphs.graph_breadth_first import graph_breadth_first


def test_instantiate_graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}

def test_instantiate_empty_node():
    node1 = Node(1)
    assert node1.value == 1
    assert node1.next == None

def test_instantiate_queue():
    queue = Queue()
    assert queue

def test_add_nodes():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    actual = graph.size()
    assert actual == 3


