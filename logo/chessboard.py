from tealight.logo import (move,
                           turn, 
                           color)

colors = ["black", "white"]

for i in range(0,4):
  color("black")
  move(50)
  color("white")
  move(50)
