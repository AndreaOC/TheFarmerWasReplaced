import C_carrotAndTree
import C_Pumpkin
import C_Grass
import C_Cactus
import C_Functions

C_Functions.move_to(0,0)
pet_the_piggy()
change_hat(Hats.Pumpkin_Hat)

while True:   

    #Cosechar Cactus
    for i in range(5):
        C_Functions.move_to(0,0)
        C_Cactus.plant_cactus()
        do_a_flip()
        #Seleccion y ordenamiento
        C_Cactus.cosecha_selectiva()
        C_Cactus.harvest_cactus()
        
    C_Functions.move_to(0,0)
    
    #Cosechar Zanahorias y Madera
    C_carrotAndTree.plant_all(get_world_size())
    C_carrotAndTree.harvest_all(get_world_size())
    
    #Cosechar Calabazas
    C_Pumpkin.plant_pumpkin(get_world_size())
    C_Pumpkin.harvest_pumpkin()
    
    #Cosechar Zanahorias y Madera
    C_carrotAndTree.plant_all(get_world_size())
    C_carrotAndTree.harvest_all(get_world_size())
    
    #Cosechar Pasto
    clear()
    do_a_flip()
    C_Grass.harvest_all(get_world_size())
    