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
                line.replace('[]', '').split(',')
                self.__list.append(list(eval(line)))

    def get_list(self):
        return self.__list
