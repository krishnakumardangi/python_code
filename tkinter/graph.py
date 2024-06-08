# Plot any graph using this python file, but this you have to made some changes in it.

import numpy as np
import matplotlib.pyplot as plt

# Your functions
# Funtion 1
x1 = np.arange(0.1, 100, 0.1)
y1 = np.sqrt(x1)

# Funtion 1
x2 = np.arange(0.1, 100, 0.1)
y2 = np.log(x2)

# Plot
plt.plot(x1, y1, '-')
plt.plot(x2, y2, '-')
plt.show()
