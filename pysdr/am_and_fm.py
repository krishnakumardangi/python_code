'''Below is an example of FM and AM modulation where the “signal” at the top is the audio signal being modulated onto to the carrier.'''

import numpy as np
import matplotlib.pyplot as plt
import random

num_symbols = 1000
fm = 10 # 10 Hz
fc = 100 # 100 Hz
t = np.arange(0, 1, 1/(40*num_symbols))

x = np.sin(2*np.pi*fm*t)


# Signal to be Modulated
plt.figure("AM and FM")
plt.subplot(2,2,1)
plt.title("Signal to be Modulated")
plt.plot(t, x)
plt.grid(True)


y = np.sin(2*np.pi*fc*t)
# Carrier wave
plt.subplot(2,2,2)
plt.title("Carrier")
plt.plot(t, y)
plt.grid(True)


am = x*y
# With Phase noise
plt.subplot(2,2,3)
plt.title("Amplitude Modulation")
plt.plot(t, am)
plt.grid(True)


FM = []
phase = [fc-fm, fc+fm]

for i in range(len(t)):
    # BPSK modulation
    if i%80 == 0:
        val = random.randint(0,1)
        FM.append(np.sin(2*np.pi*phase[val]*t[i])) 
    else:
        FM.append(np.sin(2*np.pi*phase[val]*t[i]))  
# With AWGN and Phase noise
plt.subplot(2,2,4)
plt.title("Frequency Modulation")
plt.plot(t, FM)
plt.grid(True)

plt.show()
