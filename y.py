import random 
import time
import os

x = ['a','b','c','d','e','f','A','B','C','D','E','F','!','@','#','$','%','^','&','*','(',')','+','=',':',';','"',0,1,2,3,4,5,6,7,8,9,'<','>','?','/','|']

height, width = os.popen('stty size','r').read().split()

line_width = int(width)

color = ["\033[01;32m", "\033[01;32m", "\033[01;32m", "\033[00;30m", "\033[00;30m", "\033[0;37m"]


while True:
    for i in range(line_width):
        print( random.choice(color), random.choice(x), end=' ', sep=' ') 
    print()
    time.sleep(0.15)

