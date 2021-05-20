# Imports
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin
from matplotlib.patches import Arc, Arrow
from matplotlib.widgets import Slider

# Réglage de l'affichage
fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.title('Trajectoire')
plt.subplots_adjust(bottom=0.2)

# Constantes de la simulation
gterre = 9.81 # m/s^2
v0 = 50 # m/s
alpha = 45 # rad

# On calcul les coordonnées de v0
v0a = ax.add_patch(Arrow(0, 0, 0, 0, color='r', label='v0'))

# Angle alpha
angle = ax.add_patch(Arc([0, 0], 5, 5, 0, 0, alpha, color='g', label='Alpha'))

# Définition du graphique
l, = plt.plot([], [], 'ob', label='y=f(x)')

# Sliders (pour changer les réglages)
ax_v0 = plt.axes([0.25, 0.1, 0.65, 0.03])
slider_v0 = Slider(ax_v0, 'v0', 5, 100, valinit=v0)

ax_alpha = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_alpha = Slider(ax_alpha, 'alpha', 1, 90, valinit=alpha)

# Calcul des coordonnées selon les paramètres
def calculer(val):
    # Récupère les valeurs
    v0 = slider_v0.val
    alpha = slider_alpha.val
    tmax = int(2*v0*sin(alpha * pi / 180)/gterre) + 1
    t = np.linspace(0, tmax, tmax*10)

    # On modifie les coordonnées
    x = v0 * cos(alpha * pi / 180) * t
    y = -0.5 * gterre * t**2 + v0 * sin(alpha * pi / 180) * t
    l.set_xdata(x)
    l.set_ydata(y)

    # De v0 aussi
    global v0a
    v0x = v0 * cos(alpha * pi / 180)
    v0y = v0 * sin(alpha * pi / 180)
    v0a.remove()
    v0a = ax.add_patch(Arrow(0, 0, v0x, v0y, color='r', label='v0'))

    # Et de alpha
    global angle
    angle.remove()
    angle = ax.add_patch(Arc([0, 0], v0x, v0y, 0, 0, alpha, color='g', label='Alpha'))

    # On update le graphique
    ax.set_xlim([0, max(np.max(x), v0x) + 5])
    ax.set_ylim([0, max(np.max(y), v0y) + 5])
    fig.canvas.draw_idle()

# Ajout de la méthode de calcul aux sliders
slider_v0.on_changed(calculer)
slider_alpha.on_changed(calculer)

# On calcul la trajectoire initiale
calculer(None)

# On affiche
plt.show()
