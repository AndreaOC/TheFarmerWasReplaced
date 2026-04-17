import C_Functions
import C_carrotAndTree
import C_Grass

size_world_carTree = 16
x_init_carTree_down = 16
y_init_carTree_down = 0

size_world_grass = 16
x_init_grass = 0
y_init_grass = 0

def do():
    
    change_hat(Hats.Tree_Hat)
    #cosechar Zanahorias y madera Abajo
    for i in range(7):
        C_Functions.move_to(x_init_carTree_down,y_init_carTree_down)
        C_carrotAndTree.plant_all(size_world_carTree)  
    
    change_hat(Hats.Purple_Hat)
    #Cosechar Eno
    for i in range (4):
        C_Functions.move_to(x_init_grass,y_init_grass)
        C_Grass.harvest_all(size_world_grass)
            
    
       
    