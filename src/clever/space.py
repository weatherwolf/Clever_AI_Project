class Space:

    def __init__(self, crossed: bool, value: int, dice_value: int, index: int) -> None:
        
        self.crossed = crossed
        self.value = value
        self.dice_value = dice_value
        self.index = index
        

    def cross(self, value: int = None):
       
        self.crossed = True
        if value is not None:
            self.dice_value = value
