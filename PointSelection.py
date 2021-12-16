#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import ipywidgets as widgets
import argparse


def detectPoints(event,x,y,flags,params):
    global circles
    global stop
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append([x,y])
    if event == cv2.EVENT_RBUTTONDOWN:
        stop = True

def pickpoints(image, n=9999):
    global circles
    global stop
    circles = []
    stop = False
    half_window = 100
    while stop == False:
        for point in circles:
            cv2.circle(image,(point[0], point[1]),3,(0,255,0),cv2.FILLED)    
        cv2.imshow("Point Picker", image)
        cv2.setWindowProperty("Point Picker", cv2.WND_PROP_TOPMOST, 1)
        cv2.setMouseCallback("Point Picker", detectPoints)
        cv2.waitKey(1)
        if len(circles) >= n:
            stop = True
    
    for point in circles:
        print(f"{point[0]}, {point[1]}")
    cv2.destroyWindow("Point Picker")
    return circles
        
#TODO: Add a "done" button. (or something)

#TODO: Remove -f option and require a string as input. 
#TODO:  for example: python PointSelection.py Street.jpg

#TODO: Allow for more than one imageinput (Needs a "done" button)
#TODO:  for example: python PointSelection.py Street.jpg balloonfiesta.jpg

#TODO: Allow for a folder in addition to a name then loop over images in folder.

#TODO: Move argparse stuff into a __name__=="__main__" section

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Annotate Point Data')
    parser.add_argument('-f', '--file', default='balloonfiesta.jpeg',
                        help="input filename")
    parser.add_argument('-n', '--number', default=9999,
                        help="number of points to select")
    # Parsing Inputs
    args = parser.parse_args()
    filename = args.file

    #TODO Fix hard coding of image size
    image = cv2.imread(filename)
    resized_image = cv2.resize(image, (800,500))
    pickpoints(resized_image, int(args.number))
    
        
        
        
        
        
        
        
