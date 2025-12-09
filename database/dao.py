from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.rifugio import Rifugio


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
    """

    @staticmethod
    def read_connections(year):
        connessione = DBConnect.get_connection()
        with connessione.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM connessione WHERE anno <= %s"
            cursor.execute(query, (year, ))
            connections_list = []
            for row in cursor:
                sentiero = Connessione(row["id"],
                                        row["id_rifugio1"],
                                        row["id_rifugio2"],
                                        row["distanza"],
                                        row["difficolta"],
                                        row["durata"],
                                        row["anno"])
                connections_list.append(sentiero)
        connessione.close()
        return connections_list

    @staticmethod
    def read_node(id_rifugio):
        connessione = DBConnect.get_connection()
        with connessione.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM rifugio WHERE id = %s"
            cursor.execute(query, (id_rifugio, ))
            for row in cursor:
                rifugio = Rifugio(row["id"],
                                  row["nome"],
                                  row["localita"],
                                  row["altitudine"],
                                  row["capienza"],
                                  row["aperto"])
        connessione.close()

        return rifugio
