from config import Config

class Bonus:
    
    def __init__(self, name: str) -> None:

        self.name = name
        self.printing = Config.printing
        pass

    
    def get_name(self) -> str:

        return self.name
    
    