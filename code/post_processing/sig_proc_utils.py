from scipy.signal import butter, lfilter
import numpy as np

# Frequency analysis functions

def butter_bandpass(lowcut, highcut, fs, order = 5):
    return butter(order, [lowcut, highcut], fs=fs, btype = 'band')

def butter_highpass(lowcut, fs, order = 5):
    return butter(order, lowcut, fs=fs, btype = 'high')

def butter_highpass_filter(data, lowcut, fs, order = 5):
    b, a = butter_highpass(lowcut, fs, order = order)
    y = lfilter(b, a, data)
    return y

def butter_bandpass_filter(data, lowcut, highcut, fs, order = 5):
    b, a = butter_bandpass(lowcut, highcut, fs, order = order)
    y = lfilter(b, a, data)
    return y

def calculate_breathing_frequency(dists, FRAMES_PER_SECOND):
    fs = FRAMES_PER_SECOND
    lowcut = 0.5
    highcut = 8

    y = butter_bandpass_filter(dists, lowcut, highcut, fs)
    tpCount = len(y)
    values = np.arange(int(tpCount/2))
    timePeriod = tpCount/fs
    frequencies = values/timePeriod

    fourier = abs(np.fft.fft(y)/len(y))
    fourier = list(fourier[range(int(len(y)/2))])
    
    frequency = frequencies[fourier.index(max(fourier))]
    return frequency