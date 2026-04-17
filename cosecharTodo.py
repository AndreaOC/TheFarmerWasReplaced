import C_Grass
import C_Functions

change_hat(Hats.Traffic_Cone)

size = get_world_size()
C_Functions.move_to(0,0)
C_Grass.harvest_all(size)