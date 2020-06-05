"""
Recorrido del laberinto 
______________________________________

Yeimer Serrano        20181020060
Juan David Rosero     20181020071
Maria Fernanda Uribe  20172020110

"""

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


"""
 def buscar(laberinto, lista, po,posibles):
    #0 se puede pasar, 1 no se puede
    Tareas:
      0. si encuentra  "Y" se debe romper la función
      1. Buscar el 0 mas cercano
      2. confirmar que la posicion de ese uno no se encuentre en la lista
      3. repetir
      4. No regresar por donde no 
      -
"""
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

mostrar_laberinto(laberinto())
print(buscar_x(laberinto()))