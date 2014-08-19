from tealight.logo import move, turn

def spiral(size):
  
  if size > 300:
    return
  
  move(size)
  turn(20)
  spiral(size + 2)
  
spiral(0)