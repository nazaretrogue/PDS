% Se definen los parametros
% Número de coeficientes del filtro
M=31

% Frecuencias de muestreo y de corte
Fs=8000
Fc=2000

% Calculamos la frecuencia de corte que usaremos
wc=Fc/(Fs/2)

% Parámetros del filtro
N=(M-1)/2
n=0:1:M-1

% Se define la ventana rectangular y se redimensiona para poder pintarlo en la grafica
window = rectwin(M)
window = reshape(window, [1 31])

% Generamos el impulso
hd=wc*sinc((n-N)*wc)

% Calculamos la salida del filtro y truncamos con la ventana
h=window.*hd

% Pintamos las graficas
freqz(h,1)
