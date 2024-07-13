class Order:

    counter_orders = 0

    def __init__(self, computers):
        Order.counter_orders += 1
        self.__id_order = Order.counter_orders
        self.__computers = list(computers)

    @property
    def computers(self):
        return self.__computers

    @computers.setter
    def computers(self, computers):
        self.__computers = list(computers)

    @property
    def id_order(self):
        return self.__id_order

    @id_order.setter
    def id_order(self, id_order):
        self.__id_order = id_order

    def add_computer(self, computer):
        self.__computers.append(computer)

    def __str__(self):
        computers_str = ''

        for computer in self.computers:
            computers_str += computer.__str__()

        return f'''
            Orden: {self.id_order}
            Computadoras: {computers_str}
        '''
