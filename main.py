import C_Functions
import C_Dron_1
import C_Dron_2

C_Functions.move_to(0,0)
pet_the_piggy()

while True:
    #Cosechar Heno y Cactus
    spawn_drone(C_Dron_1.dron_1)
    #Cosechar Calabazas
    C_Functions.move_to(16,16)
    C_Dron_2.dron_2()
    
    