from clever.dice import Dice

class Round:
    def __init__(self) -> None:
        self.white_dice = Dice("White", 0)
        self.yellow_dice = Dice("Yellow", 0)
        self.blue_dice = Dice("Blue", 0)
        self.green_dice = Dice("Green", 0)
        self.orange_dice = Dice("Orange", 0)
        self.purple_dice = Dice("Purple", 0)

        self.all_dice = [self.white_dice, self.blue_dice, self.yellow_dice, self.green_dice, self.orange_dice, self.purple_dice]
        self.usable_dice = [self.white_dice, self.blue_dice, self.yellow_dice, self.green_dice, self.orange_dice, self.purple_dice]
        self.throw_away_dice = []
        self.chosen_dices = []

    def roll_dice(self) -> None:
        for dice in self.usable_dice:
            dice.roll()

    def choose_dice(self, chosen_dice: Dice, player_actions: int) -> None:
        if chosen_dice:
            if player_actions > 1:
                dice_to_remove = []
                self.chosen_dices.append(chosen_dice)

                for dice in self.usable_dice:
                    if chosen_dice.value > dice.value:
                        dice_to_remove.append(dice)

                for dice in dice_to_remove:
                    self.throw_away_dice.append(dice)
                    self.usable_dice.remove(dice)
                
                self.usable_dice.remove(chosen_dice)

            else:
                self.chosen_dices.append(chosen_dice)
                self.usable_dice.remove(chosen_dice)
                for d in self.usable_dice:
                    self.throw_away_dice.append(d)
                    self.usable_dice.remove(d)
    
    def get_dice(self) -> list[Dice]:
        return self.usable_dice
