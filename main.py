import C_Functions
import C_Dron_1
import C_Dron_2
import C_Dron_3
import C_Dron_4

C_Functions.move_to(0,0)
pet_the_piggy()

while True:
    #Cosechar Calabazas
    C_Functions.move_to(0,16)
    spawn_drone(C_Dron_3.do) 
    #Cosechar Zanahorias y Madera abajo
    C_Functions.move_to(16,0)
    spawn_drone(C_Dron_4.do)
    #Cosechar Heno y Cactus
    C_Functions.move_to(0,0)
    spawn_drone(C_Dron_1.do)  
    #Cosechar Zanahorias y Madera arriba
    C_Functions.move_to(16,16)
    C_Dron_2.do()
    
    