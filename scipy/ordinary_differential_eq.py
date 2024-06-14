import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation for a simple harmonic oscillator
def harmonic_oscillator(y, t, omega):
    """
    y: array_like, shape (2,)
        Array containing the current values of y and y'
    t: float
        Current time
    omega: float
        Angular frequency of the oscillator
    """
    print(y,"\n")
    y0, y1 = y  # Unpack the state vector
    print(y0,"\n")
    print(y1,"\n")
    dydt = [y1, -omega**2 * y0]  # Define the derivatives
    return dydt

# Set the initial conditions and parameters
y0 = [1.0, 0.0]  # Initial position and velocity  # Initial value
omega = 2.0  # Angular frequency   # Integrating constant
t = np.linspace(0, 10, 1000)  # Time points

# Solve the ODE using odeint
solution = odeint(harmonic_oscillator, y0, t, args=(omega,))

# Plot the solution
plt.plot(t, solution[:, 0], 'b', label='Position')
plt.plot(t, solution[:, 1], 'g', label='Velocity')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Simple Harmonic Oscillator')
plt.legend()
plt.grid()
plt.show()
