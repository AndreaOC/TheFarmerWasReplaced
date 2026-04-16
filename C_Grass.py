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


    