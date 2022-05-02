#!/usr/bin/env python3
import numpy as np
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("image", help = "Path to the image", type=str)
# ap.add_argument("sample", help = "sample number", type=int)
# args = vars(ap.parse_args())

# sample = args["sample"]
# image = cv2.imread(args["image"])

def hough_circles(img, min_radius=10, max_radius=50, edge_param=250, acceptance_param=13.3, min_Dist=85):
    # load the image, clone it for output, and then convert it to grayscale
    image = cv2.imread(img)
    # max_radius = round(len(image[0])/4)
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect circles in the image
    circles = cv2.HoughCircles(gray,
                               cv2.HOUGH_GRADIENT,
                               dp=0.5,
                               minDist=min_Dist,
                               param1=edge_param,
                               param2=acceptance_param, 
                               minRadius=min_radius,
                               maxRadius=max_radius)

    # # edge display to check param1 value choice 
    # edges = cv2.Canny(image,100,100)
    # plt.subplot(121),plt.imshow(image,cmap = 'gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # ensure at least some circles were found
    if circles is not None:	
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles[0]:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        
        # show the output image
        cv2.imshow("output", np.hstack([image, output]))
        cv2.waitKey(0)
    
        return len(circles[0])
    else:
        return 0
