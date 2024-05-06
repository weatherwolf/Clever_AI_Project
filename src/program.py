from NeuroEvolution.mutation import Mutation
from NeuroEvolution.crossover import Crossover
from NeuroEvolution.population import Population
from NeuroEvolution.genotype import Genotype
from NeuroEvolution.mutation import Marking, Mutation
from NeuroEvolution.species import Species
from NeuroEvolution.vertex import Vertex
from NeuroEvolution.vertex import Edge

from neuroAdaptor import NeuroAdapter
from tournament import Tournament
from rng import RNG

import numpy as np
import os

class Program:

    def __init__(self):
        
        print("test")
        self.main()


    def main(self):

        print(f"I'm in the program.py file, running the code")

        path: str = "C:/Users/wolfb/OneDrive/Documenten/Projecten/Clever AI/clever.txt"

        RNG.initialise()

        NeuroAdapter()

        Mutation.initialise()
        Crossover.initialise()
        Population.initialise()

        tournament: Tournament = Tournament()

        # if os.path.exists(path):
            
        #     print('test')

        #     self.load_state(path, tournament)

        # else:
        
        #     tournament.initialise()

        tournament.initialise()


        for i in range(1000):

            print(f"tournament {i}")

            tournament.execute_tournament()
            Population._instance.new_generation()
            self.save_state(path, tournament)

            
        
    def save_state(self, target: str, tournament: Tournament):

        print(f"SAVE POPULATION")

        build: str = ""
        build2: str = ""

        build += str(Population._instance.GENERATION)
        build += ";"
        build += str(tournament.champion_score)
        build += ";"

        markings: int = 0

        for i in range(len(Mutation._instance.historical)):

            build += Mutation._instance.historical[i].order
            build += ","

            build += Mutation._instance.historical[i].source
            build += ','

            build += Mutation._instance.historical[i].destination

            if i != len(Mutation._instance.historical) - 1:

                build += ','

            markings += 1


        net_build: list[str] = []
        net_count: int = -1
        gene_count: int = 0

        build += ';'

        for i in range(len(Population._instance.species)):

            net_build.append("")
            net_count += 1

            net_build[net_count] += str(Population._instance.species[i].top_fitness)
            net_build[net_count] += ','
            net_build[net_count] += str(Population._instance.species[i].staleness)
            net_build[net_count] += "&"

            members: int = len(Population._instance.species[i].members)

            for j in range(members):

                net_build.append("")
                net_count += 1
                gene_count += 1

                print(f"{gene_count}/{len(Population._instance.genetics)}")

                genes: Genotype = Population._instance.species[i].members[j]

                vertices: int = len(genes.vertices)

                for k in range(vertices):

                    net_build[net_count] += str(genes.vertices[k].index)
                    net_build[net_count] += ','
                    net_build[net_count] += str(genes.vertices[k].type)
                    net_build[net_count] += ','

                
                net_build[net_count] += "#"

                edges: int = len(genes.edges)

                for k in range(edges):

                    net_build[net_count] += str(genes.edges[k].source)
                    net_build[net_count] += ','
                    net_build[net_count] += str(genes.edges[k].destination)
                    net_build[net_count] += ','
                    net_build[net_count] += str(genes.edges[k].weight)
                    net_build[net_count] += ','
                    net_build[net_count] += str(genes.edges[k].enabled)
                    net_build[net_count] += ','
                    net_build[net_count] += str(genes.edges[k].innovation)
                    net_build[net_count] += ','
                
                if j != members - 1:

                    net_build[net_count] += 'n'

            
            if i != len(Population._instance.species) - 1:

                net_build[net_count] += '&'

        build2 += ';'

        with open(target, 'w') as file:

            file.write(build)
            
            for b in net_build:
                file.write(b)
            

            file.write(build2)  


        print(f"{markings} MARKINGS")


    def load_state(self, location: str, tournament: Tournament):

        load: str = ""

        with open(location, 'r') as file:

            file.read()


        parts: list[str] = load.split(';')

        gen: int = int(parts[0])
        score: float = float(parts[1])

        Population._instance.GENERATION = gen
        tournament.champions_score = score

        marking_string: str = parts[2]
        markings_parts: list[str] = marking_string.split(',')

        i: int = 0

        while i < range(np.shape(markings_parts)[0]):

            order: int = int(markings_parts[i])
            source: int = int(markings_parts[i + 1])
            destination: int = int(markings_parts[i + 2])

            recreation: Marking = Marking()

            recreation.order = order
            recreation.source = source
            recreation.destination = destination

            Mutation._instance.historical.append(recreation)

            i += 3 

        
        network_string: str = parts[3]
        species_parts: list[str] = network_string.split('&')
        
        x: int = 0

        while x < np.shape(species_parts)[0]:

            first_parts: list[str] = species_parts[x].split(',')

            Population._instance.species.append(Species())
            Population._instance.species[len(Population._instance.species) - 1].top_fitness = float(first_parts[0])
            Population._instance.species[len(Population._instance.species) - 1].staleness = float(first_parts[1])
            
            network_parts: str[list] = species_parts[x+1].split('n')

            for i in range(np.size(network_parts)[0]):

                genotype: Genotype = Genotype()

                network: str = network_parts[i]
                nparts: list[str] = network.split("#")

                verts: str = nparts[0]
                vparts: list[str] = verts.split(",")

                j: int = 0

                while j < np.size(vparts)[0] - 1:

                    index: int = int(vparts[j])
                    type: Vertex.EType = Vertex.EType[vparts[j+1]]

                    genotype.add_vertex(Vertex(index, type))

                    j += 2

                edges: str = nparts[1]
                eparts: list[str] = edges.split(',')

                j = 0

                while j < np.size(eparts)[0] - 1:

                    source: int = int(eparts[j])
                    destination: int = int(eparts[j+1])
                    weight: float = float(eparts[j+2])
                    enabled: bool = bool(eparts[j+3])
                    innovation: int = int(eparts[j+4])

                    genotype.add_edge(Edge(source, destination, weight, enabled, innovation))

                    j += 5

                
                Population._instance.species[len(Population._instance.species) - 1].members.append(genotype)
                Population._instance.genetics.append(genotype)


            x += 2


        Population._instance.inscribe_population()
            
            

        



                    