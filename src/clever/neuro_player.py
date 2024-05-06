import random

from clever.dice import Dice
from clever.space import Space
from clever.board import Board
from clever.round import Round
from clever.bonus import Bonus
from clever.player import Player
from clever.bonus_specific import *
from clever.board_specific import *

from NeuroEvolution.phenotype import Phenotype

from config import Config


class NeuroPlayer(Player):

    def __init__(self, name: str, index: int, phenotype: Phenotype = None, adapter = None) -> None:

        super().__init__(name, 0, [YellowBoard(), BlueBoard(), GreenBoard(), OrangeBoard(), PurpleBoard()], index)
        
        self.phenotype: Phenotype = phenotype
        self.adapter = adapter
        self.printing = Config.printing
        
    
    def player_choose_dice(self, dice: list[Dice]) -> Dice:
        
        # return random.choice(dice)

        Y: list[float] = self.phenotype.propagate(self.adapter.pack)
        count_dice: int = len(dice)

        for i in range(count_dice):

            if Y[0] <= (i + 1)/count_dice:

                return dice[i]
            
            
        return dice[count_dice - 1]
        
    
    
    def player_choose_board(self, boards: list[Board]) -> Board:

        # return random.choice(boards)

        Y: list[float] = self.phenotype.propagate(self.adapter.pack)
        count_boards: int = len(boards)

        for i in range(count_boards):

            if Y[1] <= 0.7:

                return boards[i]
            
            
        return boards[count_boards - 1]
    
        
    def player_choose_space(self, available_spaces: list[Space]) -> Space:
        
        # return random.choice(available_spaces)

        Y: list[float] = self.phenotype.propagate(self.adapter.pack)
        count_available_spaces: int = len(available_spaces)

        for i in range(count_available_spaces):

            if Y[2] <= (i + 1)/count_available_spaces:

                return available_spaces[i]
            
            
        return available_spaces[count_available_spaces - 1]
        
    
    def player_choose_bonus(self) -> list[Bonus]:

        yellowX = YellowX()
        blueX = BlueX()
        greenX = GreenX()
        orangeX = OrangeX(6)
        purpleX = PurpleX(6)
        
        bonus_list: list[Bonus] = [yellowX, blueX, greenX, orangeX, purpleX]

        # bonus: Bonus = random.choice(bonus_list)
        # return [bonus]

        Y: list[float] = self.phenotype.propagate(self.adapter.pack)
        count_bonus_list: int = len(bonus_list)

        for i in range(count_bonus_list):

            if Y[3] <= count_bonus_list/(count_bonus_list + 1):

                return bonus_list[i]
            
            
        return bonus_list[count_bonus_list - 1]
    
    # Why act on all bonusses in the list ?
    
    def player_act_on_bonus(self, bonus: list[Bonus]) -> None:
        
        for b in bonus:

            self.bonuses.append(b)

            if self.printing:

                print(f"\nActing on the {b} bonus")

            
            b.power(player=self)

        
    def player_choose_reroll(self) -> bool:
        
        # reroll_choice: bool = False

        # if self.reroll_count >= 1:

        #     reroll_choice = random.choice([True, False])

        #     if reroll_choice:

        #         self.set_reroll_count(self.reroll_count - 1)

        #         if self.printing:

        #             print(f"Reroll count: {self.reroll_count}, Bonuses are: {self.bonuses}")


        # return reroll_choice

        reroll_choice: bool = False

        if self.reroll_count >= 1:

            Y: list[float] = self.phenotype.propagate(self.adapter.pack)

            if Y[4] <= 0.2:

                reroll_choice = True

                self.set_reroll_count(self.reroll_count - 1)

                if self.printing:

                    print(f"Reroll count: {self.reroll_count}, Bonuses are: {self.bonuses}")


        return reroll_choice
            
    
    def player_choose_plusOne(self, dice: list[Dice]) -> Dice:

        # chosen_dice: Dice = None

        # if self.plusOne_count >= 1 and dice:

        #     chosen_dice = random.choice(dice)

        #     self.set_plusOne_count(self.plusOne_count - 1)

        #     if self.printing:

        #         print(f"plusOne count: {self.reroll_count}, player chose {chosen_dice.print_color_value()}")


        # return chosen_dice
    

        chosen_dice: Dice = None

        if self.plusOne_count >= 1 and dice:

            Y: list[float] = self.phenotype.propagate(self.adapter.pack)

            if Y[5] <= 0.2:

                chosen_dice = self.player_choose_dice(dice)
                dice.remove(chosen_dice)

                self.set_plusOne_count(self.plusOne_count - 1)

                if self.printing:

                    print(f"plusOne count: {self.reroll_count}, player chose {chosen_dice.print_color_value()}")


        return chosen_dice

    
    
    def player_act_on_PlusOne(self, round: Round) -> None:

        usable_dice_plusOne: list[Dice] = round.get_all_dice()
        chosen_dice_plusOne = self.player_choose_plusOne(usable_dice_plusOne)

        if chosen_dice_plusOne:

            chosen_board_plusOne = self.choose_board(self.boards, chosen_dice_plusOne)
            chosen_space_plusOne = self.choose_space(chosen_board_plusOne, chosen_dice_plusOne, round)
            self.choose_space_actions(chosen_board_plusOne, chosen_space_plusOne, chosen_dice_plusOne)

            usable_dice_plusOne.remove(chosen_dice_plusOne)
            chosen_dice_plusOne = self.player_choose_plusOne(usable_dice_plusOne)


    def choose_board(self, boards: list[Board], chosen_dice: Dice) -> Board:
        
        if chosen_dice.get_color() == "White":

            return self.player_choose_board(boards)
        

        else:

            return chosen_dice.get_board(boards)
        
    
    def choose_space(self, board: Board, chosen_dice: Dice, round: Round) -> Space:

        chosen_space = None
        available_spaces = None

        if board.color == "Blue":

            available_spaces = board.available_spaces(round.white_dice.value + round.blue_dice.value)  

        else:

            available_spaces = board.available_spaces(chosen_dice.value)
        

        if available_spaces:

            chosen_space = self.player_choose_space(available_spaces)
            chosen_space.cross(chosen_dice.get_value())


        return chosen_space
    
    
    def choose_space_actions(self, chosen_board: Board, chosen_space: Space, chosen_dice: Dice) -> None:

        if chosen_space:

            bonus = chosen_board.check_bonus(chosen_space)
            chosen_board.cross_space(chosen_space, chosen_dice.value)

            if bonus:

                self.player_act_on_bonus(bonus)
    

    def action(self, round: Round, is_active: bool) -> Dice:

        if is_active:

            usable_dice = round.get_usable_dice()

        else:
            
            usable_dice = round.get_throw_away_dice()


        # player can only reroll if it is an active player in the round
        while self.player_choose_reroll() and is_active:

            round.roll_dice()

            if self.printing:
                
                print("Rerolling the following dice:")

                for d in usable_dice:

                    print(d.print_color_value())

        if self.printing:

            print("Usable dice for this turn are:")

            for d in usable_dice:

                print(d.print_color_value())


        if usable_dice:

            chosen_dice = self.player_choose_dice(usable_dice)
            if self.printing:

                print(f"\n{self.name} choose {chosen_dice.print_color_value()}")


            chosen_board = self.choose_board(self.boards, chosen_dice)

            chosen_space = self.choose_space(chosen_board, chosen_dice, round)
            self.choose_space_actions(chosen_board, chosen_space, chosen_dice)

            if self.printing:

                print(f"\nThe available spaces on the {chosen_board.print_color_value()} board is: {chosen_space}")


            self.player_act_on_PlusOne(round)

            return chosen_dice
        
        
        return None