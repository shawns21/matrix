#!/usr/bin/python3

import curses
import random
import math

scr = curses.initscr()
curses.start_color()

rows, cols = scr.getmaxyx()
rows -= 1
cols = int(cols/3)

m = []

fib = [0,1]
a = []
"""
    n = fib[0] + fib[1]
    fib[0] = fib[1]
    fib[1] = n
    if n < cols:
        for z in range(n):
            a.append(random.randint(0,cols-1))
"""
for i in range(1000):
    s = ""

    for z in range(int(math.log(i+1))):
        a.append(random.randint(0,cols-1))
    
    for k in range(cols):
        if(k in a):
            s += chr(random.randint(192,255)) + "  "
        else:
            s += " " + "  "
    
    m.append(s)

    scr.erase()
    if(len(m)>rows):
        l = rows
    else:
        l = len(m) - 1

    for line in m[-rows:]:
        scr.addstr(l,0, line)
        l -= 1

    scr.refresh()
    curses.napms(200)


#scr.addch(rows, cols, "X")
#scr.refresh()
"""
s = "Testing addstr"
s += "\nAnd newline"
scr.addstr(0,0, s)

for i in range(100):
    scr.addch(7,7,i)
    scr.refresh()
    curses.napms(500)

curses.napms(2000)

curses.endwin()
"""
curses.napms(5000)
curses.endwin()
print(rows)