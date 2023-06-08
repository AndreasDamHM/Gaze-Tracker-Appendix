"""from BPF import bandPassFilterFreq, bandpassFilterTimeSetup, bandPassFilterTime
import numpy as np
import matplotlib.pyplot as plt

b,a = bandpassFilterTimeSetup(6,0.15,7)


x = np.linspace(0,50,5*6827)

y = np.sin(2*np.pi*x*0.12) + np.sin(2*np.pi*x*1) + np.sin(2*np.pi*x*12) + np.sin(2*np.pi*x*56) + np.sin(2*np.pi*x*250) + np.sin(2*np.pi*x*600)

plt.plot(x,y)

state = [np.zeros(6),np.zeros(3),np.zeros(2)]

y,_ = bandPassFilterTime(y, b, a, state)

#y = bandPassFilterFreq(y)
plt.plot(x,y)


y = np.sin(2*np.pi*x*1)
plt.plot(x,y)
plt.legend(('Noisy', 'Filtered','True'), loc='upper left')



plt.title('Test signal')
plt.savefig('Test signal')
plt.close()
"""
from GuessPosition import guessPosition
from SignalProcessing import reduceChannel, outliers2, SignalProcessingFreq
import numpy as np
from CalibrationGUI import calibrationGUI

def validation(params, filename1, filename2):
    dataHor, dataVer, targetsHor, targetsVer,_,_ = calibrationGUI(filename1, filename2)

    print(len(targetsVer))
    targetsHor = reduceChannel(targetsHor, 0.044)
    targetsVer = reduceChannel(targetsVer, 0.044)
    dataHor, dataVer, _= SignalProcessingFreq(dataHor,dataVer, 0.044)

    print(len(targetsHor))


    dataHor, targetsHor = outliers2(dataHor, targetsHor)
    dataVer, targetsVer = outliers2(dataVer, targetsVer)

    N = min( len(dataHor),len(dataVer) )
    print(N)
    print(len(targetsVer))
    dataHor = dataHor[0:N]
    dataVer = dataVer[0:N]
    targetsHor = targetsHor[0:N]
    targetsVer = targetsVer[0:N]

    N = N/10
    N = np.floor(N)
    N = round(N)

    guessedPositions = np.zeros((2,N))

    truePositions = np.zeros((2,N))
    print(N)
    print(np.shape(guessedPositions))
    for i in range(N):
        x_pos, y_pos = guessPosition(params,dataHor[i*10:(i+1)*10-1],dataVer[i*10:(i+1)*10-1])

        if x_pos <= 510:
            x_pos = 1
        elif 510 < x_pos < 1020:
            x_pos = 2
        else:
            x_pos = 3

        if np.median(targetsHor[i*10:(i+1)*10-1]) <= 10.66:
            true_x = 1
        elif 10.66 < np.median(targetsHor[i*10:(i+1)*10-1]) <= 10.66*2:
            true_x = 2
        else:
            true_x = 3
        print(y_pos)
        if y_pos <= 286.66:
            y_pos = 1
        elif 286.66 < y_pos <= 286.66*2:
            y_pos = 2
        else:
            y_pos = 3

        if np.median(targetsVer[i*10:(i+1)*10-1]) <= 6.66:
            true_y = 1
        elif 6.66 < np.median(targetsVer[i*10:(i+1)*10-1]) <= 6.66*2:
            true_y = 2
        else:
            true_y = 3

        guessedPositions[0,i] = x_pos
        guessedPositions[1,i]= y_pos

        truePositions[0,i] = true_x
        truePositions[1,i] = true_y

    print(guessedPositions)
    print(truePositions)
    hitRateSquare = np.zeros(9)
    hitRateRow = np.zeros(3)
    hitRateColumn = np.zeros(3)
    for i in range(3):
        for j in range(3):

            list = np.argwhere((truePositions[0,:] == i+1) & (truePositions[1,:] == j+1))
            list2 = np.zeros((2,len(list)))
            for k in range(len(list)):
                list2[0,k] = guessedPositions[0,list[k]]
                list2[1,k] = guessedPositions[1,list[k]]

            square = len(np.argwhere((list2[0,:] == i+1) & (list2[1, :] == j+1)))/len(list)
            row = len(np.argwhere((list2[1,:] == j+1)))/len(list)
            column = len(np.argwhere((list2[0,:] == i+1)))/len(list)
            hitRateSquare[i*3 + j] = square
            hitRateRow[j] += row/3
            hitRateColumn[i] += column/3
    return hitRateSquare, hitRateRow, hitRateColumn


"""A = [10.0,10.0,10.0,10.0,0.0,0.1,0.4]
B =[1,1,1,1,1,1,1]


outliers2(B,A)
print(np.where((A == 10.0)))"""



















