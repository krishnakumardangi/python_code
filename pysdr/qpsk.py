''' Even though we could generate the complex symbols directly, let’s start from the knowledge that QPSK has four symbols at 90-degree intervals around the unit circle. We will use 45, 135, 225, and 315 degrees for our points. First we will generate random numbers between 0 and 3 and perform math to get the degrees we want before converting to radians.'''



import numpy as np
import matplotlib.pyplot as plt

num_symbols = 1000

x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
x_degrees = x_int*360/4.0 + 45 # 45, 135, 225, 315 degrees
x_radians = x_degrees*np.pi/180.0 # sin() and cos() takes in radians
x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # this produces our QPSK complex symbols
# Without AWGN and Phase Noise
plt.figure("QPSK Constellation")
plt.subplot(2,2,1)
plt.title("QPSK Modulation")
plt.plot(np.real(x_symbols), np.imag(x_symbols), '.')
plt.grid(True)


n = (np.random.randn(num_symbols) + 1j*np.random.randn(num_symbols))/np.sqrt(2) # AWGN with unity power
noise_power = 0.01
r1 = x_symbols + n * np.sqrt(noise_power)
# With AWGN 
plt.subplot(2,2,2)
plt.title("QPSK Modulation with AWGN")
plt.plot(np.real(r1), np.imag(r1), '.')
plt.grid(True)


phase_noise = np.random.randn(len(x_symbols)) * 0.1 # adjust multiplier for "strength" of phase noise
r2 = x_symbols * np.exp(1j*phase_noise)
# With Phase noise
plt.subplot(2,2,3)
plt.title("QPSK Modulation with Phase Noise")
plt.plot(np.real(r2), np.imag(r2), '.')
plt.grid(True)


r3 = x_symbols * np.exp(1j*phase_noise) + n * np.sqrt(noise_power)
# With AWGN and Phase noise
plt.subplot(2,2,4)
plt.title("QPSK Modulation with AWGN and Phase Noise")
plt.plot(np.real(r3), np.imag(r3), '.')
plt.grid(True)

plt.show()
