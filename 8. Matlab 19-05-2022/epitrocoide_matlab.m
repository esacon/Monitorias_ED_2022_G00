clc; % Limpiamos la consola.
close all; % Cerramos las figuras abiertas (si hay).

% input - Permite recibir datos de entrada, y asigna un tipo de dato
% automáticamente. El texto debe ir entre comillas simples ''.
a = input('Ingrese el radio de la circunferencia directriz: ');
b = input('Ingrese el radio de la circunferencia generatriz: ');
h = input('Ingrese la distancia del punto al centro de la circunferencia generatriz: '); 

% Imprimir texto con formato:
fprintf('\na=%i\tb=%i\th=%.2f\n', a, b, h);

disp(a); % Muestra el contenido de la variable.

[x, y] = epitrocoide(a, b, h);

% Para graficar utilizamos el comando plot
plot(x, y, '-r','linewidth', 2);
title('Epitrocoide');
text = sprintf('a=%i\tb=%i\th=%.2f', a, b, h);
legend(text);
xlabel('Ángulo en radianes');
grid on;

% Funcion que calcula un epitrocoide.
function [x, y] = epitrocoide(a, b, h)
    % Para operar con los elementos de un vector, se coloca un . antes de la operación. 
    theta = -8*pi:pi/30:8*pi; % lim_inf:paso:lim_sup.
    x = (a + b).*cos(theta) - h.*cos((a + b)/b*theta);
    y = (a + b).*sin(theta) - h.*sin((a + b)/b*theta);
end

