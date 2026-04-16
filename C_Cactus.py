import C_Functions

def move_plant(n, dir):
    for i in range(n):            
        if get_ground_type() == Grounds.Soil:
            plant(Entities.Cactus)
        else:            
            harvest()
            till()
            plant(Entities.Cactus)
        move(dir)    
#Plantar Cactus        
def plant_cactus():
        move_plant(2, North)
        move_plant(1, East)
        move_plant(2, South)
        move_plant(1, East)
        move_plant(2, North)
        move_plant(1, East)

#Echo con Gemini :c
#Escanear el área 3x3
def mapear_cactus():
    lista_cactus = []
    for x in range(3):
        for y in range(3):
            C_Functions.move_to(x, y)
            tamano = measure() # Obtiene el tamaño del cactus
            lista_cactus.append([tamano, x, y])
    return lista_cactus

#Cosecha selectiva y re-siembra (Más eficiente que ordenar)
def cosecha_selectiva():
    # Solo se ejecutará 5 veces
    for ciclo in range(10): 
        # 1. Encontrar el cactus más pequeño actualmente en el campo 3x3
        min_val = 999999
        best_x, best_y = -1, -1
        
        for x in range(3):
            for y in range(3):
                C_Functions.move_to(x, y)
                
                # Si la celda está vacía, plantamos uno nuevo
                if get_entity_type() == None: 
                    plant(Entities.Cactus)
                
                valor = measure()
                # Consideramos solo cactus válidos
                if valor != None and valor < min_val:
                    min_val = valor
                    best_x, best_y = x, y
        
        # 2. Ir al cactus más pequeño encontrado y cosecharlo
        if best_x != -1:
            C_Functions.move_to(best_x, best_y)
            harvest()
            plant(Entities.Cactus)
    
#Cosechar cactus
def harvest_cactus():
    for i in range(9):
        C_Functions.move_to(i % 3, i // 3)
        harvest()
    