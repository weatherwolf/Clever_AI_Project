from NeuroEvolution.phenotype import Phenotype
from NeuroEvolution.genotype import Genotype
from NeuroEvolution.population import Population
from NeuroEvolution.network import Network

from clever.neuro_player import NeuroPlayer
from clever.game import Game

from neuroAdaptor import NeuroAdapter

import concurrent.futures
import threading

class Tournament:

    TOURNAMENT_SIZE: int = 4
    ROUND_SIZE: int = 2

    WORKERS: int = 20
    BATCH_SIZE: int = 5

    champion: Phenotype = None
    champions_score: float = 0.0

    contestants: list[Phenotype]
    contestants_genes: list[Genotype]

    def __init__(self) -> None:
        
        self.contestants = []
        self.contestants_genes = []
        Tournament._instance = self


    @classmethod
    def get_instance(cls):

        if cls._instance is None:

            cls._instance = cls()


        return cls._instance
    
    
    def initialise(self) -> None:

        INPUTS: int = 67
        OUTPUTS: int = 6

        Population._instance.generate_base_population(self.TOURNAMENT_SIZE, INPUTS, OUTPUTS)


    def execute_tournament(self) -> None:

        print(f"Tournament # {Population._instance.GENERATION}")

        self.contestants.clear()
        self.contestants_genes.clear()

        for i in range(self.TOURNAMENT_SIZE):

            Population._instance.genetics[i].bracket = 0
            Population._instance.population[i].score = 0

            self.contestants.append(Population._instance.population[i])
            self.contestants.append(Population._instance.genetics[i])

        
        while len(self.contestants) > 1:

            self.execute_tournament_round()

        
        for i in range(self.TOURNAMENT_SIZE):

            top: float = 0

            if self.champion:

                top = self.champion.bracket


            diff: float = Population._instance.genetics[i].bracket - top
            Population._instance.genetics[i].fitness = self.champion_score + diff * 5


        self.champion = self.contestants_genes[0]
        self.champion_score = self.contestants_genes[0].fitness



    def execute_tournament_round(self) -> None:

        # print(f"ROUND SIZE {len(self.contestants)}")

        # cs: list[Phenotype] = []
        # cs_genes: list[Genotype] = []

        # for i in range(len(self.contestants)):

        #     played: int = 0

        #     print(f"BRACKET ({ i/4 })")

        #     while played < self.ROUND_SIZE:
        #         print("Initialised Workers")

        #         with concurrent.futures.ThreadPoolExecutor(max_workers=self.WORKERS) as executor:

        #             futures = [executor.submit(self.play_game_thread, self, i) for _ in range(self.WORKERS)]

        #             for future in concurrent.futures.as_completed(futures):

        #                 future.result()


        #         played += self.WORKERS * self.BATCH_SIZE

        #         # for c in range(40):

        #         #     print("index: " + str(c) + ", " + "{0:0.000}".format(Monopoly.Analytics.instance.ratio[c]))

        #     mi = 0
        #     ms = self.contestants[i].score

        #     for j in [1,2,3,4]:

        #         if ms < self.contestants[i + j].score:

        #             mi = j
        #             ms = self.contestants[i + j].score

                
        #     for j in range(3):

        #         if j == mi:

        #             self.contestants_genes[i + j].bracket += 1
        #             continue
            
                
        #         self.contestants[i + j] = None


        i = 0
        while i < len(self.contestants):

            if self.contestants[i] is None:

                self.contestants.pop(i)
                self.contestants_genes.pop(i)

            else:

                i += 1

        return
    

    def play_game_thread(self, i: int):

        instance = Tournament.get_instance()
        

        for i in range(self.BATCH_SIZE):

            adapter: NeuroAdapter = NeuroAdapter()

            # Create a list of players that will play this game
            players: list[NeuroPlayer] = [NeuroPlayer(str(i), i, self.contestants[i], adapter),
                                        NeuroPlayer(str(i+1), i+1, self.contestants[i+1], adapter),
                                        NeuroPlayer(str(i+2), i+2, self.contestants[i+2], adapter),
                                        NeuroPlayer(str(i+3), i+3, self.contestants[i+3], adapter)]
            
            game: Game = Game(players=players)

            # Plays the game with the players
            game.start_game()

            if game.status == game.EState.WIN1:

                game.players[0].network.score += 1

            elif game.status == game.EState.WIN2:

                game.players[1].network.score += 1

            elif game.status == game.EState.WIN3:

                game.players[2].network.score += 1

            elif game.status == game.EState.WIN4:

                game.players[3].network.score += 1

            elif game.status == game.EState.DRAW:

                for player in game.players:

                    if player in game.winners:

                        player.network.score += 1/len(game.winners)
                    


            

            
