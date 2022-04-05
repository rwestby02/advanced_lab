import numpy as np
import cv2 as cv
import matplotlib
from skimage import io

#print("image filepath")  #trying to ensure that the r to make raw strings is added to an inputted string, windows problem
#image_loc = input()

#print(image_loc)

image_input = io.imread(r"C:\\Users\\riley\\Documents\\townscaper.png")#the letter r ensures that the filepath can be read on windows, using skimage b/c problems with opencv
image_hsv = cv.cvtColor(image_input, cv.COLOR_BGR2HSV)#color conversion

lower_bound = np.array([27, 10, 10])#selecting for yellow values, needs refinement. HSV in opencv is 0-179,0-255,0-255   
upper_bound = np.array([33, 255, 255])

mask = cv.inRange(image_hsv, lower_bound, upper_bound)#binary image of pixels with yellow values, black is no yellow, white is yellow

result = cv.bitwise_and(image_hsv, image_hsv, mask = mask)#combines the image with the mask to cut out all the errors from hsv conversion

cv.namedWindow("Display window", cv.WINDOW_NORMAL)#displays all the created images
cv.namedWindow('Mask', cv.WINDOW_NORMAL)
cv.namedWindow('Result', cv.WINDOW_NORMAL)
cv.imshow("Display window", image_hsv)
cv.imshow('Mask', mask)
cv.imshow('Result', result)

cv.waitKey(0)
cv.destroyAllWindows()#pressing any key closes all the windows, waits indefinitely 
