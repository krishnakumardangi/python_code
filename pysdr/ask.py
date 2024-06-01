import numpy as np
import matplotlib.pyplot as plt
import random

num_symbols = 100
fc = 100  # 0.1 KHz

x = np.random.randint(0, 2, num_symbols)  # 0 or 1
t0 = np.arange(0, 1, 1/num_symbols)
t = np.arange(0, 1, 1/(40*fc))

x_plot = []
y = []
amplitude = [1,2]
    
for i in range(len(t)):
    # BPSK modulation
    if i%80 == 0:
        val = random.randint(0,1)
        x_plot.append(val)
        x_plot.append(val)
        y.append(amplitude[val]*np.sin(2*np.pi*fc*t[i]))  # 0 or 1
    else:
        y.append(amplitude[val]*np.sin(2*np.pi*fc*t[i]))  # 0 or 1
    
t1 = np.arange(0, 1, 1/(len(x_plot)))

plt.figure("ASK Modulation")
plt.subplot(2,1,1)
plt.title("Binary Signals")
plt.plot(t1, x_plot)
plt.grid(True)

plt.subplot(2,1,2)
plt.title("ASK Modulation")
plt.plot(t, y, '-')
plt.grid(True)

plt.show()
