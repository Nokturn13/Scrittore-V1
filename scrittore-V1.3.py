import mouse
import keyboard
import time
import random


a = input("Coordinate x: ")
b = input("Coordinate y: ")
c = input("testo: ")
d =  input("Timer Y/n: ")
if d == "Y":
    e = input("Timer in secondi: ")
    time.sleep(float(e))
else:
    pass

mouse.move(str(a), str(b))
mouse.press(button='left')
array = [0.1, 0.2]
for i in list(c):
    keyboard.write(i)
    time.sleep(array[random.randint(0, 1)])

