% Se define el array con los pulsos
x=[ones(1,30)];

% Se definen los coeficientes de las ecuaciones en diferencias
a=[1 0 0.9];
b=[0.3 0.6 0.3];

filtro = filter(b, a, x)

% Pintamos la grafica discreta y continua
stem(filtro);

% Calculamos los polos
zplane(roots(a))
