from Order import Order
from Keyboard import Keyboard
from Mouse import Mouse
from Monitor import Monitor
from Computer import Computer


keyboard1 = Keyboard('USB', 'HP')
mouse1 = Mouse('USB', 'HP')
monitor1 = Monitor('HP', 15)
computer1 = Computer('HP', monitor1, keyboard1, mouse1)

keyboard2 = Keyboard('Bluetooth', 'Acer')
mouse2 = Mouse('Bluetooth', 'Acer')
monitor2 = Monitor('Acer', 27)
computer2 = Computer('Acer', monitor2, keyboard2, mouse2)

keyboard3 = Keyboard('Bluetooth', 'Gamer')
mouse3 = Mouse('Bluetooth', 'Gamer')
monitor3 = Monitor('Gamer', 34)
computer3 = Computer('Gamer', monitor3, keyboard3, mouse3)

order = Order([computer1, computer2])
order.add_computer(computer3)

print(order)
