import random

from NeuroEvolution.phenotype import Phenotype
from NeuroEvolution.genotype import Genotype

from clever.neuro_player import NeuroPlayer

class RNG:
    _instance = None

    def __init__(self):

        self.gen = random.Random()


    @staticmethod
    def initialise():

        if RNG._instance is None:

            RNG._instance = RNG()


    def shuffle_neural_players(self, players: list[NeuroPlayer]):

        container = list(players)
        shuffle = []

        while container:
            r = self.gen.randint(0, len(container) - 1)
            shuffle.append(container.pop(r))

        return shuffle

    def shuffle_phenotypes(self, phenotypes: list[Phenotype]):

        shuffle = []

        while phenotypes:

            r = self.gen.randint(0, len(phenotypes) - 1)

            shuffle.append(phenotypes.pop(r))


        return shuffle
    

    def double_shuffle(self, phen: list[Phenotype], gene: list[Genotype], op: Phenotype, og: Genotype):

        while phen:

            r = self.gen.randint(0, len(phen) - 1)

            op.append(phen.pop(r))
            og.append(gene.pop(r))
