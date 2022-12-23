# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:18:44 2021

@author: M Sabbagh
"""

import pyaudio
import numpy as np

nchannels = 1
rate = 8000     #sampling frequency
chunk = 512     #buffer size
incPercent = 50     
L = chunk
I = np.int((1 + incPercent/100)* L)
A = L - (I - L)


s1 = np.zeros(L)
s2 = np.zeros(L)
s3 = np.zeros(L)
alpha = np.zeros(L)
#print(A ,L ,I, L-A)
alpha[A: L] = np.linspace(1, 0, num = L - A)
#print("alpha =", alpha)
#print(alpha.shape)
#x = np.zeros(L)
#print(x.shape)
#print(x.ndim)
def chunk_processing(x):
            #x.reshape(1, L)
            xdimnew = np.linspace(0, L - 1, I, endpoint = True)  #np.arange(I)
            xdimold = np.linspace(0, L - 1, L, endpoint = True)  #np.arange(L)
            #print(xdimold)
            #print(xdimnew)
            x = np.interp(xdimnew, xdimold, x)
            #print(x.shape)
            s1 = x[0: L]
            s2[A: L] = x[L: I]
            s3[0: A] = s1[0: A]
            s3[A: L] = alpha[A: L]* s1[A: L] + (1 - alpha[A: L])* s2[A: L]
            y = s3
            y = y.astype(np.int16)
            #assert y.dtype == np.int16
            return y

p = pyaudio.PyAudio()
        
stream = p.open(format = pyaudio.paInt16,
                channels = nchannels,
                rate = rate,
                input = True,
                output = True,
                frames_per_buffer = chunk)
        
try:
    while True:
            
        x = np.frombuffer(stream.read(num_frames = chunk), dtype = np.int16)   
        y = chunk_processing(x)
            
        y = y.tobytes()
            
        stream.write(y)
        
except KeyboardInterrupt:
    pass

#stopping and closing the stream and terminating pyaudio
stream.stop_stream()
stream.close()
p.terminate()