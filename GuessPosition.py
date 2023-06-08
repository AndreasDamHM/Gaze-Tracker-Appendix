from Training import create_polynomial
import numpy as np
import mouse

def guessPosition(params, dataHor, dataVer):

    phiX = np.zeros((len(dataHor), len(params[0,:])))
    phiY = np.zeros((len(dataVer), len(params[0,:])))

    for i in range(len(dataHor)):
        for j in range(len(params[0,:])):
            phiX[i,j] = create_polynomial(dataHor[i],j)
    for i in range(len(dataVer)):
        for j in range(len(params[1,:])):
            phiY[i,j] = create_polynomial(dataVer[i],j)
    #print(params[0,:].T)
    #print(phiX)
    #print(phiX @ (params[0,:]).T)
    xCoor = np.median(phiX @ (params[0,:]).T)
    yCoor = np.median(phiY @ (params[1,:]).T)

    #print("xcoor = " + str(xCoor))
    #print("ycoor = " + str(yCoor))

    mouse_x = (xCoor/31) * 1530
    mouse_y = (yCoor/20) * 860
    #print("mouseX = " + str(mouse_x))
    #print("mouseY = " + str(mouse_y))
    return mouse_x, mouse_y

def moveCursor(x_pos, y_pos):

    mouse.move(str(round(x_pos)), str(round(y_pos)), duration=0.2)
