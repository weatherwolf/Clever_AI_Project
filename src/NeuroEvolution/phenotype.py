from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype

import numpy as np


class Phenotype:

    def __init__(self) -> None:

        self.vertices: list[Vertex] = []
        self.edges: list[Edge] = []
        self.vertices_inputs: list[Vertex] = []
        self.vertices_outputs: list[Vertex] = []

        self.score: float = 0 

    
    def sigmoid(x: float) -> float:
        
        return 1/(1 + np.exp(-x))
    

    def add_vertex(self, type: Vertex.EType, index: int) -> None:

        v: Vertex = Vertex(type, index)
        self.vertices.append(v)


    def add_edge(self, source: int, destination: int, weight: float, enabled: bool) -> None:

        e: Edge = Edge(source, destination, weight, enabled)
        self.edges.append(e)

        self.vertices[e.destination].incoming.append(e)

    

    def inscribe_genotype(self, code: Genotype) -> None:

        self.vertices = []
        self.edges = []

        vertex_count: int = len(code.vertices)
        edge_count: int = len(code.edges)

        for i in range(vertex_count):

            self.add_vertex(code.vertices[i].index, code.vertices[i].type)

        for i in range(edge_count):

            e: Edge = code.edges[i]
            self.add_edge(e.source, e.destination, e.weight, e.enabled)

    
    def process_graph(self) -> None:

        vertices_count: int = len(self.vertices)

        for i in range(vertices_count):

            vertex: Vertex = self.vertices[i]

            if (vertex.type == Vertex.EType.INPUT):

                self.vertices_inputs.append(vertex)


            if (vertex.type == Vertex.EType.OUTPUT):

                self.vertices_outputs.append(vertex)

    
    def reset_graph(self):

        vertices_count: int = len(self.vertices)

        for i in range(vertices_count):

            vertex: Vertex = self.vertices[i]
            vertex.value = 0.0

    
    def propagate(self, X: list[float]) -> list[float]:

        repeats: int = 10

        for e in range(repeats):

            for i in range(len(self.vertices_inputs)):

                self.vertices_inputs[i].value = X[i]


            for i in range(len(self.vertices)):

                if self.vertices[i].type == Vertex.EType.OUTPUT:
                    
                    continue


                paths: int = len(self.vertices[i].incoming)

                for j in range(paths):

                    enabled: float = 1.0 if self.vertices[i].incoming[j].enabled else 0.0
                    self.vertices[i].value += self.vertices[self.vertices[i].incoming[j].source].value * enabled

                
                if len(self.vertices[i].incoming) > 0:

                    self.vertices[i].value = self.sigmoid(self.vertices[i].value)


            Y: list[float] = []

            for i in range(len(self.vertices_outputs)):

                paths: int = len(self.vertices_outputs[i].incoming)

                for j in range(paths):

                    enabled: float = 1.0 if self.vertices_outputs[i].incoming[j].enabled else 0.0
                    self.vertices_outputs[i] += self.vertices[self.vertices_outputs[i].incoming[j].source] * enabled


                if len(self.vertices_outputs[i].incoming) > 0:

                    self.vertices_outputs[i].value = self.sigmoid(self.vertices_outputs[i].value)
                    Y[i] = self.vertices[i].value

        
        if e == repeats - 1:

            return Y
        
    
        return []

            



