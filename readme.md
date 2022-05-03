Circle Detection

This document will give a walk through of the code and what each of the scripts do and how they work. 

For more general information on the project, motivations and methodologies, refer to the pdf document located at lyx_docs/circle_detection.pdf

The document will proceed by going through each of the files in the scripts directory and describing the functions present.

mushroom_data, rectangle_data, test_data:

These three scripts work very similarly so I will describe the functions present in all of them together. 
	
spore_mushrooms(spore_table, n_spores, max_radius):
	
	This function creates a 2_d square lattice of value zero. Then it chooses points which will mark the center of the shapes that will be drawn later by changing the value of that lattice site to one. These location are chosen randomly and locations will not be chosen if a potential overlap of shapes would occur. For this reason it is important not to "stuff" to many mushrooms onto a sample or else the algorithm will search a long time for possible configurations. A wall time could be added.
	The spore_table parameter decides the size of the 2-d lattice. 
	n_spores determines how many shapes will be put onto the lattice.
	max_radius determines the maximum radius the circles could shapes.
	
	The function returns the updated spore_table object which holds the location of the centers of the shape. This object is smaller than the final sample images to be created. This table will be mapped onto the full sized lattice.

map_spores(growing_table, spore_table, spore_length, spore_width, max_radius):

	The growing table is the 2d array that will be returned from the script. The spore_table is the output from the spore_mushrooms function. The spore_length and spore_width are the sizes of the spore_table, this could be have been taken from the spore_table but for a reason I can't now recall I did not do that. The max_radius is the additional metric needed to properly map the points from teh spore_table to the growing table. 

grow_mushrooms(growing_table, max_radius, n_spores)

	This script will grow the circles to a variable size. The script was updated in the test.py to include a min_radius arguments as well. The n_spores but could have been gathered by summing th growing table. 
	Shapes will be picked to grow to random sizes based off of there restrictions. For the circles a variable called coor will list all of the radii of the circles as well as the coordinated needed to create a boudning box around them. This will be saved to a text file called pos.txt and is used in the training of certain machine learning algorithms. In our case the Haar Cascade. 

generate_data(max_radius, max_mushrooms, length, width, n_samples):
	Finally, generate data is used to generate all of the samples by passing arguments for the size of the output image, the max number of shapes to put on each image, the max_radius of the shapes and the number of samples to be saved. 	The samples are saved to either the positives/, negatives/, or tests/ directories as numbered .jpeg files. 
	This file also outputs a file called bank, which has all of the coordinateed for the circles and their bounding rectangles for each sample. This is returned from the function as the variable named 'bank' and passed to another function called gen_pos_txt(bank) to save the above mentioned text file. 

hough_circle.py:

This finle has a single function which is our implementation of the hugh circle algorithm. The function accepts an image as well as other function specific parameters that have the optimized values found for this project saved as their defaults. 

The function will output a picture of the image before and after the algorithm found it's candidates for the location of the cirlces. By pressing 'q' on your key board the image will be cleared. 

diagnosis.py:

This script will test the algorithm based off of the data generated into the tests/ directory. 

It will give an accuracy score described in the pdf. 

