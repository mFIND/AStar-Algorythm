class ListReader:
    # None signifies the lack of a value
    # You can make a variable private by starting it with __
    __file_name = None
    __list = None

    # The constructor is called to set up or initialize an object
    # self allows an object to refer to itself inside of the class
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__read_list_from_file()

    def __read_list_from_file(self):
        self.__list = list()
        with open(self.__file_name, "r") as temp_file:
            for line in temp_file:
                temp_list = [int(s) for s in line.replace('[', '').replace(']', '').split(',')]
                self.__list.append(self.__get_nested_list_from_list(temp_list))

    @staticmethod
    def __get_nested_list_from_list(ints_list):
        dimensions = int((len(ints_list) - 1) / 2)
        out_list = list()
        for i in range(2):
            temp_list = []
            for j in range(dimensions):
                temp_list.append(ints_list[dimensions * i + j])
            out_list.append(temp_list)
        out_list.append(ints_list[dimensions * 2])
        return out_list

    def get_list(self):
        return self.__list
