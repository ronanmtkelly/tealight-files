from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,1):
  move(i)
  turn(1)
  color(colors[i%3])