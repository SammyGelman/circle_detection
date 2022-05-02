#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import imageio

def spore_mushrooms(spore_table, n_spores, max_radius):
    length = len(spore_table)
    width = len(spore_table[0])

    len_range = np.linspace(0, length - 1, length).astype(int)
    len_width = np.linspace(0, width - 1, width).astype(int)

    spored = 0
    holder = 0.1
    idx_radius = (max_radius - 1)

    while spored < n_spores:
        spore = True
        prop_x = np.random.choice(len_range)
        prop_y = np.random.choice(len_width)

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
                        break
        if spore:
            for i in x_range:
                for j in y_range:
                    if i >= 0 and j >=0 and i < length and j < width:
                        spore_table[i,j] = holder
            spore_table[prop_x,prop_y] += 1
            spored += 1

    spore_table -= holder
    return spore_table

def map_spores(growing_table, spore_table, spore_length, spore_width, max_radius):
    for i in range(spore_length):
        for j in range(spore_width):
            growing_table[i+max_radius,j+max_radius] = spore_table[i,j]
    return growing_table

def grow_mushrooms(growing_table, max_radius, min_radius):
    length = len(growing_table)
    width = len(growing_table[0])
    output = np.zeros((length, width))
    num_mushrooms = 0
    base = max_radius - min_radius
    for i in range(length):
        for j in range(width):
            if growing_table[i,j] == 1:
                rand_shape = np.random.random()
                if rand_shape >= 0.25:
                    r = round(np.random.random()*(base - 1) + 1) + min_radius
                    num_mushrooms += 1
                    cv2.circle(output,(i,j),r,1,-1)
                else:
                    h = round(np.random.random()*(max_radius - 1) + 1)
                    w = round(np.random.random()*(max_radius - 1) + 1)
                    cv2.rectangle(output,(i,j),(i+h,j+w),1,-1)
    return output, num_mushrooms

def generate_data(max_radius, min_radius, max_mushrooms, length, width, n_samples):
    spore_length = length - 2*max_radius
    spore_width = width - 2*max_radius
   
    bank = []
    num_mushrooms = 0

    for i in range(n_samples):
        spore_table = np.zeros((spore_length, spore_width))
        growing_table = np.zeros((length,width))
        n_spores = round(max_mushrooms*np.random.random())
        spore_mushrooms(spore_table, n_spores, max_radius)

        map_spores(growing_table,
                spore_table,
                spore_length,
                spore_width,
                max_radius)
        
        sample, num_mushrooms = grow_mushrooms(growing_table, max_radius, min_radius)
        
        #normalize sample and convert to unit8
        sample_n = cv2.normalize(src=sample, 
                                dst=None, 
                                alpha=0, 
                                beta=255, 
                                norm_type=cv2.NORM_MINMAX, 
                                dtype=cv2.CV_8U)
        
        filename = '../tests/test_'+str(i)+'.jpeg'
        
        #save array to jpeg image in correct folder
        imageio.imwrite(filename, sample_n)
        bank.append(str(num_mushrooms))
    return bank

def gen_test_txt(bank):
    # open the output file for writing. This will delete all existing data for
    # that address
    with open('../ref_txt/test.txt', 'w') as f:
        for i in range(len(bank)):
            for item in bank[i]:
                f.write(str(item) + " ")
            f.write("\n")


bank = generate_data(40, 15, 12, 500, 500, 1000)
gen_test_txt(bank)

