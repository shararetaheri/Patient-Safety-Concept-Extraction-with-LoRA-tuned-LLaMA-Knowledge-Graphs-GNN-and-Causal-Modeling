import networkx as nx

class OntologySimilarity:

    def semantic_distance(self, graph, concept1, concept2):
        try:
            return nx.shortest_path_length(graph,
                                           concept1,
                                           concept2)
        except:
            return None
