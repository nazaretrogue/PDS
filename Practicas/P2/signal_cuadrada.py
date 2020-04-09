import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Crea las muestras de la señal
x = np.tile([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1],64)
plt.plot(x)

# Mostramos la señal original
plt.show()

# Calcula la transfomada de Fourier
X = fft(x)
f = np.r_[0:0.5:1/1024]
plt.subplot(1,2,1)
plt.plot(f,abs(X[0:512]))
plt.subplot(1,2,2)
plt.plot(f,np.angle(X[0:512]))

# Mostramos la transformada
plt.show()
