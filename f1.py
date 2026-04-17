def harvest_column(message):
    for _ in range(get_world_size()):
        harvest()
        move(North)
    print(message)

i = 0
while True:
    if spawn_drone(harvest_column, i):
        move(East)
        i = (i + 1) % 10