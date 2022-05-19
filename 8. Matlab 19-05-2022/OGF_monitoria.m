format rat;
clc;
syms z;

lim = 10;

%% Validación ejercicio

fprintf("La sucesión descrita es la siguiente: \n\n");
result = '';

for n = lim - 1:-1:0
    
   if n < 2
       fn = n*5^n;
   elseif mod(n, 2) == 1
       fn = 3*n^2;
   else
       fn = 0;
   end
   
   % Format result string.
   if fn ~= 0
       result = result + string(strtrim(rats(fn))) + '*z';
       if n ~= 1
           result = result + '^' + n + ' + ';
       end
   end
end

fprintf("%s\n\n", result);

%% Expansión por Series de Taylor.

funcion = 5*z + (3*z^7-6*z^5+27*z^3)/((1-z^2)^3);
tay = taylor(funcion, "Order", lim);

fprintf("La expansión por series de Taylor de la función F(z) es: \n\n");
disp(tay);

%% Funciones adicionales

function sum = suma(n)
    sum = 0;
    for k = 0: n
        % sum = sum + 3^k * (n - k);  % Ejercicio 1
        % sum = sum + binom(k, 2) * 2^(n - k);  % Ejercicio 2
        % sum = sum + k^2*2^(n-k);  % Ejercicio 3
        sum = sum + 2^k * 3^(n-k);    % Ejercicio 4
    end
end

function comb = binom(n, k)
    comb = factorial(n)/(factorial(k)*factorial(n - k));
end

function fact = factorial(n)
    fact = 1;
    for i = 1: n
        fact = fact*i;
    end
end

%% Funciones de ejercicios anteriores:

% funcion = z^2*(3/(1 - 3*z) * 1/(1 - z)^2);    % Ejercicio 1
% funcion = z^2*(1/(1 - z)^3 * 1/(1 - 2*z) - 1);    % Ejercicio 2
% funcion =  (z^2 + z)/(1 - z)^3 * 1/(1 - 2*z) - suma(0)*z^0 - suma(1)*z^1;   % Ejercicio 3
% funcion = 1/(1 - 2*z) * 1/(1 -3*z) - suma(0)*z^0 - suma(1)*z^1 - suma(2)*z^2 - suma(3)*z^3;   % Ejercicio 4
% funcion = (1 - z)^2 * (1/(1 - 2*z));   % Ejercicio 5
% funcion = 1/(1-3*z)^4;

% fn = 2^(n-2);  % Ejercicio 5
% fn = suma(n);
