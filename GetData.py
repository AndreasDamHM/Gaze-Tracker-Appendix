import csv
import numpy as np
import time
import matplotlib.pyplot as plt

"""
filename1 = "C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/CH1.csv"
file = open(filename1, 'r+')
csvreader = csv.reader(file, delimiter = ';')
ECG1 = ([])
for row in csvreader:
    ECG1.extend(row)
ECG1 = np.array(ECG1, dtype=np.float32)
print(len(ECG1))
file.truncate(0)
file.close()
#print(ECG1)
"""


ECG_CH1 = np.array([])
ECG_CH2 = np.array([])

def GetData(KEY):
    file = open(
        "C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/" + KEY + ".csv",
        'r+')
    csvreader = csv.reader(file, delimiter=';')
    Data = ([])
    for row in csvreader:
        Data.extend(row)
    Data = np.array(Data, dtype=np.float32)
    #print(np.shape(Data))
    if len(Data) == 0:
        n = 1
    if len(Data) != 0:
        n = 0

    file.truncate(0)
    file.close()
    Data = np.array(Data, dtype=np.float32)
    #print('New data read: ' + str(len(Data)))
    return Data, n


def targetCreation(name1, name2, pos1, pos2):

    dataHor,_ = GetData(name1)
    dataVer,_ = GetData(name2)

    N_hor = len(dataHor)
    N_ver = len(dataVer)


    targetHor = pos1 * np.ones(N_hor)
    targetVer = pos2 * np.ones(N_ver)

    targetHor = np.array(targetHor, dtype=np.float32)
    targetVer = np.array(targetVer, dtype=np.float32)


    return dataHor, dataVer, targetHor, targetVer

"""abort = 0
while True:
    time.sleep(0.05)
    Data, n = GetData('ECG_CH1')
    ECG_CH1 = np.append(ECG_CH1,Data)
    Data, n = GetData('ECG_CH2')
    if n == 0:
        abort = 0
    abort += n
    ECG_CH2 = np.append(ECG_CH2, Data)
    if abort >= 50:
        break




print(len(ECG_CH1))
print(len(ECG_CH2))

"""

