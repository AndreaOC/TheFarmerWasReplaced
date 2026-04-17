import C_Functions
import C_carrotAndTree

size_world_carTree = 16
x_init_carTree_up = 16
y_init_carTree_up = 16

def do():    

    change_hat(Hats.Carrot_Hat)
    
    #cosechar Zanahorias y madera Arriba
    C_Functions.move_to(x_init_carTree_up,y_init_carTree_up)
    C_carrotAndTree.plant_all(size_world_carTree)
    
    