% Se define el array con los pulsos
x=[ones(1,30)];

% Coeficientes
b = 0.1 * ones(1,10);
a = 1;

filtro = filter(b, a, x)

stem(filtro)
