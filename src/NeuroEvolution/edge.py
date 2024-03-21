class Edge:

    def __init__(self, source: int, destination: int, weight: float, enabled: bool, innovation: int = 0) -> None: 

        self.source = source 
        self.destination = destination
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation 