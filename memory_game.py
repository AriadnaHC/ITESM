#Ariadna Huesca Coronado    A01749161
import random
import  time#para contar el tiempo de la partida
tablero=[]
POSICIONES=[]

def iniciar_tablero():
    """
    Funcion para inicializar el tablero y el estado del tablero
    Retorna:Matriz(tablero) y matriz con estados del tablero(si se adivino o no)
    """    
    lista_inicial=[]#valores que puede tomar el tablero    
    estado=[]    
    contador_lista=0#contador de lista    
    for i in range(1,19):
        lista_inicial+=[i,i]    
    random.shuffle(lista_inicial)#revuelve las posiciones
    for i in range(6):
        nuevo=[]
        nuevo2=[]
        for j in range(6):
            nuevo.append(0)
            nuevo2.append(False)
        tablero.append(nuevo)   
        estado.append(nuevo2)    
    for i in range(6):
        POSICIONES.append(i)
        for j in range(6):
            tablero[i][j]=lista_inicial[contador_lista]                    
            contador_lista+=1    
    return tablero,estado

def pedir_nombre_jugadores():
    """
    Pide el nombre de los jugadores, considerando que deben ser diferentes y los regresa
    """
    jugador1=input("jugador 1\n")
    jugador2=input("jugador 2\n")
    while jugador1==jugador2:
        print("error, los jugadores no pueden ser iguales")
        jugador2=input("jugador 2\n")
    return jugador1,jugador2

def comprobar_carta(posicion):
    """
    Determina si una carta es valida(esta dentro del rango y es numerico)
    posicion:Posicion de la carta a evaluar
    Retorna: True si es valida y False de lo contrario
    """
    if(posicion.isnumeric()):
        if(int(posicion)>=0 and int(posicion)<6):
            return True
        else:
            print("Fuera de rango")
            return False
    else:
        print("Inserto un caracter")
        return False
    
def comprobar_disponibilidad(renglon,columna,estado):
    """
    comprueba si la casilla esta disponible(que estado sea False)
    renglon:primer indice de la matriz
    columna:segundo indice de la matriz
    estado:si esta adivinada o no
    Retorna: True si estado en esa posicion es False, False de lo contrario
    """
    if(estado[renglon][columna]):
        print("Casilla ya ocupada")
        return False
    else:
        return True
        
def despliega_instrucciones():
    """
    Lee el archivo instrucciones.txt linea a linea
    """
    archivo=open("instrucciones.txt","r")
    for i in archivo:
        i=i.replace("\n","")
        print(i)
    input("presione enter tecla para regresar al menu\n")

def mostrar_tablero(estado):
    """
    Muestra el tablero en funcion del estado actual
    tablero:matriz con todos los valores de la matriz
    estado:matriz que dice si ya se ha adivinado el dato o no 
    Retorna: None
    """
    for i in range(7):
        for j in range(7):
            if i==0:                
                if j!=0:            
                    print(str(POSICIONES[j-1])+"\t",end="")
                else:
                    print("\t",end="")
            elif j==0:
                print(str(POSICIONES[i-1])+"\t",end="")    
            else:            
                if estado[i-1][j-1]:
                    print(str(tablero[i-1][j-1])+"\t",end="")
                else:
                    print("-\t",end="")
        print("\n")
    
def jugar(carta):    
    """
    Realiza una jugada, pidiendo una renglon y columna, comprobando si es valida
    carta:si es la carta 1 o la 2
    Retorna: el renglon y la columna
    """
    renglon=input("renglon carta {0}: ".format(carta))
    while not comprobar_carta(renglon):
        renglon=input("renglon carta {0}: ".format(carta))
        
    columna=input("columna carta {0}: ".format(carta))
    while not comprobar_carta(columna):    
        columna=input("columna carta {0}: ".format(carta))
    return int(renglon),int(columna)

def termino_partida(estado):
    """
    Revisa si termino la partida
    estado: matriz que contiene si una carta ha sido adivinada ya
    Retorna: True si todos lo sestados son True(termino partida),False de otra forma
    """
    for i in estado:
        for j in i:
            if not j:
                return False
    return True

def quien_gano(jugador1,jugador2,j1,j2):
    """
    Imprime el jugador que gano
    jugador 1: int puntos del jugador 1
    jugador 2: int puntos jugador 2
    """
    print("termino Partida")
    if jugador1>jugador2:
        print("Gano jugador {0} con {1} puntos contra {2} puntos".\
              format(j1,jugador1,jugador2))
    elif jugador1<jugador2:
        print("Gano jugador {0} con {1} puntos contra {2} puntos".\
              format(j2,jugador2,jugador1))
    else:
        print("Empate con {0} puntos".format(jugador2))    

def partida():
    """
    Aqui se llaman todas las funciones necesarias para jugar
    """
    tablero,estado=iniciar_tablero()  
    print(tablero)
    inicio_de_tiempo = time.time()    
    answer="s"
    jugadorTurno=""
    turno=True
    jugador1,jugador2=pedir_nombre_jugadores()
    puntos_jugador_1=puntos_jugador_2=0
    
    while(answer=="s" and not termino_partida(estado)):
        mostrar_tablero(estado)
        if(turno):
            jugadorTurno=jugador1
        else:
            jugadorTurno=jugador2
        print("turno del jugador "+jugadorTurno)
        r,c=jugar("1")
        while not comprobar_disponibilidad(r,c,estado):
            r,c=jugar("1")    
        print("\nelegiste: "+str(tablero[r][c]))                
        r2,c2=jugar("2")
        while not comprobar_disponibilidad(r2,c2,estado) or not (r2!=r or c!=c2):
            if(r2==r and c==c2):
                print("Escogiste la misma de la ronda pasada")
            r2,c2=jugar("2")       
        print("\nelegiste: "+str(tablero[r2][c2]))                
        if tablero[r][c]==tablero[r2][c2]:
            print("par encontrado!")
            if(jugadorTurno==jugador1):
                puntos_jugador_1+=1
            else:
                puntos_jugador_2+=1
            estado[r][c]=True
            estado[r2][c2]=True                    
        else:
            turno=not turno
        answer=input("seguir jugando?s)")
        
    if termino_partida(estado):
        quien_gano(puntos_jugador_1,puntos_jugador_2,jugador1,jugador2)              
        tiempo_final = time.time() 
        tiempo_transcurrido = tiempo_final - inicio_de_tiempo    
        tiempo_transcurrido/=60
        tiempo=str(tiempo_transcurrido)
        print("tiempo de la partida: "+tiempo[:4]+"min")
    else:
        print("usted terminó la Partida")
        print("Puntajes")
        print("Jugador 1: {0} puntos".format(puntos_jugador_1))
        print("Jugador 2: {0} puntos".format(puntos_jugador_2)) 
        

    
def main():
    print("MEMORAMA")
    respuesta=input("1 para jugar,2 para las instrucciones, cualquier otro para salir\n")
    while(respuesta=="1" or respuesta=="2"):
        if(respuesta=="1"):
            partida()
        elif(respuesta=="2"):
            despliega_instrucciones()
        respuesta=input("1 para jugar,2 para las instrucciones, cualquier otro para salir\n")
    print("SALIENDO DEL JUEGO...")
    
    
main()