%% Graficar en Matlab.
% Definimos el vector de x.
x = 0:pi/180:2*pi; % lim_inf:paso:lim_sup.
% Definimos la funci�n f(x).
y = sin(x);
% Gr�fica de una l�nea punteada de ancho 2 y de color verde.
plot(x, y, '--g', 'linewidth', 2);
grid on; % Activar cuadr�cula.
xlabel('x') % Texto en el eje X.
ylabel('sin(x)') % Texto en el eje Y.
title('Mi primera gr�fica en Matlab') % T�tulo del gr�fico.
legend('sin(x)') % Leyenda de la funci�n.