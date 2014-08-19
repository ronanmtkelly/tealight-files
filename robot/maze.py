from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while touch() != 'fruit':
  if touch() != 'wall':
    move(1)
  else:
    if left_side() == 'wall':
      turn(1)
      if right_side == 'wall':
        turn(2)
    else:
      turn(-1)
      move()
      
move(1)