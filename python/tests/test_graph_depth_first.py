import pytest
from stacks_queues.stacks_queues import Node, Stack
from graphs.graph import Graph, Vertex
from graphs.graph_depth_first import graph_depth_first

def test_instantiate_graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}

def test_instantiate_empty_node():
    node1 = Node(1)
    assert node1.value == 1
    assert node1.next == None

def test_instantiate_queue():
    queue = Stack()
    assert queue


@pytest.mark.skip("pending")
def test_full(graph_and_root):
    graph, root = graph_and_root
    actual = graph.graph_depth_first(root)
    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected

@pytest.mark.skip("pending")
def test_empty():
    graph = Graph()
    node = Vertex("some other node")
    actual = graph.graph_depth_first(node)
    expected = []
    assert actual == expected

@pytest.fixture
def graph():
    letters = Graph()
    a = letters.add_node("a")
    b = letters.add_node("b")
    c = letters.add_node("c")
    d = letters.add_node("d")
    e = letters.add_node("e")
    f = letters.add_node("f")
    g = letters.add_node("g")
    h = letters.add_node("h")
    letters.add_edge(a, b)
    letters.add_edge(b, c)
    letters.add_edge(c, g)
    letters.add_edge(a, d)
    letters.add_edge(d, e)
    letters.add_edge(d, h)
    letters.add_edge(d, f)
    letters.add_edge(h, f)
    return letters

@pytest.fixture
def graph_and_root(graph):
    return graph, graph.get_nodes()[0]


