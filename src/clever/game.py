import numpy as np

from clever.player import Player
from clever.round import Round
from clever.bonus_specific import Reroll, PlusOne

class Game:

    def __init__(self, players: list[Player]) -> None:
        
        self.players = players
        self.current_player_index = 0
        self.round_number = 1
        self.rounds = []
        self.number_of_rounds = self.number_of_Rounds()


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
        
        print("Starting a new game!")
        self.number_of_Rounds()
        self.initialize_rounds()
        self.play_rounds()
        self.end_game()


    def initialize_rounds(self) -> None:
        
        for _ in range(len(self.number_of_rounds * self.players)):
            round = Round()
            self.rounds.append(round)


    def play_rounds(self) -> None:
        
        for i in range(self.number_of_rounds):
            print(f"\nRound {self.round_number}")
            for player in self.players:
                print(f"The value of i: {i+1}")
                if i+1 == 1 or i+1 == 3:
                    Reroll.power(player)
                elif i+1 == 2:
                    PlusOne.power(player)
                elif i+1 == 4:
                    print("test")
                    player.player_act_on_bonus(player.player_choose_bonus())

                self.play_round(self.rounds[player.index + np.size(self.players) * i], player)

            self.round_number += 1


    def play_round(self, round: Round, player: Player) -> None:
        
        print(f"\n{player.name}'s turn:")
        self.play_turn(player, round)


    def play_turn(self, player: Player, round: Round) -> None:
        
        print("Rolling dice...")
        player_actions = 3

        while player_actions > 0:
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
        
        print("")
        for player in self.players:
            for board in player.boards:
                print(f"The score of the {board.print_color_value()} board is: {board.get_score()}")
            print(f"The bonuses of {player.name} are: {player.bonuses}")
            print(f"The final score of {player.name} is {player.get_total_score()}\n")
        
        print("")
        print("End of the Game")
        