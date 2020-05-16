% Coeficientes del filtro
M=34

% Debemos definir las bandas de frecuencia
% ya que fir2 necesita un vector con ellas

% Como la frecuencia de corte es 4kHz y el
% vector debe empezar en 0 y acabar en 1,
% las bandas que se van a tocar son las de 0.4
f=[0 0.4 0.4 1]


% Se define la amplitud de cada banda de
% frecuencia del vector f
amplitud = [0 0 1 1]

% Se devuelven M+1 coeficientes
h = fir2(M, f, amplitud)

freqz(h,1)
