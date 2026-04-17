import C_Functions
import C_Pumpkin

size_world_pumpkin = 16
x_init_pumpkin = 0
y_init_pumpkin = 16

def do():
    
    change_hat(Hats.Pumpkin_Hat)
    
    #cosechar Calabazas
    C_Functions.move_to(x_init_pumpkin,y_init_pumpkin)
    C_Pumpkin.plant_pumpkin(size_world_pumpkin)
    C_Functions.move_to(x_init_pumpkin,y_init_pumpkin)
    C_Pumpkin.harvest_pumpkin()
    
