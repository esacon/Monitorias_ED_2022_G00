% Número de iteraciones.
n = input('Digite el número de iteraciones: ');

x = zeros(1, n); % Matriz de ceros de 1xn (1 fila, n columnas)
y = zeros(1, n); % Matriz de ceros de 1xn (1 fila, n columnas) - Vector de 0's.

% Las tres reglas se seleccionan de forma aleatoria con igual probabilidad.
% 
% Regla 1: x=0.5*x_{n-1} 
%          y=0.5*y_{n-1}
%
% Regla 2: x=0.5*x_{n-1} + 0.25
%          y=0.5*y_{n-1} + sqrt(3)/4
%
% Regla 3: x=0.5*x_{n-1} + 0.5 
%          y=0.5*y_{n-1}
%
% Se sabe que, dado que es una relación de recuerrencia, sus casos bases
% son x_1 = 0 y_1 = 0. Se escojen iteraciones con n = 100, 1000 y 10000.


for i=2:n
    c = randi(3); % Número aleatorio entre 1 y 3.
    % Dependiendo del caso, se guarda el valor en el vector.
    switch c
        case 1    
            x(i) = 0.5*x(i-1);
            y(i) = 0.5*y(i-1);
        case 2
            x(i) = 0.5*x(i-1) + .25;
            y(i) = 0.5*y(i-1) + sqrt(3)/4;
        case 3
            x(i) = 0.5*x(i-1) + .5;
            y(i) = 0.5*y(i-1);
    end
end
% Graficamos los vectores x, y de color rojo y cada marcador con un
% triángulo.
plot(x, y, '^r', 'markersize', 4);
% Asignamos un título.
title('Triángulo de Sierpinski');
% Asignamos una leyenda.
text = sprintf('N=%d iteraciones', n);
legend(text);