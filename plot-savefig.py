import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='A Simple Plot')
ax.grid()

fig.savefig("test.png", type="png", dpi=100)
fig.savefig("test.pdf")