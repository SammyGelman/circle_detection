#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle

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
    print(growing_table.shape)
    print(spore_table.shape)
    return growing_table

def grow_mushrooms(growing_table, max_radius):
    length = len(growing_table)
    width = len(growing_table[0])
    output = np.zeros((length, width))
    for i in range(length):
        for j in range(width):
            if growing_table[i,j] == 1:
                r = round(np.random.random()*(max_radius - 1) + 1)
                cv2.circle(output,(i,j),r,1,-1)
    return output

def generate_data(max_radius, max_mushrooms, length, width, n_samples):
    bank = []
    spore_length = length - 2*max_radius
    spore_width = width - 2*max_radius

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

        bank.append(grow_mushrooms(growing_table, max_radius))

    with open('mushrooms.pkl', 'wb') as f:
        pickle.dump(bank, f)

generate_data(14, 8, 200, 100,10)

