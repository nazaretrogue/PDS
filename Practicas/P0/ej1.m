f0 = 262;
A = 2;
phi = pi/4;
fSampling = 8000;
tSampling = 1/fSampling;
t = -0.005:tSampling:0.005;
x = A*sin(2*pi*f0*t+phi);
x2 = A*sawtooth(2*pi*f0*t);
num_col_figura = 3;
figure(1);
subplot(num_col_figura, 1, 1); % Filas, columnas, id ventana
%plot(t, x);
plot(t, x, 'Color', [1, 0, 1], 'LineWidth', 3, 'LineStyle', ':');
subplot(num_col_figura, 1, 2);
%plot(t, x2);
plot(t, x2, '--rs', 'MarkerSize', 5, 'MarkerFaceColor', 'g', 'MarkerEdgeColor', 'g');

subplot(num_col_figura, 1, 3);
plot(t, x, 'Color', [1, 0, 1], 'LineWidth', 3, 'LineStyle', ':');
hold on;
plot(t, x2, '--rs', 'MarkerSize', 5, 'MarkerFaceColor', 'g', 'MarkerEdgeColor', 'g');

hold on;
stem(t, x);