#!/usr/bin/python3

import os
import time
import random

os.system("clear")

green = "\u001b[32m"
white = "\u001b[37m"
black = "\u001b[30m"

colorArray = []
for _ in range(16):
    colorArray.append(green)

for _ in range(3):
    colorArray.append(white)

for _ in range(1):
    colorArray.append(black)

for _ in range(1000):
    s = ""
    for _ in range(50):
        c = colorArray[random.randint(0,19)]
        s += c+chr(random.randint(192,255)) + "  "

    print(s)
    time.sleep(.1)