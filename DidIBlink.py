import numpy as np
from SignalProcessing import SignalProcessingTime, SignalProcessingFreq, plotData

def blinkTraining(dataVer, dataHor):
    k = 90
    dataVer = dataVer[0]
    dataHor = dataHor[0]
    blinkingImage = np.zeros((1, 2*k))
    #states = [np.zeros(6), np.zeros(4), np.zeros(2)]
    _, _, blinkingData = SignalProcessingFreq(dataHor, dataVer, 0.222)
    plotData(blinkingData, 'Blink', 20)
    print(len(blinkingData))
    blinkingData = blinkingData[int(3.5*682): int(-1*682)]
    R = len(blinkingData) % 4
    print(R)

    blinkingData = blinkingData[0:len(blinkingData)-R]
    plotData(blinkingData, 'Blink1', 10)

    blinkingData = np.split(blinkingData,4)
    print(blinkingData)
    M = 0
    maxima = np.zeros(4)
    blinkingData1 = np.zeros((4, 2*k))
    for i in range(4):
        maxInd = np.argmax(blinkingData[i])
        #print("maxInd " + str(maxInd))

        if (maxInd >= k and maxInd <= 1650-k):
            blinkingData1[i,:] = blinkingData[i][maxInd - k : maxInd + k]
            blinkingData1[i,:] = blinkingData1[i,:] - min(blinkingData1[i,:])
            maxima[i] = max(blinkingData1[i,:])
            #print("blinkingdata1 " + str(blinkingData1))
    median = np.median(maxima)
    for i in range(4):
        if abs(median - max(blinkingData1[i,:]) < 1.5 * np.std(maxima)):
            blinkingImage = blinkingImage + blinkingData1[i,:]
            M += 1


    print('sample size: ' + str(M))
    blinkingImage = blinkingImage/M
    #print("blinkingImage" + str(blinkingImage*100))
    blinkingImage = blinkingImage[0]
    plotData(blinkingImage, 'Blink Image', 0.2)
    return blinkingImage




def didIBlinknotused(data, image):
    Blink = 0

    mu_image = np.mean(image)
    std_image = np.std(image)

    for i in range(round((len(data)-len(image))/10)):

        mu_data = np.mean(data[-(len(image)+10*i),-(1 + 10*i)])
        std_data = np.std(data[-(len(image)+10*i),-(1 + 10*i)])
        pBlink = (((image - mu_image).T @ (data - mu_data))/(std_image * std_data))/len(data)
        #print("mu image " + str(mu_image))
        #print('std image ' + str(std_image))
        #print('p blink ' + str(pBlink))
        if pBlink >= 0.8 :
            Blink = 1
            return Blink



def didIBlink(data,image):
    blink = 0

    corrmax = -1000

    for i in range(len(data)-len(image)+1):

        corr = (data[i:i+len(image)] @ image )/ (np.linalg.norm(data[i:i+len(image)]) * np.linalg.norm(image)) - np.absolute((np.linalg.norm(image)-np.linalg.norm(data[i:i+len(image)] - min(data[i:i+len(image)])))/np.linalg.norm(image))
        if corr >= corrmax:
            corrmax = corr

            if corrmax >= 0.65:

                blink = 1
                return blink
    print('blink correlation ' + str(corrmax))
    return blink


