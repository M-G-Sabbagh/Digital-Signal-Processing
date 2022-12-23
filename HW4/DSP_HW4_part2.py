# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:59:52 2021

@author: Maryam Sabbagh
"""

import pyaudio
import numpy as np
import matplotlib.pyplot as plt

        
nchannels = 1
rate = 8000     #sampling frequency
chunk = 512     #buffer size
p = pyaudio.PyAudio()
        
stream = p.open(format= pyaudio.paInt16,
                channels= nchannels,
                rate= rate,
                input=True,
                output=True,
                frames_per_buffer=chunk)

def signal_processing(x):
            y = x.copy()
            assert y.dtype==np.int16
            return y
        
fig, ax = plt.subplots()
z = np.arange(0, chunk)
line, = ax.plot(z, np.random.rand(chunk))
ax.set_ylim(-32800, 32800)  #data type: 16 bit integer
ax.set_xlim(0, chunk)       #limiting x axis to chunk(buffer size)
        
fig.canvas.draw()
plt.show(block=False)
ax.draw_artist(ax.patch)
        
try:
    while True:
        while True:
            
            x = np.frombuffer(stream.read(num_frames= chunk), dtype='<i2').reshape(-1, nchannels)
            y = signal_processing(x)
            
            line.set_ydata(y)
            ax.draw_artist(ax.patch)
            ax.draw_artist(line)
            fig.canvas.update()
            fig.canvas.flush_events()

except KeyboardInterrupt:
    pass


#stopping and closing the stream and terminating pyaudio
stream.stop_stream()
stream.close()
p.terminate()
