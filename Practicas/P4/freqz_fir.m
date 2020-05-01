% Se definen los coeficientes de las ecuaciones en diferencias
b = 0.1 * ones(1,10);
a = 1;

[H,w] = freqz(b,a,1024);

% Pintamos las gráficas
plot(w,abs(H))
