class Monitor:

    counter_monitors = 0

    def __init__(self, brand, size):
        Monitor.counter_monitors += 1
        self.__id_monitor = Monitor.counter_monitors
        self.__brand = brand
        self.__size = size

    @property
    def id_monitor(self):
        return self.__id_monitor

    @property
    def brand(self):
        return self.__brand

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @id_monitor.setter
    def id_monitor(self, _id_monitor):
        self.__id_monitor = _id_monitor

    def __str__(self):
        return f'Id: {self.__id_monitor}, Brand: {self.__brand}, Size: {self.__size}'

