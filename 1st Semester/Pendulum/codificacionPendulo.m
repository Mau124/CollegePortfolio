%% Inicialización

clear 
close all
clear vars

%Constantes
l = 0;
while l <= 0
disp('Introduzca un valor positivo para el largo del pendulo')
l = input('¿Cuál será el largo del péndulo?');
end

m = 0;
while m <= 0
disp('Introduzca un valor positivo para la masa')
m = input('¿Cuánta será su masa?');
end

num = 0;
while num <= 0
disp('Introduzca un valor positivo para las oscilaciones') 
num = input('¿Cuántas oscilaciones desea?');
end
      
    
  

g = 9.81;
w = sqrt(g/l);
P = (2*pi)/w;
theta = 20;
A = l*sind(theta);
h = (l-l*cosd(theta));
osc = num * P;

%Vector de tiempo
t = 0:0.1:osc;

%Ecuaciones de posición, velocidad y aceleración
Fs = @(t)  A.*cos(w.*t + 0);
Fv = @(t) -A.*w.*sin(w.*t + 0);
Fa = @(t) -A.*w.^2.*cos(w.*t +0);

s = Fs(t);
v = Fv(t);
a = Fa(t);

% Aproximación con trapecio
Npoints = length(t);
a = 0;
b = osc;
x_p = t;
Vx_p = Fv(x_p);

Sa = zeros(size(t));
Sa(1) = s(1);
for i=2:Npoints-1
    ai = x_p(i);
    bi = x_p(i+1);
    
    fai = Vx_p(i);
    fbi = Vx_p(i+1);
    
    Ai = (fbi+fai) * (bi-ai)/2;
    
    Sa(i) = Sa(i-1) + Ai;
    
end
ai = x_p(i);
        bi = x_p(end);
    
        fai = Vx_p(end-1);
        fbi = Vx_p(end);
    
        Ai = (fbi+fai) * (bi-ai)/2;
        
Sa(end) = Sa(end-1)+Ai;
        

% Ecuaciones de la energía potencial y cinética
EK = @(v) (1/2).*m.*v.^2;
eK = EK(v);
eU = m*g*h;
E = eU;

FU = @(t) E.*(cos(w.*t)).^2; 
FK = @(t)  E.*(sin(w.*t)).^2;

U = FU(t);
K = FK(t);

% Creando figura para ejes de graficación
figure("Name", "Simulacion péndulo simple", "NumberTitle", "off");
pendulum = subplot(3,2,[1,3,5]);
posicion = subplot(3,2,2);
velocidad = subplot(3,2,4);
energia = subplot(3,2,6);

% Graficación de los distintos datos
title(pendulum,'Simulacion del pendulo');
xlim(pendulum, [-A-1, A+1]);
ylim(pendulum, [-l, 0]);
xlabel(pendulum, 'S(t)')
ylabel(pendulum, 'h')

title(posicion, 'S(t)');
xlim(posicion, [0, osc]);
ylim(posicion, [-A, A]);
xlabel(posicion, 't')
ylabel(posicion, 'S')

title(velocidad, 'V(t)');
xlim(velocidad, [0, osc]);
ylim(velocidad, [-A*w, A*w]);
xlabel(velocidad, 't')
ylabel(velocidad, 'V')

title(energia, 'E(t)');
xlim(energia, [0, osc]);
ylim(energia, [0, E+1]);
xlabel(energia, 't')
ylabel(energia, 'E')

posi = animatedline(posicion, 'Color', 'r');
veloci = animatedline(velocidad, 'Color', 'm');
energia_cinetica = animatedline(energia, 'Color', 'g');
energia_potencial = animatedline(energia,'Color', 'r');
pend = animatedline(pendulum,'Marker','o','MarkerFaceColor', 'b', 'MarkerSize', 10);
legend('Energia cinetica','Energia potencial');

for k = 1:length(t)
       addpoints(posi, t(k), s(k));
       addpoints(veloci, t(k), v(k));
       addpoints(energia_cinetica, t(k),K(k));
       addpoints(energia_potencial, t(k), U(k));
       addpoints(pend, s(k), -1*sqrt((l.^2)-(s(k).^2)));
       addpoints(pend, [0;s(k)],[0;-1*sqrt((l.^2)-(s(k).^2))])
       pause(.1);
       cla(pendulum);
       pendulum = subplot(3,2,[1,3,5]);
       pend = animatedline(pendulum,'Marker','o','MarkerFaceColor', 'b', 'MarkerSize', 10); 
       
end

close all

% Graficación de la posición aproximada contra la posición exacta
hold on
plot(t, s, 'Color', 'r')
xlabel('Tiempo (t)')
ylabel('Posición (s)')
plot(t, Sa, 'Color', 'b')
legend('Posición exacta','Posición Aproximada')
hold off






