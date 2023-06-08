import mouse  #bottom right is 1530;860
import time
def moveCursor(x_pos, y_pos):

    mouse.move(str(round(x_pos)), str(round(y_pos)), duration=0.12)

