# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:29:27 2021

@author: User
"""



from scipy import signal
import numpy as np
import pyaudio

    

rate = 8192
fs = rate      # Sample rate, Hz
fr1 = 697       # Frequency of firt row
fr2 = 770       # Frequency of second row
fr3 = 852       # Frequency of third row
fr4 = 941       # Frequency of fourth row   
fc1 = 1209      # Frequency of firt column
fc2 = 1336      # Frequency of second column
fc3 = 1477      # Frequency of third column
fc4 = 1633      # Frequency of fourth column

band = [fr1 - 30, fr1 + 30]  # Desired pass band for filter1, Hz
trans_width = 6    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f1 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)


band = [fr2 - 30, fr2 + 30]  # Desired pass band for filter2, Hz
trans_width = 6    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f2 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
    


band = [fr3 - 40, fr3 + 40]  # Desired pass band for filter3, Hz
trans_width = 8    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f3 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
   


band = [fr4 - 40, fr4 + 40]  # Desired pass band for filter4, Hz
trans_width = 8    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f4 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)



band = [fc1 - 50, fc1 + 50]  # Desired pass band for filter5, Hz
trans_width = 10    # Width of transition from pass band to stop band, Hz
numtaps = 1500        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f5 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)



band = [fc2 - 55, fc2 + 55]  # Desired pass band for filter6, Hz
trans_width = 11    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f6 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
    


band = [fc3 - 65, fc3 + 65]  # Desired pass band for filter7, Hz
trans_width = 13    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f7 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)



band = [fc4 - 75, fc4 + 75]  # Desired pass band for filter8, Hz
trans_width = 15    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f8 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)



cutoff = 200    # Desired cutoff frequency, Hz
trans_width = 300  # Width of transition from pass band to stop band, Hz
numtaps = 100      # Size of the FIR filter.
energyfilt= signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0], Hz=fs)


def energy(x):
    y1 = signal.lfilter(f1, [1.0], x)
    y2 = signal.lfilter(f2, [1.0], x)
    y3 = signal.lfilter(f3, [1.0], x)
    y4 = signal.lfilter(f4, [1.0], x)
    y5 = signal.lfilter(f5, [1.0], x)
    y6 = signal.lfilter(f6, [1.0], x)
    y7 = signal.lfilter(f7, [1.0], x)
    y8 = signal.lfilter(f8, [1.0], x)
    
    out1 = signal.lfilter(energyfilt, [1.0], y1*y1)
    out2 = signal.lfilter(energyfilt, [1.0], y2*y2)
    out3 = signal.lfilter(energyfilt, [1.0], y3*y3)
    out4 = signal.lfilter(energyfilt, [1.0], y4*y4)
    out5 = signal.lfilter(energyfilt, [1.0], y5*y5)
    out6 = signal.lfilter(energyfilt, [1.0], y6*y6)
    out7 = signal.lfilter(energyfilt, [1.0], y7*y7)
    out8 = signal.lfilter(energyfilt, [1.0], y8*y8)
    
    
    out = [out1*out1, out2*out2, out3*out3, out4*out4, out5*out5, out6*out6, out7*out7, out8*out8]
    return out


def findkey(freq):
    if freq[0] > freq[1]:
        temp = freq[0]
        freq[0] = freq[1]
        freq[1] = temp
    #print(freq)
    if freq[0] == fr1:
        if freq[1] == fc1:
            return '1'
        elif freq[1] == fc2:
            return '2'
        elif freq[1] == fc3:
            return '3'
        elif freq[1] == fc4:
            return 'A'
    elif freq[0] == fr2:
        if freq[1] == fc1:
            return '4'
        elif freq[1] == fc2:
            return '5'
        elif freq[1] == fc3:
            return '6'
        elif freq[1] == fc4:
            return 'B'
    elif freq[0] == fr3:
        if freq[1] == fc1:
            return '7'
        elif freq[1] == fc2:
            return '8'
        elif freq[1] == fc3:
            return '9'
        elif freq[1] == fc4:
            return 'C'
    elif freq[0] == fr4:
        if freq[1] == fc1:
            return '*'
        elif freq[1] == fc2:
            return '0'
        elif freq[1] == fc3:
            return '#'
        elif freq[1] == fc4:
            return 'D'
        
        
def key(x):
    keys = []
    x = x/32768
    en1, en2, en3, en4, en5, en6, en7, en8 = energy(x)
 
    
    if len(x) > chunk:
        en = [sum(en1[chunk : 2*chunk]), sum(en2[chunk : 2*chunk]), sum(en3[chunk : 2*chunk]), sum(en4[chunk : 2*chunk]), sum(en5[chunk : 2*chunk]), sum(en6[chunk : 2*chunk]), sum(en7[chunk : 2*chunk]), sum(en8[chunk : 2*chunk])]
        #print(max(en))
        if max(en) > 1:
            freq = [0,0]
            while True:
                enarr = np.asarray(en)
                first = np.argmax(enarr)
                enarr[first] = 0
                second = np.argmax(enarr)
                
                if first == 0 or second == 0:
                    freq[0] = fr1
                if first == 1 or second == 1:
                    freq[0] = fr2
                if first == 2 or second == 2:
                    freq[0] = fr3
                if first == 3 or second == 3:
                    freq[0] = fr4
                if first == 4 or second == 4:
                    freq[1] = fc1
                if first == 5 or second == 5:
                    freq[1] = fc2
                if first == 6 or second == 6:
                    freq[1] = fc3
                if first == 7 or second == 7:
                    freq[1] = fc4
                    
                if freq[0]*freq[1] != 0:
                    keys.append(findkey(freq))
                    break
                else:
                    break
    return keys



def add_previous_chunk(x , p_x): 
    if (len(p_x)>0):
        X = np.zeros(2*chunk)
        X[0:chunk] = p_x
        X[chunk:chunk*2] = x.T
    else:
        X = np.zeros(chunk)
        X[0:chunk] =x.T
    return X



nchannels = 1
rate = fs    #sampling frequency
chunk = 1024*2    #buffer size
p = pyaudio.PyAudio()
        
stream = p.open(format = pyaudio.paInt16,
                channels = nchannels,
                rate = rate,
                input = True,
                output = True,
                frames_per_buffer = chunk)



p_x = []
try:
    while True:
            
        x = np.frombuffer(stream.read(num_frames = chunk), dtype ='<i2').reshape(-1, nchannels)    
        
        y = add_previous_chunk(x,p_x)
        p_x = x.T
       
        print(key(y))
        
except KeyboardInterrupt:
    pass

#stopping and closing the stream and terminating pyaudio
stream.stop_stream()
stream.close()
p.terminate()
