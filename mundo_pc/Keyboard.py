from InputDevice import InputDevice


class Keyboard(InputDevice):

    keyboard_counter = 0

    def __init__(self, type_input, brand):
        super().__init__(type_input, brand)
        Keyboard.keyboard_counter += 1
        self.__id_keyboard = Keyboard.keyboard_counter

    @property
    def id_keyboard(self):
        return self.__id_keyboard

    @id_keyboard.setter
    def id_keyboard(self, value):
        self.__id_keyboard = value

    def __str__(self):
        return f'Id: {self.id_keyboard}, Marca: {self.brand}, Tipo entrada: {self.type_input}'
