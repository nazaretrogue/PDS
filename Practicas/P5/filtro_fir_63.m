% Coeficientes del filtro
M=63

% Frecuencias de muestreo y corte
Fs=8000
Fc=2000
wc=Fc/(Fs/2)

h = fir1(M-1, wc, rectwin(M))

freqz(h,1)
