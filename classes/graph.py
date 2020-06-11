class Graph():
    """We define a class of non orientated graphs.
    A graph is given by a set of vertices and a set of
    edges, given as couples of vertices
    
    """
    
    def __init__(self):
        self._vertices = set()
        self._edges = set()
        
    def __repr__(self):
        """Method to represent the graph by returning
        a string of the number of its vertices and edges
        
        """
        v = (len(self._vertices)<2)*"vertex" + (len(self._vertices)>1)*"vertices" 
        e = "edge"+(len(self._edges)>1)*'s'
        
        return("Graph composed of {} {} and {} {}".format(len(self._vertices), v, len(self._edges), e))
    
    def add_vertex(self, *vertices):
        """Method to add a vertex to a graph."""
        for vertex in vertices:           
            self._vertices.add(vertex)
        
    def add_edge(self, vertex1, vertex2):
        """Method to add an edge to a graph. If
        one of the vertex is not in the graph, raises an exception
        
        """
        if (vertex1 not in self._vertices):
            raise ValueError("Vertex {} is not in the graph".format(vertex1))
        elif  (vertex2 not in self._vertices):
            raise ValueError("Vertex {} is not in the graph".format(vertex2))
        else:
            self._edges.add(frozenset({vertex1,vertex2}))
            
    def remove_edge(self, vertex1, vertex2):
        """Method to remove an existing edge in a graph. 
        """
        self._edges.remove({vertex1, vertex2})
    
    def neighbours(self, vertex):
        """ Takes graph and a vertex from the graph as arguments and returns
        the set of vertices which are at distance 1 from the inputed vertex. 
        
        """
        if vertex not in self._vertices:
            raise ValueError("Vertex {} is not in the graph".format(vertex))
        neighbours = set()
        for vertex2 in self._vertices:
            if {vertex, vertex2} in self._edges:
                neighbours.add(vertex2)
        return neighbours
    
    def graph_distance(self, start, target, distance_tree = False ):
        """Takes three arguments: a graph, a starting vertex in the graph and a target, and returns
        the combinatorial distance between these vertices.
        
        If the option distance_tree is set to True, the function returns a dictionary whose keys are
        visited vertices during the program execution and whose arguments are the combinatorial distances 
        relative to start.
        
        """
        if (start not in self._vertices):
             raise ValueError("Vertex {} is not in the graph".format(start))
        if  (target not in self._vertices):
            raise ValueError("Vertex {} is not in the graph".format(target))
        totreat = [start]
        marked = set([start])
        tree = {start: 0}
        while totreat and target not in marked:
            v = totreat.pop(0)
            n = [vertex for vertex in self.neighbours(v) if vertex not in marked] 
            totreat += n
            for vertex in n:
                tree[vertex] = tree[v] + 1
                marked.add(vertex)                 
        if target not in marked:
            return float('inf')
        elif distance_tree:
            return tree
        else:
            return tree[target]
        
        
    def shortest_path(self, start, target):
        """Takes three arguments: a graph, a starting vertex in the graph and a target, and returns
        a shortest path as a list of vertices.
        
        
        """
        distances = self.graph_distance(start, target, True)
        if distances == float('inf'):
            raise ValueError('These vertices are not connected')
        cursor = target
        dist = distances[cursor]
        list_by_dist = [set() for i in range(dist +1)]
        path = [target]
        for vertex in distances:
            list_by_dist[distances[vertex]].add(vertex)
        while cursor != start:
            for vertex in self.neighbours(cursor):
                if vertex in list_by_dist[dist - 1]:
                    path = [vertex] + path
                    cursor = vertex
                    dist -= 1
        return path
       
        
       
