from NeuroEvolution.vertex import Vertex
from NeuroEvolution.edge import Edge
from NeuroEvolution.genotype import Genotype
from NeuroEvolution.mutation import Mutation
from NeuroEvolution.phenotype import Phenotype

class Network:
    _instance = None

    @classmethod
    def get_instance(cls):

        if cls._instance is None:

            cls._instance = cls()

        return cls._instance
    
    
    def create_base_genotype(inputs: int, outputs: int) -> Genotype:

        network: Genotype = Genotype()

        for i in range(inputs):

            network.add_vertex(Vertex(i, Vertex.EType.INPUT))


        for i in range(inputs, inputs + outputs):

            network.add_vertex(Vertex(i, Vertex.EType.OUTPUT))


        network.add_edge(Edge(0,inputs, 0.0, True, 0))

        # Somehow b2studios does not add the edges to the network now
        # This code is commented  out, must be a reason for this, but I don't know what

    
    def register_base_markings(inputs: int, outputs: int) -> None:

        mutation_instance: Mutation = Mutation()

        for i in range(inputs):

            for j in range(outputs):

                input = i
                output = j

                info: Edge = Edge(input, output, 0.0, True)

                mutation_instance.register_marking(info)
                

    def __init__(self) -> None:
        pass


    def create_base_recurrent(self) -> Genotype:

        network: Genotype = Genotype()
        nodeNum: int = 0

        # I don't really understand why the for loop runs until 1, this means that it runs once, but why use a for loop ?
        for i in range(1):

            network.add_vertex(Vertex(nodeNum, Vertex.EType.INPUT))
            nodeNum += 1


        for i in range(1):

            network.add_vertex(Vertex(nodeNum, Vertex.EType.OUTPUT))
            nodeNum += 1

        
        network.add_edge(Edge(0, 1, 0.0, True, 0))
        network.add_edge(Edge(1, 0, 0.0, True, 1))

        physical: Phenotype = Phenotype
        physical.inscribe_genotype(network)
        physical.process_graph()

        return network
    

    def class_buggy_network(self) -> Genotype:

        network: Genotype = Genotype()
        nodeNum: int = 0

        for i in range(2):

            network.add_vertex(Vertex(nodeNum, Vertex.EType.INPUT))
            nodeNum += 1


        for i in range(1):

            network.add_vertex(Vertex(nodeNum, Vertex.EType.OUTPUT))
            nodeNum += 1


        for i in range(2):

            network.add_vertex(Vertex(nodeNum, Vertex.EType.HIDDEN))
            nodeNum += 1


        network.add_edge(Edge(0, 2, 0.0, True, 0))
        network.add_edge(Edge(1, 2, 0.0, True, 1))
        network.add_edge(Edge(1, 3, 0.0, True, 2))
        network.add_edge(Edge(3, 2, 0.0, True, 3))

        physical: Phenotype = Phenotype()
        physical.inscribe_genotype(network)
        physical.process_graph()

        return network
    




    
