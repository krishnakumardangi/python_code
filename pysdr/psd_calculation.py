import numpy as np
import matplotlib.pyplot as plt

Fs = 300 # sample rate
Ts = 1/Fs # sample period
N = 2048 # number of samples to simulate

t = Ts*np.arange(N)
x = np.exp(1j*2*np.pi*50*t) # simulates sinusoid at 50 Hz

f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step

PSD1 = np.abs(np.fft.fft(x))**2 / (N*Fs)
PSD_log1 = 10.0*np.log10(PSD1)
PSD_shifted1 = np.fft.fftshift(PSD_log1)

plt.subplot(2,1,1)
plt.plot(f, PSD_shifted1)
plt.title("Power Spectrum Density without Noise")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)


n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) # complex noise with unity power
noise_power = 2
r = x + n * np.sqrt(noise_power)

PSD = np.abs(np.fft.fft(r))**2 / (N*Fs)
PSD_log = 10.0*np.log10(PSD)
PSD_shifted = np.fft.fftshift(PSD_log)


plt.subplot(2,1,2)
plt.plot(f, PSD_shifted)
plt.title("Power Spectrum Density with Noise")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()
