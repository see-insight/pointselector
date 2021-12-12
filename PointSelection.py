#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import ipywidgets as widgets
import argparse

#TODO: Add a "done" button. (or something)

#TODO: Remove -f option and require a string as input. 
#TODO:  for example: python PointSelection.py Street.jpg

#TODO: Allow for more than one imageinput (Needs a "done" button)
#TODO:  for example: python PointSelection.py Street.jpg balloonfiesta.jpg

#TODO: Allow for a folder in addition to a name then loop over images in folder.

parser = argparse.ArgumentParser(description='Annotate Point Data')
parser.add_argument('-f', '--file', default='balloonfiesta.jpeg',
                    help="input filename")
# Parsing Inputs
args = parser.parse_args()
filename = args.file

#TODO Fix hard coding of image size
image = cv2.imread(filename)
resized_image = cv2.resize(image, (800,500))
circles = np.zeros((1,2), int)
counter = 0


def detectPoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(circles)
        
# cid = fig.canvas.mpl_connect('button_press_event', detectPoints)

# imgplot = plt.imshow(image)
# plt.show()




half_window = 100
counter = 0
while True:
    if counter == 1:
        #TODO: add if statemetns to make sure index is not less than zero
        template = resized_image[circles[0,1]-half_window:circles[0,1]+half_window, circles[0,0]-half_window:circles[0,0]+half_window, :]
        cv2.imshow("Output Image", template)
        counter = 0
        
    cv2.imshow("Original", resized_image)
    cv2.setMouseCallback("Original", detectPoints)
    cv2.waitKey(1)

    
#TODO: Export point locations as a file
#TODO:  ex:  Street.png  10 20 Corner_of_Eye
#            Street.png  399 19 Nose_tip

# Simple example:
#    10 20 point1
#    399 19 point2

# if __name__ == "__main__":

