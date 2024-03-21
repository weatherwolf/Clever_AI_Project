from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype

import random

class Crossover:

    _instance = None


    CROSSOVER_CHANCE: float = 0.75
    C1: float = 1.0
    C2: float = 1.0
    C3: float = 0.4
    DISTANCE: float = 1.0

    @classmethod
    def get_instance(cls):

        if cls._instance is None:

            cls._instance = cls()

    
        return cls._instance
    
    
    def __init__():
        pass


    def produce_offspring(first: Genotype, second: Genotype) -> Genotype:

        copy_first: list[Edge] = []
        copy_second: list[Edge] = []

        copy_first.extend(first)
        copy_second.extend(second)

        match_first: list[Edge] = []
        match_second: list[Edge] = []

        disjoint_first: list[Edge] = []
        disjoint_second: list[Edge] = []

        excess_first: list[Edge] = []        
        excess_second: list[Edge] = []

        genes_first: int = len(first.edges)
        genes_second: int = len(second.edges)        

        invmax_first: int = first.edges[len(first.edges) - 1].innovation
        invmax_second: int = first.edges[len(second.edges) -1].innovation

        invmin: int = min(invmax_first, invmax_second)
        i: int = 0

        while i < genes_first:

            for j in range(genes_second):

                info_first: Edge = copy_first[i]
                info_second: Edge = copy_second[j]

                #matching genes
                if(info_first.innovation == info_second.innovation):

                    match_first.append(info_first)
                    match_second.append(info_second)

                    copy_first.remove(info_first)
                    copy_second.remove(info_second)

                    genes_first -= 1
                    genes_second -= 1
                    break

                else: 

                    i += 1
        

        for i in range(len(copy_first)):

            if copy_first[i].innovation > invmin:

                excess_first.append(copy_first[i])

            else:

                disjoint_first.append(copy_first[i])


        for i in range(len(copy_second)):

            if copy_second[i].innovation > invmin:

                excess_second.append(copy_second[i])

            else:

                disjoint_second.append(copy_second[i])

            
        child: Genotype = Genotype()
        matching: int = len(match_first)

        for i in range(matching):

            roll: int = random.randint(0, 2)

            if (roll == 0 or not match_second[i].enabled):

                child.add_edge(match_first[i])

            else:

                child.add_edge(match_second[i])

            
        for i in range(len(disjoint_first)):

            child.add_edge(disjoint_first[i])

        
        for i in range(len(excess_first)):

            child.add_edge(excess_first[i])


        child.sort_edges()

        ends: list[int] = []
        vertex_count: int = len(first.vertices)

        for i in range(vertex_count):

            vertex: Vertex = first.vertices[i]

            if vertex.type == Vertex.EType.HIDDEN:
                break


            ends.append(vertex.index)
            child.add_vertex(vertex)

            child.sort_vertices()

            return child
        

    def add_unique_vertices(genotype: Genotype, ends: list[int]) -> None:

        unique: list[int] = []
        edgeCount: int = len(genotype.edges)

        for i in range(edgeCount):

            info: Edge = genotype.edges[i]

            if(info.destination not in ends and info.destination not in unique):

                unique.append(info.destination)


            uniques: int = len(unique)

            for i in range(uniques):

                genotype.add_vertex(unique[i], Vertex.EType.HIDDEN)


    def speciation_distance(first: Genotype, second: Genotype) -> float:
        
        copy_first: list[Edge] = []
        copy_second: list[Edge] = []

        copy_first.extend(first)
        copy_second.extend(second)

        match_first: list[Edge] = []
        match_second: list[Edge] = []

        disjoint_first: list[Edge] = []
        disjoint_second: list[Edge] = []

        excess_first: list[Edge] = []        
        excess_second: list[Edge] = []

        genes_first: int = len(first.edges)
        genes_second: int = len(second.edges)        

        invmax_first: int = first.edges[len(first.edges) - 1].innovation
        invmax_second: int = first.edges[len(second.edges) -1].innovation

        invmin: int = min(invmax_first, invmax_second)

        diff: float = 0.0
        i: int = 0

        while i < genes_first:

            for j in range(genes_second):

                info_first: Edge = copy_first[i]
                info_second: Edge = copy_second[j]

                #matching genes
                if(info_first.innovation == info_second.innovation):

                    weight_difference : float = abs(info_first.weight - info_second.weight)
                    diff += weight_difference

                    match_first.append(info_first)
                    match_second.append(info_second)

                    copy_first.remove(info_first)
                    copy_second.remove(info_second)

                    genes_first -= 1
                    genes_second -= 1
                    break

                else:

                    i += 1

        
        for i in range(len(copy_first)):

            if copy_first[i].innovation > invmin:

                excess_first.append(copy_first[i])

            else:

                disjoint_first.append(copy_first[i])


        for i in range(len(copy_second)):

            if copy_second[i].innovation > invmin:

                excess_second.append(copy_second[i])

            else:

                disjoint_second.append(copy_second[i])

        
        match: int = len(match_first)
        disjoint: int = len(disjoint_first) + len(disjoint_second)
        excess: int = len(excess_first) + len(excess_second)

        n: int = max(len(first.edges), len(second.edges))

        E: float = excess / n
        D: float = disjoint / n
        W: float = diff / match

        return E * Crossover.C1 + D * Crossover.C2 + W * Crossover.C3
    



        





            
        

            