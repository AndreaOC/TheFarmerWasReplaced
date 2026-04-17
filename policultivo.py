import C_Functions

clear()
set_world_size(9)
plant(Entities.Bush)
companion = get_companion()
plant_type, (x,y) = companion
if companion != None:    
    C_Functions.move_to(x,y)
    plant(plant_type)

pet_the_piggy()
C_Functions.move_to(0,0)
while can_harvest() == False:
    harvest()
    C_Functions.move_to(x,y)
    while can_harvest() == False:
        harvest()
        break

do_a_flip()
do_a_flip()


