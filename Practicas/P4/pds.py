# -*- coding: utf-8 -*-
"""

Procesamiento Digital de Señales
Funciones de apoyo para realizar la práctica 4

"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def impz(b,a,n):
    impulse = np.repeat(0.,len(n)); impulse[np.where(n==0)] = 1.
    response = signal.lfilter(b, a, impulse)
    plt.stem(n, response)
    plt.ylabel('Amplitud')
    plt.xlabel('n (muestras)')
    plt.title('Respuesta impulsiva')
    plt.show()

    
def stepz(b,a,n):
    step = np.repeat(0.,len(n)); step[np.where(n>=0)] = 1.
    response = signal.lfilter(b,a,step)
    plt.stem(n, response)
    plt.ylabel('Amplitud')
    plt.xlabel('n (muestras)')
    plt.title('Respuesta al escalon')
    plt.show()


def zplane(b,a):
    
    # Fix axes
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Draw circle
    circle = patches.Circle((0,0),radius=1,color='black',ls='dashed',fill=False)
    ax.add_patch(circle)

     # Make a and b of equal length
    a = np.append(a, np.repeat(0, max(len(a),len(b))-len(a)))
    b = np.append(b, np.repeat(0, max(len(a),len(b))-len(b)))
    
    # Plot poles
    p = np.roots(a)
    plt.plot(p.real, p.imag, 'kx', ms=7)

    # Plot zeros    
    z = np.roots(b)
    plt.plot(z.real, z.imag, 'ko', ms=7)

    plt.axis('scaled')
    plt.show()


def plot_freq_resp(b, a=1, worN=None):
    w, h = signal.freqz(b, a, worN)
    plt.plot(w, 20 * np.log10(abs(h)), 'b')
    plt.ylabel('Amplitud [dB]', color='b')
    plt.xlabel('Frecuencia [rad/muestra]')
    plt.gca().twinx()
    angles = np.unwrap(np.angle(h))
    plt.plot(w, angles, 'g')
    plt.ylabel('Fase (rad)', color='g')
    plt.title('Respuesta en frecuencia')
    plt.grid()
    plt.show()


def plot_group_delay(b,a):
    w, gd = signal.group_delay((b, a))
    plt.plot(w, np.round(gd,5))
    plt.ylabel('Retardo de grupo [muestras]')
    plt.xlabel('Frecuencia [rad/muestra]')
    plt.title('Retardo de grupo')
    plt.show()
