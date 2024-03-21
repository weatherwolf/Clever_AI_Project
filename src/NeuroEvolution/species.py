from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype
from NeuroEvolution.mutation import Mutation
from NeuroEvolution.crossover import Crossover

import math
import random

class Species:

    def __init__(self) -> None:
        
        self.members: list[Genotype] = []

    
    members: list[Genotype] = []

    top_fitness: float = 0.0
    staleness: int = 0
    fitness_sum: float = 0.0


    def breed(self) -> Genotype:

        roll: float = random.random()
        crossover_instance: Crossover = Crossover.get_instance()
        mutation_instance: Mutation = Mutation.get_instance()

        if (roll <= crossover_instance.CROSSOVER_CHANCE or len(self.members > 1)):

            s1: int = random.randint(0, len(self.members))
            s2: int = random.randint(0, len(self.members) - 1)

            if (s2 >= s1):

                s2 += 1

            else:

                temp: int = s1
                s1 = s2
                s2 = temp

            
            child: Genotype = Crossover.produce_offspring(Species.members[s1], Species.members[s2])
            
            mutation_instance.mutate_all(child)

            selection:int = random.randint(0, len(self.members))

            return child
        
        else:

            selection: int = random.randint(0, len(self.members))

            child: Genotype = self.members[selection].clone()
            mutation_instance.mutate_all(child)

            return child
        
    
    def sort_members(self) -> None:

        self.members.sort(key=lambda genotype: genotype.adjusted_fitness, reverse=True)

    
    def remove_range(self, start: int, end: int) -> None:
        self.members = self.members[:start] + self.members[end:]
        
    
    def cull_to_portion(self, portion: float) -> None:

        if len(self.members <+ 1):

            return
        
        
        remaining: int = math.ceil(len(self.members) * portion)
        self.remove_range(remaining, len(self.members) - remaining)


    def cull_to_one(self) -> None:

        if len(self.members) <= 1:

            return
        
        self.remove_range(1, len(self.members) - 1)

    
    def calculate_adjusted_fitness(self) -> None:

        sum: float = 0.0
        members_count: int = len(self.members)

        for i in range(members_count):

            sum += self.members[i].adjusted_fitness

        
        self.fitness_sum = sum



        