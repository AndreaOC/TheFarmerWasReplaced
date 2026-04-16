def create_maze():
    clear()
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)
    
create_maze()

#if get_entity_type() == Entities.Treasure:
#    harvest()
#else

    

    
