%% Graficar en Matlab.
% Definimos el vector de x.
x = 0:pi/180:2*pi; % lim_inf:paso:lim_sup.
% Definimos la función f(x).
y = sin(x);
% Gráfica de una línea punteada de ancho 2 y de color verde.
plot(x, y, '--g', 'linewidth', 2);
grid on; % Activar cuadrícula.
xlabel('x') % Texto en el eje X.
ylabel('sin(x)') % Texto en el eje Y.
title('Mi primera gráfica en Matlab') % Título del gráfico.
legend('sin(x)') % Leyenda de la función.