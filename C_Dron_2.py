import C_Functions
import C_carrotAndTree

size_world_carTree = 16
x_init_carTree_up = 16
y_init_carTree_up = 16

x_init_carTree_down = 16
y_init_carTree_down = 0

def dron_2():    
    change_hat(Hats.Purple_Hat)
    #cosechar Zanahorias y madera Arriba
    C_Functions.move_to(x_init_carTree_up,y_init_carTree_up)
    C_carrotAndTree.plant_all(size_world_carTree)
    
    #cosechar Zanahorias y madera Abajo
    C_Functions.move_to(x_init_carTree_down,y_init_carTree_down)
    C_carrotAndTree.plant_all(size_world_carTree)