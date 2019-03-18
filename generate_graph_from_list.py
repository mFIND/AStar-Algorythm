from vertex import *

class GraphGenerator:
    __list = None
    __x_dim = None
    __y_dim = None
    __vertex_dict = None

    def __init__(self, list):
        self.__list = list
        self.__y_dim = len(list)
        self.__x_dim = len(list[0])
        self.__vertex_dict = {}

    def create_graph(self):
        for edge in self.__list:
            ver = []
            for i in range(2):
                if str(edge[0]) in self.__vertex_dict:
                    ver.append(self.__vertex_dict[str(edge[0])])
                else:
                    ver.append(Vertex(edge[0]))
                    self.__vertex_dict.update({str(edge[0]): ver[len(ver)-1]})
            ver[0].add_new_neighbours(ver[1], edge[2])
            ver[1].add_new_neighbours(ver[0], edge[2])
        return self.__list[0][0], self.__list[self.__y_dim - 1][1]


"""
    @David, tutaj mam pomysł na to, jak graf generować:
    
    zapisujemy pkt startowy i początkowy:
    self.__list[0][0], self.__list[self.__y_dim - 1][1]
    
    tworzymy mapę(C++)/dictionary(Python), w którym słowo klucz to
    współrzędne danego pkt (np. [0,0,0], ewentualnie str([0,0,0])),
    a wartością element (domyślnie przechowywany jako wskaźnik o ile się nie mylę)
    
    dzięki czemu będzie można łatwo prze-iterować przez całą listę,
    i dodać wszystkie zależności między wierzchołkami grafu

    Przy iterowaniu:
    -> albo pkt o zadanym kluczu istnieje, albo nie, i go tworzymy
    -> x2, bo 2 pkty na element listy
    -> w danym elemencie tworzymy powiązanie do elementu sąsiedniego
"""
