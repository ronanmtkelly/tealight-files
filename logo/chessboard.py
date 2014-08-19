from tealight.logo import (move,
                           turn, 
                           color)

colors = ["black"]

for i in range(0,4):
  color("black")
  move(400)
  turn(90) 

for i in range(0,4):
  color("black")
  move(50)
  turn(90)
  move(400)
  turn(-90)
  move(50)
  turn(-90)
  move(400)
  turn(90)
  
for i in range(0,4):
  color("black")