from InputDevice import InputDevice


class Mouse(InputDevice):

    mouse_counter = 0

    def __init__(self, type_input, brand):
        super().__init__(type_input, brand)
        Mouse.mouse_counter += 1
        self.__id_mouse = Mouse.mouse_counter

    @property
    def id_mouse(self):
        return self.__id_mouse

    @id_mouse.setter
    def id_mouse(self, value):
        self.__id_mouse = value

    def __str__(self):
        return f'Id: {self.id_mouse}, Marca: {self.brand}, Tipo entrada: {self.type_input}'
