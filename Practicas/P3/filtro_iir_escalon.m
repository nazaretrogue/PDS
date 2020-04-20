% Se definen los arrays con los pulsos
x=[1 ones(1,29)];

% Se definen los coeficientes de las ecuaciones en diferencias
a=[1 0 0.9];
b=[0.3 0.6 0.3];

% Muestra actual
xn=[0 0 0];
yn=[0 0 0];

filtro = filter(b, a, x)

% Pintamos la grafica discreta y continua
stem(filtro);
