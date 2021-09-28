from stacks_queues.stacks_queues import Node, Queue
from graph import Graph


def graph_breadth_first(vertex):
    nodes = []
    breadth = Queue()
    visited = set()

    breadth.enqueue(vertex)
    visited.add(vertex)

    while not breadth.isEmpty():
        front = breadth.dequeue()
        nodes.append(vertex)

        for child in front.next:
            if child not in visited:
                visited.append(child)
                breadth.enqueue(child)
    return nodes

# ALGORITHM 
# BreadthFirst(vertex)
#     DECLARE nodes <-- new List()
#     DECLARE breadth <-- new Queue()
#     DECLARE visited <-- new Set()

#     breadth.Enqueue(vertex)
#     visited.Add(vertex)

#     while (breadth is not empty)
#         DECLARE front <-- breadth.Dequeue()
#         nodes.Add(front)

#         for each child in front.Children
#             if(child is not visited)
#                 visited.Add(child)
#                 breadth.Enqueue(child)

#     return nodes;
