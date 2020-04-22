% Se define el array con los pulsos
x=[1 zeros(1,29)];

% Se definen los coeficientes de las ecuaciones en diferencias
a=[1 0 0.9];
b=[0.3 0.6 0.3];

filtro = filter(b, a, x)

% Pintamos la grafica discreta y continua
stem(filtro);
