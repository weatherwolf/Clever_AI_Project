from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge

class Genotype:

    def __init__(self, vertices: list[Vertex] = [], edges: list[Edge] = []) -> None:

        self.vertices = vertices
        self.edges = edges

        self.inputs = 0
        for v in self.vertices:
            if v.type == Vertex.EType.INPUT:
                self.inputs += 1

        self.fitness = 0.0
        self.adjusted_fitness = 0.0


    def add_vertex(self, v: Vertex) -> None:
        
        self.vertices.append(v)
        if v.type == Vertex.EType.INPUT:
            self.inputs += 1


    def add_edge(self, e: Edge) -> None:
        
        self.edges.append(e)


    def clone(self):

        clone = Genotype()
        for v in self.vertices:
            clone.add_vertex(v)

        for e in self.edges:
            clone.add_edge(e)

        return clone
    

    def sort_typology(self) -> None:

        self.sort_vertices()
        self.sort_edges()


    def sort_vertices(self) -> None:
        
        self.vertices.sort(key=lambda v: v.index)

    def sort_edges(self) -> None:

        self.edges.sort(key=lambda e: e.innovation)



