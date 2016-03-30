#!/usr/bin/env python
#
# Tyler Anderson Tue Mar 29 21:13:42 EDT 2016
# Try to droop and signal and correct it. 

import numpy as np
import matplotlib.pyplot as plt

# Some constants
LEN = 1024
GAMMA = 100.

# Generate the transfer function
n1 = np.arange(LEN)
h1 = -1*np.exp(-n1/GAMMA)/GAMMA
h1[0] = h1[0] + 1.
fig, ax = plt.subplots()
ax.stem(n1,h1)
plt.xlim(-10,LEN)
plt.show()

# Show the DFT of it
