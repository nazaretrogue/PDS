import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def fft_senial_muestreada(x):
    N = len(x)
    W = np.exp(-1j*2*np.pi/N)
    X = [0]*N

    for k in range(N):
        for j in range(N):
            X[k] = X[k]+x[j]*(W**(k*j))

        if X[k] < 10 ** -5:
            X[k] = 0.0

    X = np.array(X).ravel()

    return X

x = np.tile([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1],64)

plt.plot(x)
plt.show()

FFT = fft(x)
X = fft_senial_muestreada(x)

n = 1024
f = np.r_[0:0.5:1/n]

plt.subplot(1,2,1)
plt.plot(f,abs(X[0:512]))
plt.subplot(1,2,2)
plt.plot(f,np.angle(X[0:512]))
plt.show()
