from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while touch() != 'fruit':
  if touch() == 'wall':
    if left_side() == 'wall':
      turn(1)
    else:
      if right_side() == 'wall':
        turn(-1)
      else:
        turn(1)
  else:
    move(1)