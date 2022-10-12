from tkinter import *
from graphics import *

def main():
   frame = GraphWin('Map', 300, 200)   # pop-up window
   frame.setCoords(0, 0, 299, 199)  # 300 by 200
   shape = Polygon([Point(50, 100), Point(100, 50), Point(150, 100)])   # Triangle
   shape.setFill("red")
   shape.setOutline("black")
   shape.draw(frame)
   
   mainloop()

main()