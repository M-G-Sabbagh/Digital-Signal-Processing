# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:21:37 2021

@author: Maryam Sabbagh
"""

import pyaudio
import numpy as np

        
nchannels = 1
rate = 44100    #sampling frequency
chunk = 512     #buffer size
p = pyaudio.PyAudio()
        
stream = p.open(format = pyaudio.paInt16,
                channels = nchannels,
                rate = rate,
                input = True,
                output = True,
                frames_per_buffer = chunk)
def signal_processing(x):
            y = x.copy()
            assert y.dtype == np.int16
            return y
try:
    while True:
            
        x = np.frombuffer(stream.read(num_frames = chunk), dtype ='<i2').reshape(-1, nchannels)    
        y = signal_processing(x)
            
        y = y.tobytes()
            
        stream.write(y)
        
except KeyboardInterrupt:
    pass

#stopping and closing the stream and terminating pyaudio
stream.stop_stream()
stream.close()
p.terminate()
