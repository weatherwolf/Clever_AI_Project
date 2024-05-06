import numpy as np

from clever.player import Player
from clever.round import Round
from clever.neuro_player import NeuroPlayer
from clever.bonus_specific import Reroll, PlusOne

from config import Config

class Game:


    def __init__(self, players: list[NeuroPlayer]) -> None:
        
        self.players = players
        self.current_player_index = 0
        self.round_number = 1
        self.rounds = []
        self.number_of_rounds = self.number_of_Rounds()
        self.status = self.EState.ONGOING
        self.winners = []

        self.printing = Config.printing


    class EState:

        ONGOING = 0
        DRAW = 1
        WIN1 = 2
        WIN2 = 3
        WIN3 = 4
        WIN4 = 5


    def number_of_Rounds(self) -> int:
        
        if np.size(self.players) < 3: 

            return 6
        
        elif np.size(self.players) == 3:

            return 5
        
        elif np.size(self.players) == 4:

            return 4
        
        else:

            return 0
        

    def start_game(self) -> None:
        
        if self.printing:

            print("Starting a new game!")


        self.initialize_rounds()
        self.play_rounds()
        self.end_game()


    def initialize_rounds(self) -> None:

        for _ in range(len(self.number_of_rounds * self.players)):

            round = Round()
            self.rounds.append(round)


    def play_rounds(self) -> None:
        
        for i in range(self.number_of_rounds):
            
            if self.printing:

                print(f"\nRound {self.round_number}")


            for j in range(len(self.players)):
                
                player = self.players[j]

                if i+1 == 1 or i+1 == 3:
                
                    reroll = Reroll()
                    reroll.power(player=player)

                elif i+1 == 2:

                    plusOne = PlusOne()
                    plusOne.power(player=player)

                elif i+1 == 4:

                    player.player_act_on_bonus(player.player_choose_bonus())
                

                if self.printing:

                    print(f"round currently being played: {j + np.size(self.players) * i}")
                
                
                self.play_round(self.rounds[j + np.size(self.players) * i], player)


            self.round_number += 1


    def play_round(self, round: Round, player: NeuroPlayer) -> None:

        if self.printing:

            print(f"\n{player.name}'s turn:")
        
        
        self.play_turn(player, round)


    def play_turn(self, player: Player, round: NeuroPlayer) -> None:
        
        if self.printing:
            
            print("Rolling dice...")
        
        
        player_actions = 3

        while player_actions > 0:
            
            if self.printing:

                print(f"\nActions remaining: {player_actions}")


            round.roll_dice()
            chosen_dice = player.action(round, True)  

            # If last turn of the round, discard all the dice that are not chosen
            round.choose_dice(chosen_dice, player_actions)
            
            player_actions -= 1
        
        for p in self.players:

            if p != player:

                p.inactive_turn(round)
                

    def end_game(self) -> None:

        if self.printing:
            
            print("")


        highest_score: int = 0

        for player in self.players:

            if self.printing:

                for board in player.boards:

                    print(f"The score of the {board.print_color_value()} board is: {board.get_score()}")


            if highest_score < player.get_total_score():

                self.winners.clear()
                self.winners.append(player)

                highest_score = player.get_total_score()


            elif highest_score == player.get_total_score():
                
                self.winners.append(player)
                self.status = self.EState.DRAW


            if self.printing:

                print(f"The bonuses of {player.name} are: {player.bonuses}")
                print(f"The final score of {player.name} is {player.get_total_score()}\n")


        if len(self.winners) == 1:

            if self.winners[0] == self.players[0]:

                self.status = self.EState.WIN1

            elif self.winners[0] == self.players[1]:

                self.status = self.EState.WIN2

            elif self.winners[0] == self.players[2]:

                self.status = self.EState.WIN3

            elif self.winners[0] == self.players[3]:

                self.status = self.EState.WIN4     


        if self.printing:  

            print(f"Game Status: {self.status}")
            print("")
            print("End of the Game")



        