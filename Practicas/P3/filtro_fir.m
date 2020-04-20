% Se definen el array con los pulsos
x = [1 zeros(1, 29)];

% Para la media tomamos 10 muestras
h = ones(1, 10);

% Inicializamos la memoria con ceros
signal_mem = zeros(1, 10);

for n=1:length(x)
  x_in = x(n);
  signal_mem(1) = x_in;
  y_out = h(1)*signal_mem(1);

  % Recorremos el array de muestras anteriores
  for m=length(h):-1:2
    % Sumamos todos los factores anteriores
    y_out = y_out + h(m)*signal_mem(m);
    signal_mem(m) = signal_mem(m-1);
  end

  % Calculamos la media
  y(n) = y_out/length(h);
end
