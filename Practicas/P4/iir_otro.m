% Se define el array con los pulsos
x=[1 zeros(1,29)];

 % Se definen los coeficientes de las ecuaciones en diferencias
a=[1 -2.5 1];
b=[4 0 0];

y = filter(b, a, x)

% Pintamos la grafica discreta y continua
stem(y);

% Calculamos los polos
zplane(roots(a))
