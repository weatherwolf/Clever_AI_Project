import numpy as np

from clever.board import Board
from clever.space import Space
from clever.round import Round
from clever.dice import Dice
from clever.neuro_player import NeuroPlayer

class NeuroAdapter:

    num_yellow: int = 0
    num_blue: int = 16
    num_green: int = 28
    num_orange: int = 39
    num_purple: int = 50

    num_round: int = 61
    num_plus_one: int = num_round + 1
    num_reroll: int = num_plus_one + 1
    num_fox_count: int = num_reroll + 1
    num_score: int = num_fox_count + 1
    num_index: int = num_score + 1
    num_dice: int = num_index + 1

    pack: list[float] = []


    def __init__(self) -> None:

        self.pack = []

    
    def reset(self) -> None:

        player: NeuroPlayer = NeuroPlayer("temp")
        self.pack = []
    

    def convert_board(self, board: Board) -> None:

        if board.color == "Yellow":

            for i in range(0, self.num_yellow):

                self.pack[i] = 0

                if board.all_spaces[i].crossed:

                    self.pack[i] = 1


        elif board.color == "Blue":

            for i in range(self.num_yellow, self.num_yellow + self.num_blue):
                
                j: int = i - self.num_yellow
                self.pack[i] = 0

                if board.all_spaces[j].crossed:

                    self.pack[i] = 1


        elif board.color == "Green":

            for i in range(self.num_blue, self.num_blue + self.num_green):

                j: int = i - self.num_blue
                self.pack[i] = 0

                if board.all_spaces[j].crossed:

                    self.pack[i] = 1

        
        elif board.color == "Orange":

            for i in range(self.num_green, self.num_green + self.num_orange):

                j: int = i - self.num_green
                self.pack[i] = board.all_spaces[j].dice_value/6

        
        elif board.color == "Purple":

            for i in range(self.num_orange, self.num_orange + self.num_purple):

                j: int = i - self.num_orange
                self.pack[i] = board.all_spaces[j].dice_value/6

    
    def convert_dice(self, round: Round) -> None:

        total_dice: list[Dice] = round.total_dice

        for i in range(6):

            self.pack[i + self.num_dice] = total_dice[i].value / 6

    
    def convert_space(self, board: Board, space: Space) -> None:

        if board.color == "Yellow":

            self.pack[space.index] = 0

            if space.crossed:

                self.pack[space.index] = 1


        elif board.color == "Blue":

            self.pack[space.index + self.num_blue] = 0

            if space.crossed:

                self.pack[space.index + self.num_blue] = 1


        elif board.color == "Green":

            self.pack[space.index + self.num_green] = 0

            if space.crossed:

                self.pack[space.index + self.num_green] = 1

        
        elif board.color == "Orange":

            self.pack[space.index + self.num_orange] = space.dice_value/6

        
        elif board.color == "Purple":

            self.pack[space.index + self.num_purple] = space.dice_value/6


    def convert_player(self, player: NeuroPlayer) -> None:

        self.pack[self.num_reroll] = player.reroll_count
        self.pack[self.num_plus_one] = player.plusOne_count
        self.pack[self.num_fox_count] = player.fox_count
        self.pack[self.num_score] = player.get_total_score()
        self.pack[self.num_index] = player.index

        
    def convert_all(self, round: Round, player: NeuroPlayer) -> None:

        for board in player.boards:

            self.convert_board(board)

            self.pack[self.num_reroll] = player.reroll_count
            self.pack[self.num_plus_one] = player.plusOne_count
            self.pack[self.num_fox_count] = player.fox_count
            self.pack[self.num_score] = player.get_total_score()
            self.pack[self.num_index] = player.index

            self.convert_dice(round)

    
    def set_turn(self, index: int) -> None:

        self.pack[self.num_round] = index


    

    

    


    




            




        

                



        