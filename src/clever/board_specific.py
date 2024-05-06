import numpy as np

from clever.space import Space
from clever.board import Board
from clever.bonus_specific import *

class YellowBoard(Board):

    def __init__(self) -> None:
        super().__init__('Yellow', [Space(False, 3, 0, 0), Space(False, 6, 0, 1), Space(False, 5, 0, 2), Space(True, 0, 0, 3),
                                    Space(False, 2, 0, 4), Space(False, 1, 0, 5), Space(True, 0, 0, 6), Space(False, 5, 0, 7),
                                    Space(False, 1, 0, 8), Space(True, 0, 0, 9), Space(False, 2, 0, 10), Space(False, 4, 0, 11),
                                    Space(True, 0, 0, 12), Space(False, 3, 0, 13), Space(False, 4, 0, 14), Space(False, 6, 0, 15)])
        

    def is_crossable(self, space: Space, dice_value: int) -> bool:
        
        return (dice_value == 100  or space.value == dice_value) and not space.crossed

    def check_bonus(self, space: Space)  -> list[Bonus]:

        bonus_set = [BlueX(), OrangeX(4), GreenX(), Fox(), PlusOne()]
        bonus = []
        
        row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
        if row_completed:
            bonus.append(bonus_set[int(np.floor(space.index/4))])

        if space.index in [0,5,10,15]:
            diagonal_completed = all(self.all_spaces[4*j + j].crossed for j in range(4))
            if diagonal_completed:
                bonus.append(bonus_set[4])
        
        return bonus
    
  
    def get_score(self) -> int:

        score = 0
        for i in range(4):
            multiplier = 1
            for j in range(4):
                if not self.all_spaces[4*j + i].crossed:
                    multiplier = 0
            if i <= 1:
                score += multiplier*(10 + 4*i)
            elif i <= 3:
                score += multiplier*(8 + 4*i)
        return score


class BlueBoard(Board):

    def __init__(self):

        super().__init__('Blue', [Space(True, 0, 0, 0), Space(False, 2, 0, 1), Space(False, 3, 0, 2), Space(False, 4, 0, 3),
                                   Space(False, 5, 0, 4), Space(False, 6, 0, 5), Space(False, 7, 0, 6), Space(False, 8, 0, 7),
                                   Space(False, 9, 0, 8), Space(False, 10, 0, 9), Space(False, 11, 0, 10), Space(False, 12, 0, 11)])
        
        
    def is_crossable(self, space: Space, dice_value: int) -> bool:

        return (dice_value == 100 or space.value == dice_value) and not space.crossed
    

    def get_score(self) -> int:

        score = 0
        count = 1
        for space in self.all_spaces:
            if space.crossed and not space.value == 0:
                if score == 0:
                    score = 1
                else:
                    score += count
                    count += 1
        return score
    
    
    def check_bonus(self, space: Space) -> list[Bonus]:

        bonus_set = [OrangeX(5), YellowX(), Fox(), Reroll(), GreenX(), PurpleX(6), PlusOne()]
        bonus = []
        
        row_completed = all(self.all_spaces[int(4*np.floor(space.index/4)) + j].crossed for j in range(4))
        if row_completed:
            bonus.append(bonus_set[int(np.floor(space.index/4))])

        column_completed = all(self.all_spaces[(space.index % 4) + 4*j].crossed for j in range(3))
        if column_completed:
            bonus.append(bonus_set[3 + (space.index % 4)])
        
        return bonus


class GreenBoard(Board):

    def __init__(self) -> None:
        
        super().__init__('Green', [Space(False, (i%5)+1, 0, i) for i in range(11)])
        self.all_spaces[10].value = 6
    
    def is_crossable(self, space: Space, dice_value: int) -> bool:

        if not self.all_spaces[0].crossed:
            return space.index == 0
        else:
            for i in range(1, 11):
                if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                    if dice_value > self.all_spaces[i].value: 
                        return space.value == i
        return False
    
            
    def get_score(self) -> int:

        score = 0
        for space in self.all_spaces:
            if not space.crossed:
                break
            else:
                score += space.value
        return score
    

    def check_bonus(self, space: Space) -> list[Bonus]:

        bonus_set = [PlusOne(), BlueX(), Fox(), PurpleX(6), Reroll()]
        bonus = []
        
        i = space.index
        if i == 3:
            bonus.append(bonus_set[0])
        elif i == 5:
            bonus.append(bonus_set[1])
        elif i == 6:
            bonus.append(bonus_set[2])
        elif i == 8:
            bonus.append(bonus_set[3])
        elif i == 9:
            bonus.append(bonus_set[4])
        
        return bonus


class OrangeBoard(Board):

    def __init__(self) -> None:

        super().__init__('Orange', [Space(False, i, 0, i) for i in range(11)])


    def is_crossable(self, space: Space, dice_value: int) -> bool:

        if not self.all_spaces[0].crossed:
            return space.value == 0
        else:
            for i in range(1, 11):
                if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                    return space.value == i
        return False
    

    def cross_space(self, space: Space, dice_value: int) -> None:

        if not space.crossed:

            if space == self.all_spaces[3] or space == self.all_spaces[6] or space == self.all_spaces[8]:

                space.cross(2 * dice_value)

            elif space == self.all_spaces[10]:

                space.cross(3 * dice_value)

            else:

                space.cross(dice_value)

        
        if self.printing:

            print(f"\nUpdated state of the {self.color} Board:")
            for space in self.all_spaces:

                if space.crossed:

                    print(f"\033[92m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")

                else:

                    print(f"\033[0m Space {space.index}: Crossed: {space.crossed}, Value: {space.value}, Dice Value: {space.dice_value}")


    def get_score(self) -> int:

        score = 0
        for space in self.all_spaces:
            if space.crossed:
                score += space.dice_value
        return score
    
    
    def check_bonus(self, space: Space) -> list[Bonus]:

        bonus_set = [Reroll(), YellowX(), PlusOne(), Fox(), PurpleX(6)]
        bonus = []
        
        i = space.value
        if i == 2:
            bonus.append(bonus_set[0])
        elif i == 4:
            bonus.append(bonus_set[1])
        elif i == 5:
            bonus.append(bonus_set[2])
        elif i == 7:
            bonus.append(bonus_set[3])
        elif i == 9:
            bonus.append(bonus_set[4])
        
        return bonus

class PurpleBoard(Board):
    def __init__(self) -> None:

        super().__init__('Purple', [Space(False, i, 0, i) for i in range(11)])


    def is_crossable(self, space: Space, dice_value: int) -> bool:

        if not self.all_spaces[0].crossed:
            return space.index == 0
        else:
            for i in range(1, 11):
                if not self.all_spaces[i].crossed and self.all_spaces[i - 1].crossed:
                    if dice_value > self.all_spaces[i-1].dice_value or self.all_spaces[i-1].dice_value == 6:
                        return space.index == i
        return False
    

    def get_score(self) -> int:

        score = 0
        for space in self.all_spaces:
            if space.crossed:
                score += space.dice_value
        return score
    
    
    def check_bonus(self, space: Space) -> list[Bonus]:

        bonus_set = [Reroll(), BlueX(), PlusOne(), YellowX(), Fox(), Reroll(), GreenX(), OrangeX(6), PlusOne()]
        bonus = []
        
        if(space.index >= 2):
            bonus.append(bonus_set[space.index-2])
        
        return bonus
