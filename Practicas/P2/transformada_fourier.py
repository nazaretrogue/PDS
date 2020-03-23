import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def fft_senial_muestreada(x):
    N = len(x)
    W = np.exp(-1j*2*np.pi/N)
    X = [0]*N
    X_aux = [0]*N

# <script>
#   var yjr = []; //real part of data
#   var yji = []; //imaginary part of data
#   var Ykr = [];  //real part of Fourier coefficients
#   var Yki = [];  //imaginary part of Fourier coefficients
#   var pi = Math.PI;
#
#   yjr = [0.7013, -0.0724, 0.0988, 0.0715, 0.4013, -0.0901, -0.1263, 0.2660];
#   yji = [0.0437, 0.5133, -0.2688, -0.1162, 0.1188, -0.1408, -0.0688, -0.3813];
#
#   N = yjr.length;
#
#   start = 0; //is the standard DFT
#   //start = Math.floor(N/2)-N+1; has all k vectors in the first Brillouin zone
#
#   for (k=0; k<N; k++) {
#     ks = start+k;
#     Ykr[k] = 0; Yki[k] = 0;
#     for (j=0; j<N; j++) {
#       Ykr[k] = Ykr[k] + yjr[j]*Math.cos(2*pi*ks*j/N) - yji[j]*Math.sin(2*pi*ks*j/N);
#       Yki[k] = Yki[k] + yjr[j]*Math.sin(2*pi*ks*j/N) + yji[j]*Math.cos(2*pi*ks*j/N);
#     }
#     Ykr[k] = Ykr[k]/N; Yki[k] = Yki[k]/N;
#     document.write("Y<sub>"+k+"<\/sub> = "+Ykr[k]+" + <i>i</i>("+Yki[k]+")<br \/>");
#   }
#
# </script>

    for k in range(N):
        for i in range(N):
            X_aux[k] = X_aux[k]+x[i]*(W**(k*i))

    X = fft(X_aux)

    return X

x = np.tile([1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1],64)

for k in range(len(x)):
    print(x[k] )

plt.plot(x)
plt.show()

FFT = fft(x)
X = fft_senial_muestreada(x)

n = 1024
f = np.r_[0:0.5:1/n]

plt.subplot(1,4,1)
plt.plot(f,abs(X[0:512]))
plt.subplot(1,4,2)
plt.plot(f,np.angle(X[0:512]))
plt.subplot(1,4,3)
plt.plot(f,abs(FFT[0:512]))
plt.subplot(1,4,4)
plt.plot(f,np.angle(FFT[0:512]))
plt.show()
