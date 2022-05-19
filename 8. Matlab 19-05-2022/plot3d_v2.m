n = input('Limíte de los ejes: ');

ejex = xv - n:1:xv + n; % Un vector (xv-n,xv+n) con paso de 1.
ejey = yv - n:1:yv + n; % Un vector (xv-n,xv+n) con paso de 1.

f = input('Digite una función que depende de X y Y: ')
[X, Y] = meshgrid(ejex, ejey);
Z = f(X, Y);
mesh(X, Y, Z);
