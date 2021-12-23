
class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, vertex):
        '''
        Adds a node to the graph
        Returns: The added node
        '''
        # vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        '''
        Adds a new edge between two nodes in the graph
        Returns: nothing
        '''
        if start_vertex not in self._adjacency_list:
            raise KeyError('Starting Vertex not found.')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not found')
        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        '''
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        '''
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        '''
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        '''
        return self._adjacency_list[vertex]

    def size(self):
        '''
        Returns the total number of nodes in the graph
        '''
        return len(self._adjacency_list)

class Vertex:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

