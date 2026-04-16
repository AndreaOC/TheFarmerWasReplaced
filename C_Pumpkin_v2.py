def move_plant(n, dir):
    for i in range(n):            
        if get_ground_type() == Grounds.Soil:
            while can_harvest() == False:
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)
                use_item(Items.Weird_Substance)

        else:            
            harvest()
            till()
            while can_harvest() == False:
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)
                use_item(Items.Weird_Substance)
        move(dir)    
            
def plant_pumpkin(size):
    for i in range(size/2):
        move_plant(size - 1, North)
        move_plant(1, East)
        move_plant(size - 1, South)
        move_plant(1, East)
            
def harvest_pumpkin():
    do_a_flip()
    harvest()
    