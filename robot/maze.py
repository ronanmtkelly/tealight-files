from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while touch() != 'fruit':
  if left_side() == 'wall':
    if touch() != 'wall':
      move(1)
    else:
      turn(1)
  else:
    turn(-1)
    move(1)