import mouse
import keyboard
import time
import random


a = input("Coordinate x: ")
c = input("testo: ")
b = input("Coordinate y: ")
mouse.move(str(b), str(c))
mouse.press(button='left')
array = [0.1, 0.2]
for i in list(a):
    keyboard.write(i)
    time.sleep(array[random.randint(0, 1)])

