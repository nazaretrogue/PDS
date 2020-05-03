% Se define el array con los pulsos
x=[1 zeros(1,29)];

% Coeficientes
b = 0.1 * ones(1,10);
a = 1;

% Muestra actual
xn = zeros(1,10);
yn = zeros(1,10);

% Se calculan los pulsos
for n=1:length(x)
  for m=length(b):-1:2
    xn(m) = xn(m-1);
    yn(m) = yn(m-1);
  end

  xn(1)=x(n);
  yn(1)=0.;

  % Se hace la media de los 10 valores al multiplicar por b
  y(n) = b*xn';

end

stem(y);
zplane(roots(a))
