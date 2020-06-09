"""
Recorrido del laberinto 
______________________________________

Yeimer Serrano        20181020060
Juan David Rosero     20181020071
Maria Fernanda Uribe  20172020110

"""
#pos[filas],[columnas]
def laberinto():
#Lectura de archivos 
  return [line.split() for line in open("laberinto.txt" , "r").readlines()]

def mostrar_laberinto(laberinto):
  print("Laberinto a explorar\n")
  for i in range (len(laberinto)):
    print (laberinto[i]) 

def buscar_x(laberinto):
  print("\nTu posición inicial es:")
  for i in range (len(laberinto)):
    try:
      return [i,laberinto[i].index("X")]
    except ValueError:
      continue

#modo 1 (avazaar), modo 2 (regresar)
def buscar(laberinto, recorrido,pos,posInicial,modo):
    if modo ==1 and len(recorrido)==0:
        if(len(buscador_camino(pos, laberinto, [], 4))==1):
            if buscador_camino(pos, laberinto, [], 4)[0][0]> pos[0]:
               return buscar(laberinto,[pos],[pos]+avnzar(pos, laberinto, -2) ,[],1)
            elif buscador_camino(pos, laberinto, [], 4)[0][0]< pos[0]:
               return buscar(laberinto,[pos],[pos]+avnzar(pos, laberinto, 2) ,[],1)
            elif buscador_camino(pos, laberinto, [], 4)[0][1]> pos[1]:
               return buscar(laberinto,[pos],[pos]+avnzar(pos, laberinto, 1) ,[],1)
            elif buscador_camino(pos, laberinto, [], 4)[0][1]< pos[1]:
               return buscar(laberinto,[pos],[pos]+avnzar(pos, laberinto, -1) ,[],1)
        #Llego a una pared
        elif len(buscador_camino(pos, laberinto, [], 4))==1 and len(recorrido)!=0:
            return buscar(laberinto,recorrido,pos,posInicial,2)
        elif len(buscador_camino(pos, laberinto, [], 4))==2:
            #Que siga por la linea en la que va (tiene que confirmar que no se encuentre en recorrido)
        
        elif len(buscador_camino(pos, laberinto, [], 4))>2:
            #Tiene que guardar la posicion en la que se encuentra
            
        elif [pos[0],pos[1]+1]=="Y" or [pos[0],pos[1]-1]=="Y" or [pos[0]+1,pos[1]]=="Y" or [pos[0]-1,pos[1]]=="Y":
            #Ya llegó a la Y
            return recorrido
            
            
    elif modo==2:
        if [pos[0],pos[1]-1]==posInicial:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, -1),posInicial,1)
        elif[pos[0],pos[1]+1]== posInicial:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, 1),posInicial,1)
        elif [pos[0]+1,pos[1]]==posInicial:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, -2),posInicial,1)
        elif[pos[0]-1, pos[1]]==posInicial:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, 2),posInicial,1)
        #Si aún no ha llegado
        elif posInicial[0]> pos[0] and posInicial[1]==pos[1]:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, -2),posInicial,2)
        elif posInicial[0]< pos[0] and posInicial[1]==pos[1]:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, 2),posInicial,2)
        elif posInicial[1]> pos[1] and posInicial[0]==pos[0]:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, 1),posInicial,2)
        elif posInicial[1]< pos[1] and posInicial[0]==pos[0]:
            return buscar(laberinto, recorrido+[pos],avnzar(pos, laberinto, -1),posInicial,2)
        
def buscador_camino(pos, tablero,caminos,numero):
    if numero==4:
         if tablero[pos[0]+1,pos[1]]=="0":
             return  buscador_camino(pos,tablero,caminos+[pos[0]+1,pos[1]],3)
         else:
             return buscador_camino(pos,tablero,caminos,3)
    elif numero==3:
        if  tablero[pos[0],pos[1]+1]=="0":
            return  buscador_camino(pos,tablero,caminos+[pos[0],pos[1]+1],2)
        else:
            return buscador_camino(pos, tablero, caminos, 2)
    elif numero==2:
        if tablero[pos[0]-1,pos[1]]=="0":
            return buscador_camino(pos, tablero, caminos+[pos[0]-1,pos[1]],1)
        else:
            buscador_camino(pos, tablero, caminos, 1)
    elif numero==1:
         if tablero[pos[0],pos[1]-1]=="0":
             return buscador_camino(pos, tablero, caminos + [pos[0],pos[1]-1],0)
         else:
             return buscador_camino(pos, tablero, caminos, 0)
    elif numero==0:
        return caminos
    
def isIn(lista,elemento):
    if len(lista)==0:
        return False
    elif lista[0]==elemento:
        return True
    else:
        isIn(lista[1:],elemento)
def avnzar(pos, laberinto,direccion):
    #1 derecha,-1 izquierda,2 arriba,-2 abajo
    if direccion ==1:
        return [pos[0]+1,pos[1]]
    elif direccion ==-1:
        return [pos[0]-1,pos[1]]
    elif direccion ==2:
        return [pos[0],pos[1]-1]
    elif direccion ==-2:
        return [pos[0],pos[1]+1]

mostrar_laberinto(laberinto())
print(buscar_x(laberinto()))