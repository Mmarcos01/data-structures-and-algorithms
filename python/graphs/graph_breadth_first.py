from stacks_queues.stacks_queues import Node, Queue
from graph import Graph

def graph_breadth_first(vertex):
    nodes = []
    breadth = Queue()
    visited = set()

    breadth.enqueue(vertex)
    visited.add(vertex)

    while not breadth.is_empty():
        front = breadth.dequeue()
        nodes.append(vertex)

        for child in front.next:
            if child not in visited:
                visited.append(child)
                breadth.enqueue(child)
    return nodes

