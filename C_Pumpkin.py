def move_plant(n, dir):
    for i in range(n):            
        if get_ground_type() == Grounds.Soil:
            while can_harvest() == False:
                plant(Entities.Pumpkin)
                use_item(Items.Water)
                do_a_flip()
        else:            
            harvest()
            till()
            while can_harvest() == False:
                plant(Entities.Pumpkin)
                use_item(Items.Water)
                do_a_flip()    
        move(dir)    
            
def plant_pumpkin(size):
    for i in range(size/2):
        move_plant(size - 1, North)
        move_plant(1, East)
        move_plant(size - 1, South)
        move_plant(1, East)
        
def plant_pumpkin_reverse(size):
    for i in range(size/2):
        move_plant(size - 1, South)
        move_plant(1, West)
        move_plant(size - 1, North)
        move_plant(1, West)
            
def harvest_pumpkin():
    do_a_flip()
    harvest()
    


    