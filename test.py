import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
wav = wave.open("Lab1.wav","r")
raw = wav.readframes(-1)
raw = np.frombuffer(raw,"int16")
sampleRate = wav.getframerate()
params = wav.getparams()          #获取音频信息
print(params)
print(raw)
# if wav.getnchannels() == 2:
#     print("Sterco Files are not supported.Use Mono Files")
#     sys.exit(0)

Time = np.linspace(0,len(raw)/sampleRate,num = len(raw))
print(Time)
plt.title("Waveform of Wave File")
plt.plot(Time,raw,color="blue")
plt.ylabel("Amplitude")
plt.show()