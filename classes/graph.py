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
    
    def shortest_path(self, start, target):
        """Takes three arguments: a graph, a starting vertex in the graph and a target, and returns
        a shortest path as a list of vertices.
        
        """
        if (start not in self._vertices):
             raise ValueError("Vertex {} is not in the graph".format(start))
        if  (target not in self._vertices):
            raise ValueError("Vertex {} is not in the graph".format(target))
        totreat = [start]
        marked = set([start])
        paths = [[start]]
        shortest_path = []
        while totreat and target not in marked:
            v = totreat.pop(0)
            n = self.neighbours(v)
            for p in paths:
                if p[-1] == v:
                    for vertex in n:
                        paths.append(p + [vertex])                    
            totreat += [vertex for vertex in n if vertex not in marked]
            for vertex in n:
                marked.add(vertex)
        for p in paths:
            if p[-1] == target:
                shortest_path = p
                break
        if target not in marked:
            return('Sorry, there is no path between these points')
        else:
            return shortest_path
        
       
