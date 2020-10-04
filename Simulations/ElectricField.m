%% Barra de Arriba
[X,Y]=meshgrid([-1.8:.2:1.8]);
x=linspace(-1,1,100);y=.5;
q1=1;
[u,v]=campo(q1,x,y,X,Y);

%% La de abajo
x1=linspace(-1,1,100);y1=-.5;
q2=-1;
[u1,v1]=campo(q2,x1,y1,X,Y);
u1=u1+u
v1=v1+v;
magnitud=(u1.^2+v1.^2).^(1/2);
quiver(X,Y,u1./magnitud,v1./magnitud,"b","LineWidth",2)

hold on
r2 = rectangle('Position',[-1 -.60 2 .19],'Curvature',1);%coordenadas de posicion en plano y dimensiones
grid off
r2.FaceColor = "k";

hold on
r1 = rectangle('Position',[-1 .41 2 .19],'Curvature',1);%coordenadas de posicion en plano y dimensiones
grid off
r1.FaceColor = "r";

axis([-3 3 -3 3])


%% Function
function [u,v] = campo(q1,x,y,X,Y)
    u=[0];v=[0];k=9;
    for i=1:100
        distancia=((X-x(1,i)).^2+(Y-y).^2).^(3/2);
        a=(((X-x(1,i)).*k*q1))./distancia;
        b=((Y-y).*k*q1)./distancia;
        a(isnan(a)|isinf(a))=0;
        b(isnan(b)|isinf(b))=0;
        u= u + a;
        v= v + b;
    end
end
