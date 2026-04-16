def move_plant(n, dir):
    for i in range(n):        
        if dir == North:
            if get_pos_y() % 2 == 0:
                if can_harvest():
                    harvest()
                plant(Entities.Tree)
            else:
                if can_harvest():
                    harvest()
                if get_ground_type() == Grounds.Soil:
                    plant(Entities.Carrot)
                else:
                    harvest()
                    till()
                    plant(Entities.Carrot)                
                
        elif dir == South:
            if get_pos_y() % 2 != 0:
                if can_harvest():
                    harvest()
                plant(Entities.Tree)
            else:
                if can_harvest():
                    harvest()
                if get_ground_type() == Grounds.Soil:
                    plant(Entities.Carrot)
                else:
                    harvest()
                    till()
                    plant(Entities.Carrot)            
        move(dir)    
            
def plant_all(size):
    for i in range(size/2):
        move_plant(size - 1, North)
        move_plant(1, East)
        move_plant(size - 1, South)
        move_plant(1, East)


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


    