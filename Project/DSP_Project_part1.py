# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:54:54 2021

@author: User
"""


from scipy import signal
from scipy.io import wavfile as wav


    
    
fs = 8192       # Sample rate, Hz
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


def findsilence(x):
    x = x/32768
    en1, en2, en3, en4, en5, en6, en7, en8 = energy(x)
    S = []
    seg = 820
    n = len(x) // seg
    for i in range(n + 1):      # i = 0 : n
        en = [sum(en1[i*seg : (i + 1)*seg]), sum(en2[i*seg : (i + 1)*seg]), sum(en3[i*seg : (i + 1)*seg]), sum(en4[i*seg : (i + 1)*seg]), sum(en5[i*seg : (i + 1)*seg]), sum(en6[i*seg : (i + 1)*seg]), sum(en7[i*seg : (i + 1)*seg]), sum(en8[i*seg : (i + 1)*seg])]
        if min(en) == 0:
            S = S + [i]
        elif max(en) < 0.1:
            S = S + [i]
    return S, en1, en2, en3, en4, en5, en6, en7, en8

def findkey(freq):
    if freq[0] > freq[1]:
        temp = freq[0]
        freq[0] = freq[1]
        freq[1] = temp
    
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
    seg = 820
    S, en1, en2, en3, en4, en5, en6, en7, en8 = findsilence(x)
    keys = []
    
    for i in range(len(S) - 1):
        freq = [0,0]
        if S[i+1] != S[i] + 1:
            while True:
                if max(en1[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[0] = fr1
                if max(en2[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[0] = fr2
                if max(en3[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[0] = fr3
                if max(en4[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[0] = fr4
                if max(en5[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[1] = fc1
                if max(en6[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[1] = fc2
                if max(en7[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[1] = fc3
                if max(en8[(S[i] + 1)*seg : (S[i + 1])*seg]) > 0.0008:
                    freq[1] = fc4
                if freq[0]*freq[1] != 0:
                    break
                
            keys.append(findkey(freq))
    
    return keys

rate1, data1 = wav.read('DialedSequence_NoNoise.wav')
rate2, data2 = wav.read('DialedSequence_SNR30dB.wav')
rate3, data3 = wav.read('DialedSequence_SNR20dB.wav')
rate4, data4 = wav.read('DialedSequence_SNR10dB.wav')
rate5, data5 = wav.read('DialedSequence_SNR00dB.wav')

print('DialedSequence_NoNoise.wav\n',key(data1))
print('DialedSequence_SNR30dB.wav\n',key(data2))
print('DialedSequence_SNR20dB.wav\n',key(data3))
print('DialedSequence_SNR10dB.wav\n',key(data4))
print('DialedSequence_SNR00dB.wav\n',key(data5))