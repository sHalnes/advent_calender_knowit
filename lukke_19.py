from graphics import *

win = GraphWin('tiptop', 400, 400)
win.setCoords(0,0,35,25)
x1 = 11
y1 = 1
start_point = Point(x1,y1)

filename = 'lukke_19.txt'

with open(filename, 'r') as file:
    data = file.read().split('\n')
    for line in data:
        num, direction = line.split(', ')
        x2 = x1
        y2 = y1
        if direction =='west':
            x2 = x1 - int(num)

        elif direction == 'east':
            x2 = x1 + int(num)

        elif direction == 'south':
            y2 = y1 - int(num)

        elif direction == 'north':
            y2 = y1 + int(num)

        point2 = Point(x2, y2)
        line = Line(start_point, point2)
        line.draw(win)
        start_point = point2
        x1, y1 = x2, y2

win.getMouse()
win.close()