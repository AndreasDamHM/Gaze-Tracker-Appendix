
from GetData import GetData
import numpy as np
import matplotlib.pyplot as plt
from BPF import bandPassFilterTime, bandPassFilterFreq, bandpassFilterTimeSetup
import time
from Training import Calibrate, targetsGUI1

def reduceChannel(channel, T):

    N = 682.67 * T
    N = round(N)
    M = len(channel)/N
    M = np.floor(M)
    M = round(M)

    ChannelReduced = []

    for i in range(M):
        #print(channel[i*N:(i+1)*N])
        ChannelReduced.append(np.mean(channel[i*N:(i+1)*N],dtype=np.float32))
        #print(ChannelReduced[i])
    ChannelReduced.append(np.mean(channel[M*N:-1], dtype=np.float32))

    #print(ChannelReduced)
    #print(np.argmin(ChannelReduced))
    #print(np.argmax(ChannelReduced))

    return ChannelReduced

#calibrationGUI()
def plotData(data,name,axis1):
    data = np.array(data, dtype=np.float32)

    time = np.linspace(0, axis1, num=len(data))

    plt.plot(time, data)
    plt.title(name)
    plt.savefig(name)

    #plt.show()
    plt.close()

def SignalProcessingFreq(Data1,Data2,T):
    Channel1 = Data1
    Channel2 = Data2

    """Channel2 = Channel2[0:len(Channel1)]
    Channel1 = Channel1[0:len(Channel2)]
    

    Channel2 = Channel2 - Channel1 / 2"""
    Channel1 = bandPassFilterFreq(Channel1)
    Channel2 = bandPassFilterFreq(Channel2)

    if len(Channel1) <= len(Channel2):

        Channel1x = np.hstack((Channel1, np.zeros(len(Channel2) - len(Channel1))))

    else:
        Channel1x = Channel1[-1-len(Channel2):-1]

    Channel2 = Channel2 - Channel1x / 2

    Channel1Reduced = reduceChannel(Channel1, T)
    Channel2Reduced = reduceChannel(Channel2, T)

    #delete when filter works
    #plotData(Channel1Reduced[7:-7], 'Horizontal channel',22)
    #plotData(Channel2Reduced[7:-7], 'Channel 2 after adjustment',22)


    return Channel1Reduced, Channel2Reduced, Channel2


b, a = bandpassFilterTimeSetup(6, 0.15, 7)
#print((b[0]))
#print(np.shape(a))

def SignalProcessingTime(Data1, Data2,T, stateChannel1, stateChannel2, b = b ,a = a):
        Channel1 = Data1
        Channel2 = Data2

        #print(len(Channel1))
        #print(len(Channel2))
        # Channel2 = Channel2[round(- 20 * 682.67):]
        # Channel1 = Channel1[round(- 20 * 682.67):]
        # print(len(Channel2))
        # print(len(Channel1))


        Channel1, newStateChannel1 = bandPassFilterTime(Channel1, b, a, stateChannel1)
        Channel2, newStateChannel2 = bandPassFilterTime(Channel2, b, a, stateChannel2)

        if len(Channel1) <= len(Channel2):

            Channel1x = np.hstack((Channel1, np.zeros(len(Channel2)-len(Channel1))))

        else:
            Channel1x = Channel1[-1-len(Channel2):-1]

        Channel2 = Channel2 - Channel1x / 2



        Channel1 = np.array(Channel1, dtype=np.float32)
        Channel2 = np.array(Channel2, dtype=np.float32)

        Channel1Reduced = reduceChannel(Channel1, T)
        Channel2Reduced = reduceChannel(Channel2, T)

        # delete when filter works
        plotData(Channel1Reduced[30:-1], '2',20)
        plotData(Channel2Reduced[30:-1], '4',20)

        return Channel1Reduced, Channel2Reduced, Channel2, newStateChannel1, newStateChannel2



