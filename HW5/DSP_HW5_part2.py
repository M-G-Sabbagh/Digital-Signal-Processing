# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:41:11 2021

@author: M Sabbagh
"""

import pyaudio
import numpy as np
import parselmouth
from parselmouth.praat import call


nchannels = 1
rate = 8000    #sampling frequency
chunk = 512    #buffer size

        
def change_pitch(sound, factor):
          
    manipulation = call(sound, "To Manipulation", 0.01, 75, 600)

    pitch_tier = call(manipulation, "Extract pitch tier")

    call(pitch_tier, "Multiply frequencies", sound.xmin, sound.xmax, factor)

    call([pitch_tier, manipulation], "Replace pitch tier")
    return call(manipulation, "Get resynthesis (overlap-add)")

def chunk_processing(x, rate):
    
    #x = x.astype(np.float64) / 32768
    x = parselmouth.Sound(x, rate)
    y = change_pitch(x, 1)
    y = y.values.reshape(-1) 
    y = y.astype(np.int16)#* 32768
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
        y = chunk_processing(x, rate)
            
        y = y.tobytes()
            
        stream.write(y)
        
except KeyboardInterrupt:
    pass

#stopping and closing the stream and terminating pyaudio
stream.stop_stream()
stream.close()
p.terminate()