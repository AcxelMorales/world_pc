class Computer:

    counter_computers = 0

    def __init__(self, name, monitor, keyboard, mouse):
        self.__name = name
        self.__monitor = monitor
        self.__keyboard = keyboard
        self.__mouse = mouse
        Computer.counter_computers += 1
        self.__id_computer = Computer.counter_computers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self.__keyboard = keyboard

    @property
    def mouse(self):
        return self.__mouse

    @mouse.setter
    def mouse(self, mouse):
        self.__mouse = mouse

    def __str__(self):
        return f'''
        {self.__name}: {self.__id_computer}
        Monitor: {self.monitor}
        Teclado: {self.keyboard}
        Raton: {self.mouse}
        '''
