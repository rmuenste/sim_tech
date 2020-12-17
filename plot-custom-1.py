import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Cos, Sin = np.cos(X), np.sin(X)
plt.plot(X, Cos, color="blue", linewidth=2.5, linestyle="-", label="Kosinus")
plt.plot(X, Sin, color="red",  linewidth=2.5, linestyle="--", label="Sinus")
# Gitter hinzufügen
plt.grid()
# Titel
plt.title("Sinus und Kosinus",loc="center")
# Legende
plt.legend(loc="best", frameon=True)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
plt.show()