#!/usr/bin/env python3
from hough_circles import hough_circles
import time

start_time = time.time()

test_file = open('../ref_txt/test.txt')
num_mushrooms = []
delta_mushrooms = 0

for i, line in enumerate(test_file):
    num_mushrooms.append(int(line.replace(" ","")))

for i in range(len(num_mushrooms)):
    img_dir = "../tests/test_"+str(i)+".jpeg"
    found = hough_circles(img_dir)
    delta_mushrooms += abs(num_mushrooms[i] - found)

total_mushrooms = sum(num_mushrooms)
percent_acc = (total_mushrooms - delta_mushrooms) / total_mushrooms * 100
end_time = time.time()

time_per_image = (end_time - start_time)/len(num_mushrooms)
print("Average time to process image (seconds): " + str(time_per_image))
# print(delta_mushrooms)
print("Percent accuracy: " + str(percent_acc))
