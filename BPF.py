import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def bandPassFilterFreq(data: np.ndarray, lowerBandLimit: int = 0.15, upperBandLimit: int = 7,
                       sampling_rate: int = 682.67, ) -> np.ndarray:
    upperBandLimit_index = int(upperBandLimit * data.size / sampling_rate)
    lowerBandLimit_index = int(lowerBandLimit * data.size / sampling_rate)

    fSig = np.fft.fft(data, n=len(data))

    for i in range(upperBandLimit_index + 1, len(fSig)):
        fSig[i] = 0
    for i in range(0, lowerBandLimit_index):
        fSig[i] = 0

    """

    b,a = signal.butter(order,10, 'lowpass', fs=sampling_rate)

    data_filtered = signal.lfilter(b,a,data)"""
    data_filtered = 2*np.fft.ifft(fSig, n=len(data))

    return np.real(data_filtered)


def bandpassFilterTimeSetup(order, cutOffFreqLow, cutOffFreqHigh):
    sampling_frequency = 682.67  # Sampling frequency in Hz
    nyq = 0.5 * sampling_frequency

    normal_cutoffLow = cutOffFreqLow / nyq
    normal_cutoffHigh = cutOffFreqHigh / nyq

    LPFPolyB, LPFPolyA = signal.butter(order, normal_cutoffHigh, 'low', analog=False)

    HPFPolyB, HPFPolyA = signal.butter(3, normal_cutoffLow, 'high', analog=False)

    #BNFPolyB, BNFPolyA = signal.iirnotch(0.05,0.8, sampling_frequency)

    w, hA = signal.freqz(LPFPolyB, LPFPolyA, fs=sampling_frequency, worN=np.logspace(-2, np.log10(300), 50000))
    w, hB = signal.freqz(HPFPolyB, HPFPolyA, fs=sampling_frequency, worN=np.logspace(-2, np.log10(300), 50000))
    #w, hC = signal.freqz(BNFPolyB, BNFPolyA, fs=sampling_frequency, worN=np.logspace(-2, np.log10(300), 50000))

    """
    hABC = hA*hB
    plt.semilogx(w, 20 * np.log10(abs(hABC)))
    plt.title('Butterworth IIR bandpass filter fit to constraints')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dB]')
    plt.grid(which='both', axis='both')
    plt.savefig('Frequency response')
    plt.show()
    plt.close()"""

    BPFPolyB = [LPFPolyB, HPFPolyB]
    BPFPolyA = [LPFPolyA, HPFPolyA]

    return BPFPolyB, BPFPolyA


def bandPassFilterTime(data: np.ndarray, b, a, state):
    #print(np.shape(state))
    #print(state[0])
    stateLow = np.array(state[0], dtype=np.float32)
    stateHigh = np.array(state[1], dtype=np.float32)
    #stateNotch = np.array(state[2], dtype=np.float32)

    dataFiltered, stateNewLow = signal.lfilter(b[0], a[0], data, zi=stateLow)

    dataFiltered, stateNewHigh = signal.lfilter(b[1], a[1], dataFiltered, zi=stateHigh)

    #dataFiltered, stateNewNotch = signal.lfilter(b[2], a[2], dataFiltered, zi=stateNotch)

    stateNew = [stateNewLow, stateNewHigh]#,stateNewNotch]

    return dataFiltered, stateNew

#test of filter
"""x = np.linspace(0, 20, 13640)

sigLow = np.sin(2 * np.pi * 0.05 * x)

sigBP = np.sin(2 * np.pi * 6 * x)

sigHigh = np.sin(2 * np.pi * 12 * x)

plt.plot(x, (sigLow + sigBP))
plt.title('Low frequency noise - no filter')
plt.savefig('Low freq noise')
plt.close()

plt.plot(x, (sigHigh + sigBP))
plt.title('High frequency noise - no filter')
plt.savefig('High freq noise')
plt.close()

b, a = bandpassFilterTimeSetup(6, 0.6, 8)
sig1,_ = bandPassFilterTime(sigLow + sigBP, b, a, [np.zeros(6), np.zeros(4), np.zeros(2)])

plt.plot(x, sig1)
plt.title('Low frequency noise - with filter')
plt.savefig('Low freq filter')
plt.close()

sig2,_ = bandPassFilterTime(sigHigh + sigBP, b, a, [np.zeros(6), np.zeros(4), np.zeros(2)])

plt.plot(x, sig2)
plt.title('High frequency noise - with filter')
plt.savefig('High freq filter')
plt.close()

sig3,_ = bandPassFilterTime(sigLow+sigBP+sigHigh, b ,a, [np.zeros(6), np.zeros(4), np.zeros(2)])

plt.plot(x, sig3)
plt.title('Full noise - with filter')
plt.savefig('both freq noise')
plt.close()

plt.plot(x, sigLow+sigBP+sigHigh )
plt.title('Full noise - no filter')
plt.savefig('both freq filter')
plt.close()
"""
