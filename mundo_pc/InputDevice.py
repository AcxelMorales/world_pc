class InputDevice:
    def __init__(self, type_input, brand):
        self.__type_input = type_input
        self.__brand = brand

    @property
    def type_input(self):
        return self.__type_input

    @property
    def brand(self):
        return self.__brand

    @type_input.setter
    def type_input(self, value):
        self.__type_input = value

    @brand.setter
    def brand(self, value):
        self.__brand = value
