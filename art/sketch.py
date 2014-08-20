from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0



def handle_mousemove(x,y,button):
  
  if button == "left":
    color("blue")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  elif button == "right":
    color("green")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  