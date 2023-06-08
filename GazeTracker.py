import time
import threading
from CalibrationGUI import calibrationGUI
from SignalProcessing import SignalProcessingTime, plotData, removeOutliers, SignalProcessingFreq, reduceChannel
from Training import Calibrate
from GuessPosition import guessPosition
from CursorControl import moveCursor
import mouse
from GetData import GetData
from Training import Calibrate, targetsGUI1
import numpy as np
from DidIBlink import blinkTraining, didIBlink

def Setup(filename1, filename2, initialState):

    # Calibration


    time.sleep(3)
    bufferData1,_ = GetData(filename1)
    bufferData2,_ = GetData(filename2)
    _,_,_,stateChannel1, stateChannel2 = SignalProcessingTime(bufferData1,bufferData2, 0.222,initialState,initialState)

    dataHor, dataVer, targetsHor, targetsVer, blinkingDataVer, blinkingDataHor = calibrationGUI(filename1, filename2)
    DataHorT, DataVerT, _,_,_ = SignalProcessingTime(dataHor, dataVer, 0.222, stateChannel1, stateChannel2)
    DataHor, DataVer,_ = SignalProcessingFreq(dataHor, dataVer, 0.222)
    targetsHor = reduceChannel(targetsHor,0.222)
    targetsVer = reduceChannel(targetsVer,0.222)
    plotData(DataHor, 'Horizontal channel signal filtered in frequency domain',22)
    plotData(DataVer, 'Vertical channel signal filtered in frequency domain',22)
    plotData(DataHorT, 'Horizontal channel signal filtered in time domain', 22)
    plotData(DataVerT, 'Vertical channel signal filtered in time domain', 22)
    print(len(DataHor)-len(targetsHor))
    print(len(DataVer) - len(targetsVer))


    DataHor, targetsHor = removeOutliers(DataHor, targetsHor, 1)
    xWeights = Calibrate(DataHor, targetsHor, 'Linear regression horizontal channel after removal of outliers ', 1)
    DataVer, targetsVer = removeOutliers(DataVer, targetsVer, 0)

    #Calibrate(DataHorT, targetsHor, 'regHorT')
    #Calibrate(DataVerT, targetsVer, 'regVerT')

    yWeights = Calibrate(DataVer,targetsVer, 'Linear regression vertical channel after removal of outliers ',1)

    blinkingImage = blinkTraining(blinkingDataVer, blinkingDataHor)
    params = np.vstack((xWeights, yWeights))
    print(np.shape(params))
    return DataHor, DataVer, blinkingImage, params

# Main Loop
#UserGUI()



#thread 2
def GazeLoop(dataHor, dataVer, blinkingImage, params,filename1, filename2):
    fail = 0

    DataX = dataHor
    DataY = dataVer

    time.sleep(0.3)
    nowTime = time.time()
    D = 0
    fail = 0

    blinkTime = -2
    blinkCount = 0
    while True:
        D += 1
        time.sleep(0.03)
        print("time = " + str(D))
        data1,_ = GetData(filename1)
        data2,_ = GetData(filename2)
        DataX = np.append(DataX, data1)
        DataY = np.append(DataY, data2)

        DataX = DataX[-round(682.67*10):-1]
        DataY = DataY[-round(682.67*10):-1]


        if len(data1) == 0 or len(data2) == 0:
            fail += 1
        else:
            fail = 0
            DataHor, DataVer, blinkingData = SignalProcessingFreq(DataX, DataY, 0.04444)
            Blink = didIBlink(blinkingData[-682:-1], blinkingImage)
            #plotData(blinkingData[-1364:-1], str(D), 2)
            if Blink == 1 and time.time() - blinkTime >= 1:
                blinkTime = time.time()
                mouse.click('left')
                print('Blink')
                blinkCount += 1
            x_pos, y_pos = guessPosition(params, DataHor[-13:-3], DataVer[-13:-3])
            moveCursor(x_pos, y_pos)
        #print(fail)
        if fail == 1000:
            break
        if D >= 1000:
            print("number of blinks captured " + str(blinkCount))
            break



