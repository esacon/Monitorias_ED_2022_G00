%% Funciones en Matlab.

% Para la distribuci�n de Rayleigh se tienen dos par�metros.
% X es un vector 
% Sigma un escalar
% Cuando se realizan operaciones sobre vectores, debe incluirse un . antes
% de la operaci�n. Esto indica que dicha op se realizar� a cada elemento
% del vector.
f = @(x, s) x./s^2.*exp(-x.^2./(2*s^2));

x = 0:1e-03:10;

text = "";
for s=1:10
    text = "sigma= " + s;
    plot(x, f(x, s), "DisplayName", text)    
    hold on
end
grid on
legend


%% Gr�ficos en 3D

x = -2:.2:2;
y = -4:.4:4;
[x, y] = meshgrid(x, y);
z = x.*exp(-x.^2-y.^2);
surf(x,y,z)