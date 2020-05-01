% Se definen los coeficientes de las ecuaciones en diferencias
a = [1 0 0.9];
b = [0.3 0.6 0.3];

[H,w] = freqz(b,a,1024);

% Pintamos la gráfica
plot(w,abs(H))
