# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:38:29 2021

@author: User
"""


from scipy import signal
from scipy import io    

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
io.savemat('BPF_697.mat', {'BPF_697': f1 })

band = [fr2 - 30, fr2 + 30]  # Desired pass band for filter2, Hz
trans_width = 6    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f2 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_770.mat', {'BPF_770': f2 })   


band = [fr3 - 40, fr3 + 40]  # Desired pass band for filter3, Hz
trans_width = 8    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f3 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_852.mat', {'BPF_852': f3 })


band = [fr4 - 40, fr4 + 40]  # Desired pass band for filter4, Hz
trans_width = 8    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f4 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_941.mat', {'BPF_941': f4 })


band = [fc1 - 50, fc1 + 50]  # Desired pass band for filter5, Hz
trans_width = 10    # Width of transition from pass band to stop band, Hz
numtaps = 1500        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f5 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_1209.mat', {'BPF_1209': f5 })



band = [fc2 - 55, fc2 + 55]  # Desired pass band for filter6, Hz
trans_width = 11    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f6 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_1336.mat', {'BPF_1336': f6 })


band = [fc3 - 65, fc3 + 65]  # Desired pass band for filter7, Hz
trans_width = 13    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f7 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_1477.mat', {'BPF_1477': f7 })



band = [fc4 - 75, fc4 + 75]  # Desired pass band for filter8, Hz
trans_width = 15    # Width of transition from pass band to stop band, Hz
numtaps = 1000        # Size of the FIR filter.
edges = [0, band[0] - trans_width, band[0], band[1], band[1] + trans_width, 0.5*fs]
f8 = signal.remez(numtaps, edges, [0, 1, 0], Hz=fs)
io.savemat('BPF_1633.mat', {'BPF_1633': f8 })



cutoff = 200    # Desired cutoff frequency, Hz
trans_width = 300  # Width of transition from pass band to stop band, Hz
numtaps = 400      # Size of the FIR filter.
energyfilt= signal.remez(numtaps, [0, cutoff, cutoff + trans_width, 0.5*fs], [1, 0], Hz=fs)
io.savemat('LPF.mat', {'LPF': energyfilt })