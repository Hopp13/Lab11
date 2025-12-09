import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.dao = DAO()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """

        connections_list = self.dao.read_connections(year)
        for connection in connections_list:
            print(connection, type(connection))
            node1 = self.dao.read_node(connection.id_rifugio1)
            node2 = self.dao.read_node(connection.id_rifugio2)
            print(type(node1), node1)
            print(type(node2), node2)
            self.G.add_node(node1)
            self.G.add_node(node2)
            self.G.add_edge(node1, node2, year = year)

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """

        return list(self.G.nodes)

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """

        neighbors_list = self.G.neighbors(node)
        counter = 0
        for neighbor in neighbors_list:
            counter += 1
            neighbor.pop()

        return counter

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """

        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.
        """

        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        c = self.get_reachable_recursive(start)

        return a

    def get_reachable_bfs_tree(start):
        T = NX.bfs_tree(self.G, start)
        return list(T.nodes)

    def get_reachable_iterative(start):
        visitati = []
        da_visitare = start
        for nodo in da_visitare:
            visitati.append(nodo)
            nuovi = self.G.neighbors(nodo)
            for nuovo_nodo in nuovi:
                if not nuovo_nodo in visitati:
                    da_visitare.append(nuovo_nodo)
        return visitati

