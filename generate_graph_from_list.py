from vertex import *


class ListToGraphGenerator:
    __list = None
    __x_dim = None
    __y_dim = None
    __ver_dict = None

    def __init__(self, init_list):
        self.__list = init_list
        self.__y_dim = len(init_list)
        self.__x_dim = len(init_list[0])
        self.__ver_dict = {}

    def get_start_and_finish_coordinates(self):
        return self.__list[0][0], self.__list[self.__y_dim - 1][1]

    def create_graph(self):
        for edge in self.__list:
            ver = []
            for i in range(2):
                if str(edge[i]) in self.__ver_dict:
                    ver.append(self.__ver_dict[str(edge[i])])
                else:
                    ver.append(Vertex(edge[i]))
                    self.__ver_dict.update({str(edge[i]): ver[len(ver) - 1]})
            ver[0].add_new_neighbours(ver[1], edge[2])
            ver[1].add_new_neighbours(ver[0], edge[2])
        return self.__ver_dict[str(self.__list[0][0])], self.__ver_dict[str(self.__list[len(self.__list) - 1][1])]


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
