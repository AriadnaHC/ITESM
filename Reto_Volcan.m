function[]=Proyectiles(v0min,v0max,umin,umax,k,n)
    %Programación de trayectorias de proyectiles
    %Declaración de variables
    v0=randi([v0min v0max],1,n);
    v=randi([0 360],1,n);
    u=randi([umin umax],1,n);
    m=randi([1 50],1,n);
    g=9.81;
    dt=0.5;
    
    %Inicializar gráfico
    figure
    grid on
    hold on
    view(3)
    c=gca;
    c.Position(3)=0.6;
    cx=annotation('textbox',[0.8, 0, 0.1, 0.1],'String', "");
    cy=annotation('textbox',[0.8, 0.15, 0.1, 0.1],'String', "");
    cz=annotation('textbox',[0.8, 0.3, 0.1, 0.1],'String', "");
    cvx=annotation('textbox',[0.8, 0.45, 0.1, 0.1],'String', "");
    cvy=annotation('textbox',[0.8, 0.6, 0.1, 0.1],'String', "");
    cvz=annotation('textbox',[0.8, 0.75, 0.1, 0.1],'String', "");

    %Crear valores de trayectorias
    for i=1:length(v0)
        dx=0;
        x=0;
        y=0;
        z=6000;
        vr=v(i)*pi/180;
        ur=u(i)*pi/180;
        vx=v0(i)*cos(ur);
        vz=v0(i)*sin(ur);
        mi=m(i);

        %Graficar
        while z>0
        plot3(x,y,z,".")
        dx = dx + vx * dt;
        x = dx*cos(vr);
        y = dx*sin(vr);
        z = z+vz*dt;
        vx = vx+(-k*vx/mi)*dt;
        vxx=vx*cos(vr);
        vxy=vx*sin(vr);
        vz=vz+(-mi*g-k*vz)/mi*dt;

        set(cx,'String',"x = "+num2str(x))
        set(cy,'String',"y = "+num2str(y))
        set(cz,'String',"z = "+num2str(z))
        set(cvx,'String',"vx = "+num2str(vxx))
        set(cvy,'String',"vy = "+num2str(vxy))
        set(cvz,'String',"vz = "+num2str(vz))
        drawnow;
        end
    end
end