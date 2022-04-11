import numpy as np
import matplotlib.pyplot

def spore_mushrooms(spore_table, n_spores, max_radius):
    length = len(spore_table)
    width = len(spore_table[0])

    len_range = np.linspace(0, length - 1, length).astype(int)
    len_width = np.linspace(0, width - 1, width).astype(int)
    
    spored = 0

    idx_radius = (max_radius - 1)
    
    while spored < n_spores:
        spore = True
        prop_x = np.random.choice(len_range)
        prop_y = np.random.choice(len_width)

        holder = 0.1

        x_range = np.linspace(prop_x - idx_radius, 
                              prop_x + idx_radius, 
                              2*idx_radius + 1).astype(int)
        
        y_range = np.linspace(prop_y - idx_radius, 
                              prop_y + idx_radius, 
                              2*idx_radius + 1).astype(int)

        for i in x_range:
            for j in y_range:
                #check to make it is a valid index
                if (i and j) >= 0 and i < length and j < width:
                    if spore_table[i,j] != 0:
                        spore = False    
                        break()
        if spore:
            for i in x_range:
                for j in y_range:
                    if i >= 0 and j >=0 and i < length and j < width:
                        spore_table[i,j] = holder
            spore_table[prop_x,prop_y] += 1
            spored += 1
    
    spore_table -= holder
    return spore_table
def grow_mushrooms(max_radius, n_mushrooms, length, width):
    growing_table = np.zeros((length,width))
   
    spore_length = length-max_radius 
    spore_width = width-max_radius

          

