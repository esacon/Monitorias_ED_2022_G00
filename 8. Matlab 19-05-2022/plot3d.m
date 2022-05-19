xv = 7;
yv = -3;

n = input('Limíte de los ejes: ');

ejex = xv - n:1:xv + n; % Un vector (xv-n,xv+n) con paso de 1.
ejey = yv - n:1:yv + n; % Un vector (xv-n,xv+n) con paso de 1.

f = @(x, y) y - yv - abs(x - xv);
[X, Y] = meshgrid(ejex, ejey);
Z = f(X, Y);
mesh(X, Y, Z);

x = 1:1/pi:10;
subplot(121) % num_filas num_col num_fig
plot(x, sin(x))
subplot(122)
plot(x, cos(x))

