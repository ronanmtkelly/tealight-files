from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0


def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y


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
  