def removeOutliers(data, targets, n):
    left = 5.2
    right = 25.8
    midHor = 15.5
    top = 3.3
    bottom = 16.7
    midVer = 10.0

    print(np.shape(targets))
    targets = [round(target,1) for target in targets]
    targets = np.array(targets, dtype=np.float32)
    #remove faulty targets

    wrongTargets = np.argwhere((targets!=left)&(targets!=right)&(targets!=midHor)&(targets!=top)&(targets!=bottom)&(targets!=midVer))
    print('before: ' + str(len(data)))
    print(len(wrongTargets))
    #print(wrongTargets)
    data = np.delete(data, wrongTargets)
    print('after: ' + str(len(data)))
    targets = np.delete(targets, wrongTargets)

    """  #print(len(data))
    if n == 1:
        Calibrate(data, targets, 'Linear regression horizontal channel before removal of outliers',0)
    else:
        Calibrate(data, targets, 'Linear regression vertical channel before removal of outliers ',0)
    """
    #remove outliers

    positions = np.array([left,right,midHor,top,bottom,midVer])

    dataCleaned = np.array([])
    targetsCleaned = np.array([])

    #print(data)
    for i in range(len(positions)):

        indices = np.argwhere(targets == positions[i])

        dataPos = data[indices]

        targetPos = targets[indices]

        indicesToRemove = np.argwhere(np.abs(dataPos-np.median(dataPos)) > 1 * np.std(dataPos))

        print('number of outliers' + str(len(indicesToRemove)))
        dataPos = np.delete(dataPos, indicesToRemove)


        targetPos = np.delete(targetPos, indicesToRemove)

        dataCleaned = np.hstack((dataCleaned, dataPos))
        targetsCleaned = np.hstack((targetsCleaned, targetPos))

    #print(len(dataCleaned))


    return dataCleaned, targetsCleaned


def outliers2(data, targets):
    left = 5.2
    right = 25.8
    midHor = 15.5
    top = 3.3
    bottom = 16.7
    midVer = 10.0

    #print(np.shape(targets))
    targets = np.array(targets, dtype=np.float32)
    # remove faulty targets


    targets = [round(target,1) for target in targets]
    targets = np.array(targets, dtype=np.float32)
    #print(targets)



    wrongTargets = np.argwhere((targets != left) & (targets != right) & (targets != midHor) & (targets != top) &
                               (targets != bottom) & (targets != midVer))
    print('before: ' + str(len(data)))
    print(len(wrongTargets))
    #print(wrongTargets)
    data = np.delete(data, wrongTargets)
    print('after: ' + str(len(data)))
    targets = np.delete(targets, wrongTargets)
    return data, targets







A = np.array([100, 0.02,1,3,1,6,3,5,2,5,53,313,2,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
B = np.array([5.16,25.83,15.5,15.7,5.16,34,12,34,15.5,12,3.333,16.666,10, 5.16,5.16,5.16,5.16,5.16,5.16,5.16,5.16,23,2.3,2.3,2.3,2.3,2.3,5.16,5.09999,3.333,3.333,3.333])

removeOutliers(A,B,0)

"""
filename1 = 'ECG_CH1Vert'
filename2 = 'ECG_CH2Vert'
state = [np.zeros(6), np.zeros(2), np.zeros(2)]


print(state)

datax,_ = GetData(filename1)
datay,_ = GetData(filename2)

SignalProcessingTime(datax, datay, 0.222,state,state)
SignalProcessingFreq(datax, datay, 0.222)"""

"""

time.sleep(5)

state= [np.zeros(6),np.zeros(6)]

dataHor, dataVer = SignalProcessingTime('ECG_CH1Vert','ECG_CH2Vert', 0.222, state, state )

targetsHor, targetsVer = targetsGUI1()

xWeights = Calibrate(dataHor,targetsHor)
yWeights = Calibrate(dataVer,targetsVer)
print(min(dataHor),max(dataHor))


print(xWeights)
print(yWeights)"""