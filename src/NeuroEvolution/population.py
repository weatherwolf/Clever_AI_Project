from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype
from NeuroEvolution.mutation import Mutation
from NeuroEvolution.phenotype import Phenotype
from NeuroEvolution.species import Species
from NeuroEvolution.network import Network
from NeuroEvolution.crossover import Crossover

import random

class Population:

    _instance = None

    GENERATION: int = 0

    POPULATION_SIZE: int = 256
    INPUTS: int = 126
    OUTPUTS: int = 7
    MAX_STALENESS: int = 15

    PORTION: float = 0.2

    species: list[Species]
    genetics: list[Genotype]
    population: list[Phenotype]

    @classmethod
    def get_instance(cls):

        if cls._instance is None:

            cls._instance = cls()

    
        return cls._instance
    
    
    def __init__(self) -> None:
        
        self.species = []
        self.genetics = []
        self.population = []


    def generate_base_population(self, size: int, inputs: int, outputs: int):

        self.POPULATION_SIZE = size
        self.INPUTS = inputs
        self.OUTPUTS = outputs

        for i in range(self.POPULATION_SIZE):

            network: Network = Network.get_instance()
            genotype: Genotype = network.create_base_genotype(inputs, outputs)

            self.genetics.append(genotype)

            self.add_species(genotype)

        
        network.register_base_markings(inputs, outputs)

        for i in range(self.POPULATION_SIZE):

            mutation_instance: Mutation = Mutation.get_instance()
            mutation_instance.mutate_all(self.genetics[i])

        
        self.inscribe_population()


    def ner_generation(self) -> None:

        self.calculate_adjusted_fitness()

        i: int = 0

        while i < len(self.species):

            self.species[i].sort_members()
            self.species[i].cull_to_portion(self.PORTION)

            if len(self.species[i].members) <= 1:

                self.species.pop(i)
            
            else: 

                i += 1

            
            self.update_staleness()

            fitness_sum: float = 0.0

            for i in range(len(self.species)):

                self.species[i].calculate_adjusted_fitness()
                fitness_sum += self.species[i].fitness_sum


            children: list[Genotype] = []

            for i in range(len(self.species)):

                build: int = (int)(self.POPULATION_SIZE * (self.species[i].fitness_sum / fitness_sum) - 1)

                for j in range(build):

                    child: Genotype = self.species[i].breed()
                    children.append(child)

                
            while(self.POPULATION_SIZE > len(self.species) + len(children)):

                child: Genotype = self.species[random.randint(0, len(self.species))].breed()
                children.append(child)

            for i in range(len(self.species)):

                self.species[i].cull_to_one()

            
            children_count: int = len(children)

            for i in range(children_count):

                self.add_to_species(children[i])

            
            self.genetics.clear()

            self.GENERATION += 1


    def update_staleness(self) -> None:

        species_count: int = len(self.species)
        i: int = 0
        while i < species_count:

            if species_count == 1:

                return
            

            top: float = self.species[i].members[0].fitness

            if self.species[i].top_fitness < top:

                self.species[i].top_fitness = top
                self.species[i].staleness = 0

            else:

                self.species[i].staleness += 1

            
            if self.species[i].staleness >= self.MAX_STALENESS:

                self.species.pop(i)
                species_count -= 1
            
            else:

                i += 1


    def inscribe_population(self) -> None:

        self.population.clear()

        for i in range(self.POPULATION_SIZE):

            self.genetics[i].fitness = 0.0
            self.genetics[i].adjusted_fitness = 0.0

            physical: Phenotype = Phenotype()
            physical.inscribe_genotype(self.genetics[i])
            physical.process_graph

            self.population.append(physical)


    def add_species(self, genotype: Genotype) -> None:

        if len(self.species) == 0:

            new_species: Species = Species()
            new_species.members.append(genotype)

        
        else:

            species_count: int = len(self.species)
            
            found: bool = False

            for i in range(species_count):

                crossover_instance = Crossover.get_instance()
                distance: float = crossover_instance.speciation_distance(self.species[i].members[0], genotype)

                if distance < crossover_instance.DISTANCE:

                    self.species[i].members.append(genotype)
                    found = True
                    break


                if not found:

                    new_species: Species = Species()
                    new_species.members.append(genotype)

    



        



            





