from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,20):
  move(i)
  turn(1)
  color(colors[i%3])