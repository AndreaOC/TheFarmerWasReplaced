import C_Functions
import C_Grass
import C_Cactus
import C_Pumpkin

size_world_grass = 16
x_init_grass = 0
y_init_grass = 0

x_init_cactus = 0
y_init_cactus = 0

size_world_pumpkin = 16
x_init_pumpkin = 15
y_init_pumpkin = 31



def do(): 
    
    change_hat(Hats.Cactus_Hat)
    
    #cosechar cactus
    for i in range(5):
        C_Functions.move_to(x_init_cactus,y_init_cactus)
        C_Cactus.plant_cactus()
        do_a_flip()
        #Seleccion y ordenamiento
        C_Functions.move_to(x_init_cactus,y_init_cactus)
        C_Cactus.cosecha_selectiva()
        C_Cactus.harvest_cactus()
    
    #Cosechar Eno 
    #C_Functions.move_to(x_init_grass,y_init_grass)
    #C_Grass.check_ground(size_world_grass)
    C_Functions.move_to(x_init_grass,y_init_grass)
    C_Grass.harvest_all(size_world_grass)
    C_Functions.move_to(x_init_grass,y_init_grass)
    C_Grass.harvest_all(size_world_grass)
    
    change_hat(Hats.Pumpkin_Hat)
    C_Functions.move_to(x_init_pumpkin,y_init_pumpkin)
    C_Pumpkin.plant_pumpkin_reverse(size_world_pumpkin)
    
    
    




