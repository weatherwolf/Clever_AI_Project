from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype

import random

class Marking:

    def __init__(self) -> None:
        self.order: int = 0
        self.source: int = 0
        self.destination: int = 0


class Mutation:

    _instance = None

    MUTATE_LINK: float = 0.2
    MUTATE_NODE: float = 0.1
    MUTATE_ENABLE: float = 0.6
    MUTATE_DISABLE: float = 0.2
    MUTATE_WEIGHT: float = 2.0

    PETRUB_CHANGE: float = 0.9
    SHIFT_STEP: float = 0.1

    @classmethod
    def get_instance(cls):

        if cls._instance is None:

            cls._instance = cls()

    
        return cls._instance
    
    
    def __init__(self) -> None:
        pass
    
    historical: list[Marking] = []

    #Really not sure what this method extactly does, what markings do and why we need to keep a history of them and change the history
    def register_marking(self, info: Edge) -> int:

        count: int = len(self.historical)

        for i in range(count):

            marking: Marking = self.historical[i]

            if(marking.source == info.source and marking.destination == info.destination):

                return marking.order
            
            
        creation: Marking = Marking()
        creation.order = len(self.historical)
        creation.source= info.source
        creation.destination = info.destination
        
        self.historical.append(creation)

        return len(self.historical) - 1
    

    def mutate_all(self, genotype: Genotype) -> None:

        p: float = self.MUTATE_WEIGHT

        while(p > 0):

            roll: float = random.random()

            if roll < p:

                self.mutate_weight(genotype)

            p -= 1


        p = self.MUTATE_LINK

        while(p > 0):

            roll: float = random.random()

            if roll < p:

                self.mutate_link(genotype)

            p -= 1


        p = self.MUTATE_NODE

        while(p > 0):

            roll: float = random.random()

            if roll < p:

                self.mutate_node(genotype)

            p -= 1
        
        
        p = self.MUTATE_DISABLE

        while(p > 0):

            roll: float = random.random()

            if roll < p:

                self.mutate_disabled(genotype)

            p -= 1

        
        p = self.MUTATE_ENABLE

        while(p > 0):

            roll: float = random.random()

            if roll < p:

                self.mutate_enable(genotype)

            p -= 1


    def mutate_link(self, genotype: Genotype) -> None:

        vertex_count: int = len(genotype.vertices)
        edge_count: int = len(genotype.edges)

        potential: list[Edge] = []

        for i in range(vertex_count):

            for j in range(vertex_count):

                source: int = genotype.vertices[i].index
                destination: int = genotype.vertices[j].index

                t1: Vertex.EType = genotype.vertices[i].type
                t2: Vertex.EType = genotype.vertices[j].type

                if (t1 == Vertex.EType.OUTPUT or t2 == Vertex.EType.INPUT):

                    continue


                if (source == destination):

                    continue

                search: bool = False

                for k in range(edge_count):

                    edge: Edge = genotype.edges[k]

                    if (edge.source == source and edge.destination == destination):

                        search = True
                        break

                
                if not search:

                    weight: float = random.random() * 4 - 2
                    creation: Edge = edge(source, destination, weight, True)

                    potential.append(creation)

        
        if len(potential) <= 0:

            return
        

        selection: int = random.random()

        mutation: Edge = potential[selection]
        mutation.innovation = self.register_marking(mutation)

        genotype.add_edge(mutation)


    def mutate_node(self, genotype: Genotype) -> None:

        edgeCount: int = len(genotype.edges)
        selection: int = random.randint(0, edgeCount)

        edge: Edge = genotype.edges[selection]

        if not edge.enabled:

            return
        

        edge.enabled = False

        vertex_new: int = genotype.vertices[len(genotype.vertices) - 1].index + 1

        vertex: Vertex = Vertex(vertex_new, Vertex.EType.HIDDEN)

        first: Edge = Edge(edge.source, vertex_new, 1.0, True)
        second: Edge = Edge(vertex_new, edge.destination, edge.weight, True)

        first.innovation = self.register_marking(first)
        second.innovation = self.register_marking(second)

        genotype.add_vertex(vertex)

        genotype.add_edge(first)
        genotype.add_edge(second)


    def mutation_enable(genotype: Genotype) -> None:
        
        edgeCount: int = len(genotype.edges)
        candidates: list[Edge] = []

        for i in range(edgeCount):

            if not genotype.edges[i].enabled:

                candidates.append(genotype.edges[i])

        
        if len(candidates) > 0:

            return
        

        selection: int = random.randint(0, len(candidates))

        edge: Edge = candidates[selection]
        edge.enabled = True

    
    def mutate_disabled(genotype: Genotype) -> None:

        edgeCount: int = len(genotype.edges)
        candidates: list[Edge] = []

        for i in range(edgeCount):

            if genotype.edges[i].enabled:

                candidates.append(genotype.edges[i])

        
        if len(candidates) == 0:

            return
        

        selection: int = random.randint(0, len(candidates))

        edge: Edge = candidates[selection]
        edge.enabled = False

    
    def mutate_weight(self, genotype: Genotype) -> None:

        selection: int = random.randint(0, len(genotype.edges))
        edge: Edge = genotype.edges[selection]

        roll: float = random.random()

        if roll < self.PETRUB_CHANGE:

            self.mutate_weight_shift(edge, self.SHIFT_STEP)

        else:

            self.mutate_weight_random(edge)

        
    def mutate_weight_shift(edge: Edge, step: float) -> None:

        scalar: float = random.random() * step - step * 0.5
        edge.weight += scalar

    
    def mutate_weight_random(edge: Edge) -> None:

        value: float = random.random * 4.0 - 2.0
        edge.weight = value




