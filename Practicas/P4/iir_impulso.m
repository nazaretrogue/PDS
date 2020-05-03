x=[1 zeros(1,29)];

% Se definen los coeficientes de las ecuaciones en diferencias
a=[1 0 0.9];
b=[0.3 0.6 0.3];

% Muestra actual
xn=[0 0 0];
yn=[0 0 0];

for n=1:length(x)
	% Los valores cambian en cada vuelta
	xn(3)=xn(2); xn(2)=xn(1); xn(1)=x(n);

	yn(3)=yn(2); yn(2)=yn(1); yn(1)=0.;

	% Se calcula el resultado de operacion de filtrado
	y(n) = -a*yn' +b*xn';

	% Se actualizan los valores
	yn(1)=y(n);
end

% Pintamos la grafica discreta y continua
stem(y);

% Calculamos los polos
zplane(roots(a))
