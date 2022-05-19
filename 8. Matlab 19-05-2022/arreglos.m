clc; % Limpiar consola.
% clear all; % Limpia el espacio de trabajo.
close all; % Cierra las gráficas que estén abiertas.

%% Matrices predefinidas.

nf = input('Digite el número de filas de la matriz: ');
nc = nf;

% Matriz de Pascal.
fprintf('\nLa matriz de Pascal de tamaño %ix%i es: \n', nf, nc); % print. \n es salto de línea.
M = pascal(nf);
disp(M); % Display de una variable.

% Matriz de Ceros.
fprintf('\nLa matriz de Ceros de tamaño %ix%i es: \n', nf, nc);
M = zeros(nf, nc);
disp(M);

% Matriz de Unos.
fprintf('\nLa matriz de Unos de tamaño %ix%i es: \n', nf, nc);
M = ones(nf);
disp(M);

% Matriz de Identidad.
fprintf('\nLa matriz de Identidad de tamaño %ix%i es: \n', nf, nc);
M = eye(nf);
disp(M);

%%  Otras matrices

% Matriz aleatoria.
min = -10;
max = 20;
nf = 5;
nc = nf + 1;

M = randi([min max], nf, nc); % Genera una matriz aleatoria de tamaño nf x nc. Con valores entre min y max.
disp(M);

% Matriz manual
% Las columnas se separan con ' '. Mientras que las filas con ';'.
% Forma intuitiva:
%
% M = [[1 2 3]; % Primera fila
%    [4  5 6]; % Segunda fila
%    [7 8 9]   % Tercera fila
%    ];
%
M = [1 2 3; 4 5 6; 7 8 9]; % Forma más usada.
disp(M)

%% Vectores

% Dentro de las distintas formas que hay para crear un vector, se tienen:
% Nota:
% A diferencia de Python, en Matlab sí se tiene en cuenta el límite
% superior.
% En Python los vectores llegan hasta lim_sup - 1.

V = -2:pi:10; % Esto es un vector con valores entre -2 y 10, con pasos de pi.
disp(V);

% Vector a través de un espacio linealmente distribuido.
% Para linspace se tienen como parámetros a, b, e. Donde e es la cantidad
% de elementos que tendrá el vector. A y B son los límites del mismo.

a = -2;
b = 5;
e = 8;

y = linspace(a, b, e); % Vector entre -2 y 5 con 8 elementos.
disp(y)

paso = (b - a)/(e - 1); % Salto entre los elementos.
disp(paso)
e = (b - a + paso)/paso; % Cantidad de elementos.
disp(e)

%% Manejo de elementos

% En Matlab es importante saber que los arreglos no comienzan en 0, como en
% los demás lenguajes de programación. Por el contrario, inician en 1.

% Acceder a las filas de una matriz.

M = magic(5);

% Para acceder a los elementos de un arreglo, debemos especificar las
% posiciones de los mismos. Esto se logra mediante un escalar o un vector.
%
% Por ejemplo:

disp(M(1, 1:1:5)) % De la matriz M, accedemos a la 1ra fila y a las columnas de la 1 a la 5.

% También es posible especificar el punto de partida o final, sin el número
% que lo indique.

% :5 --> Un vector, que comienza en el 1er elemento hasta el 5. Con paso 1.
% 2:end --> Un vector, que comienza en el 2do elemento hasta el último. Con paso 1.
% : --> todos los elementos

M(3, 1:2:end) % Fila 3 Columnas impares
M(3, 2:2:end) % Fila 3 Columnas pares

%% Diagonales

% Se define como diagonal principal aquella que divide (diagonalmente) la
% matriz. Esta va de arriba hacia abajo, los valores por encima se enumeran
% positivamente; mientras que los de por debajo, negativamente.

% DP = 0.
diag(diag(M, 0))

% DP = 1.
diag(diag(M, 1))

% DP = 0.
diag(diag(M, 1))

% La diagonal de una matriz devuelve un vector.
% La diagonal de un vector devuelve una matriz.

% Diagonal secundarias es aquella que va en el orden inverso a la
% principal.

% fddf
ds = 0;
fliplr(diag(diag(fliplr(M), ds)));

%% Intercambies diagonales de una matriz.
n = 6;
M = pascal(n); % Matriz de 6x6.
fprintf('\nLa matriz a la cual se desean intercambiar diagonales es:\n');
disp(M);

% Definir las diagonales que se quieren intercambiar.
dp = 0;
ds = n - dp + 1; % Asegurarme que la dp y ds tengan la misma cantidad de elementos.

% 1er Paso: Guardar todas las posiciones de los elementos de mi matriz.
[i, j] = find(abs(M) >= 0);

% Encontrar las posiciones de los elementos de la dp.
pos_diag_princ = find(dp == j - i);
% Encontrar las posiciones de los elementos de la ds.
pos_diag_sec = find(ds == j + i);

% Hallar los valores de la diagonal principal.
valores_diag_princ = flip(M(pos_diag_princ));

% Hallar los valores de la diagonal secundaria.
valores_diag_sec = flip(M(pos_diag_sec));

% Intercambiar valores.
M(pos_diag_princ) = valores_diag_sec;
M(pos_diag_sec) = valores_diag_princ;

disp(M);

%% Tablero de ajedrez.

% Graficar una matriz.
M = zeros(n);
M(1:2:end, 1:2:end) = ones(3);
M(2:2:end, 2:2:end) = ones(3);
imagesc(M);
colormap('gray');









