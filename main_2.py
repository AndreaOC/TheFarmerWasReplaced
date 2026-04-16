import C_carrotAndTree
import C_Pumpkin_v2

clear()
pet_the_piggy()
change_hat(Hats.Pumpkin_Hat)

#size = get_world_size()
size = 3

while True:
    #Cosechar Zanahorias y Madera
    #C_carrotAndTree.plant_all(size)
    #C_carrotAndTree.harvest_all(size)
    
    #Cosechar Calabazas
    C_Pumpkin_v2.plant_pumpkin(size)
    C_Pumpkin_v2.harvest_pumpkin()
    
    #Cosechar Zanahorias y Madera
    C_carrotAndTree.plant_all(size)
    C_carrotAndTree.harvest_all(size)