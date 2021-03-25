# Imports
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin
from matplotlib.patches import Arc

# Réglage de l'affichage
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.title("Trajectoire")

# Récupère l'ensemble des t
t = np.linspace(0, 3, 50)

# Constantes de la simulation
gterre = 9.81 # m/s^2
v0 = 20 # m/s
alpha = pi/4 # rad
y0 = 0 # m

# On calcul les coordonnées de v0
v0x = v0 * cos(alpha)
v0y = v0 * sin(alpha)
plt.arrow(0, 0, v0x, v0y, head_width=1, head_length=1, color='r', label="v0")

# Angle alpha
angle = Arc([0, 0], 5, 5, 0, 0, alpha * 180 / pi, color='g', label='Alpha')
ax.add_patch(angle)

# On calcul les coordonnées des points
x = v0 * cos(alpha) * t
y = -0.5 * gterre * t**2 + v0 * sin(alpha) * t + y0
plt.plot(x, y, 'ob', label="y=f(x)")

# On affiche
plt.legend()
plt.show()