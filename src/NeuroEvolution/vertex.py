from NeuroEvolution.edge import Edge

class Vertex:

    class EType:
        INPUT = 0
        HIDDEN = 1
        OUTPUT = 2

    def __init__(self, index: int, type: EType) -> None:
        self.index = index
        self.type = type

        self.incoming: list[Edge] = []
        self.value = 0 


