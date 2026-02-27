import networkx as nx

class PatientTemporalGraph:

    def build_graph(self, events):

        G = nx.DiGraph()

        for i, event in enumerate(events):
            G.add_node(i, data=event)

            if i > 0:
                G.add_edge(i-1, i)

        return G
