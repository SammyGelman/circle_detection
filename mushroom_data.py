import numpy as np
import matplotlib.pyplot

def spore_mushrooms(max_radius, n_mushrooms, length, width):
    growing_table = np.zeros((length,width))
    
    v_length = length-max_radius 
    v_width = width-max_radius

    

    viable_mushroom_spots = np.zeros((v_length, v_width))

    for i in range(n_mushrooms):
        


