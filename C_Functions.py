#Echo con Geminy :c
def move_to(target_x, target_y):
    # Ajustar posición en X
    while get_pos_x() != target_x:
        if get_pos_x() < target_x:
            move(East)
        else:
            move(West)
            
    # Ajustar posición en Y
    while get_pos_y() != target_y:
        if get_pos_y() < target_y:
            move(North)
        else:
            move(South)