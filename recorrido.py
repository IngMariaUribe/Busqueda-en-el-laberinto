def laberinto():
    return [line.split() for line in open("laberinto.txt" , "r").readlines()]


def imprimirLab(laberinto):
    for i in range(len(laberinto)):
        print(laberinto[i])

def busqueda(laberinto):
    for i in range(len(laberinto)):
        try:
            return [i,laberinto[i].index("X")]
        except ValueError:
            continue
        
def busqueda_y(laberinto):
    for i in range(len(laberinto)):
        try:
            return [i, laberinto[i].index("Y")]
        except ValueError:
            continue

def camino(inicio, final, laberinto, recorrido):
    print(inicio)
    while(True):
        if(inicio == final):
            break
        else: 
            #Este if recorre hacia abajo
            if ((inicio[0]< len(laberinto) and inicio[0] + 1 < len(laberinto)) and (laberinto[inicio[0] + 1][inicio[1]] == "1" or laberinto[inicio[0] + 1][inicio[1]] == "Y") and inicio not in recorrido):
                if(laberinto[inicio[0]][inicio[1] + 1] == "Y" or laberinto[inicio[0]][inicio[1] - 1] == "Y"):
                    break
                else:
                    return camino([inicio[0] + 1, inicio[1]], final, laberinto, recorrido.append(inicio))
            #Este if recorre hacia la derecha
            if ((inicio[1] < len(laberinto[0]) and inicio[1] + 1 < len(laberinto[0])) and (laberinto[inicio[0]][inicio[1] + 1] == "1" or laberinto[inicio[0]][inicio[1] + 1] == "Y") and inicio not in recorrido):
                if(laberinto[inicio[0] - 1][inicio[1]] == "Y" or laberinto[inicio[0] + 1][inicio[1]] == "Y"):
                    break
                else:
                    return camino([inicio[0], inicio[1] + 1], final, laberinto, recorrido)
            #Este if va hacia arriba
            if ((inicio[0] < len(laberinto) and inicio[0] - 1 < len(laberinto)) and (laberinto[inicio[0] - 1][inicio[1]] == "1" or laberinto[inicio[0] - 1][inicio[1]] == "Y") and inicio not in recorrido):
                if(laberinto[inicio[0]][inicio[1] - 1] == "Y" or laberinto[inicio[0]][inicio[1] + 1] == "Y"):
                    break
                else:
                    return camino([inicio[0] - 1, inicio[1]], final, laberinto, recorrido)
            #Este if va hacia izquierda
            if ((inicio[1] > 0 and inicio[1] - 1 > 0) and (laberinto[inicio[0]][inicio[1] - 1] == "1" or laberinto[inicio[0]][inicio[1] - 1] == "Y") and inicio not in recorrido):
                if(laberinto[inicio[0] - 1][inicio[1]] == "Y" or laberinto[inicio[0] + 1][inicio[1]] == "Y" or laberinto[inicio[0]][inicio[1] - 1] == "Y"):
                    break
                else:
                    return camino([inicio[0], inicio[1] - 1], final, laberinto, recorrido)
        #print("rerco ", recorrido)


imprimirLab(laberinto())
print("Posicion X: ", busqueda(laberinto()))
print("Posicion Y: ", busqueda_y(laberinto()))
camino(busqueda(laberinto()), busqueda_y(laberinto()), laberinto(), [])
