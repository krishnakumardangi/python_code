import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define wave parameters.
wave_duration = 3
sample_rate = 100
freq = 2
q = 5

# Calculate number of samples.
samples = wave_duration*sample_rate
samples_decimated = int(samples/q)

# Create cosine wave.
x = np.linspace(0, wave_duration, samples, endpoint=False)
y = np.cos(x*np.pi*freq*2)

# Decimate cosine wave.
ydem = signal.decimate(y, q, n=None, ftype='iir', axis=-1, zero_phase=True)
xnew = np.linspace(0, wave_duration, samples_decimated, endpoint=False)

# Plot original and decimated waves.
plt.plot(x, y, '.-', xnew, ydem, 'o-')
plt.xlabel('Time, Seconds')
plt.legend(['data', 'decimated'], loc='best')
plt.show()
