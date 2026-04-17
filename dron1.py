import C_Functions
import C_Pumpkin

size_pumpkin = 16
x_init_pumpkin = 0
y_init_pumpkin = 0

#cosechar Calabazas
C_Functions.move_to(x_init_pumpkin,y_init_pumpkin)
C_Pumpkin.plant_pumpkin(size_pumpkin)
C_Functions.move_to(x_init_pumpkin,y_init_pumpkin)
C_Pumpkin.harvest_pumpkin()

#Cosechar Eno y cactus

