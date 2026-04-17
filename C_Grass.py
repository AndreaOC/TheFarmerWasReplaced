#Cosecha todo
def move_harvest(n, dir):   
    for i in range(n):
        if can_harvest():
            harvest()        
        move(dir)    
            
def harvest_all(size):
    for i in range(size/2):
        move_harvest(size - 1, North)
        move_harvest(1, East)
        move_harvest(size - 1, South)
        move_harvest(1, East)
        
#prepara el terreno para cosechar Eno
def move_check(n, dir):
    for i in range(n):            
        if get_ground_type() == Grounds.Soil:
            till() 
        move(dir)    
                
def check_ground(size):
    for i in range(size/2):
        move_check(size - 1, North)
        move_check(1, East)
        move_check(size - 1, South)
        move_check(1, East)


    