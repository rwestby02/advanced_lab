import numpy as np #images are stored as arrays
import cv2 as cv #image processing
from matplotlib import pyplot as plt #histograms
from skimage import io #for importing images
from skimage.util import img_as_ubyte #for importing images and proper interfacing with opencv

image_read = io.imread(r"filepath")#the letter r ensures that the filepath can be read on windows, using skimage b/c problems with opencv
image_input = img_as_ubyte(image_read)
image_rgb = cv.cvtColor(image_input, cv.COLOR_BGR2RGB)
image_hsv = cv.cvtColor(image_input, cv.COLOR_BGR2HSV) #color conversion


lower_bound = np.array([88, 40, 25]) #selecting for yellow values, needs refinement. HSV in opencv is 0-179,0-255,0-255. yellow about 85 - 95   
upper_bound = np.array([97, 254, 254])

mask = cv.inRange(image_hsv, lower_bound, upper_bound) #binary image of pixels with yellow values, black is no yellow, white is yellow

result = cv.bitwise_and(image_rgb, image_rgb, mask = mask) #combines the image with the mask to cut out all the errors from hsv conversion

gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY) #makes grayscale image of yellow pixels

yellow_intensity = np.sum(gray) #yellow intensity as measured by amount of yellow, not scaled for image size


cv.imwrite("mask.jpg", mask) #saves result images for debugging
cv.imwrite("result.jpg", result)
cv.imwrite("gray.jpg", gray)

  #displays all the created images, for debugging
#cv.namedWindow('Mask', cv.WINDOW_NORMAL)
#cv.namedWindow('Result', cv.WINDOW_NORMAL)
#cv.namedWindow('Input', cv.WINDOW_NORMAL)
#cv.namedWindow('Gray', cv.WINDOW_NORMAL)
#cv.imshow('Input', image_rgb)
#cv.imshow('Mask', mask)
#cv.imshow('Result', result)
#cv.imshow('Gray', gray)


print(yellow_intensity) #prints the yellow intensity value
#plt.hist(result.ravel(),256,[1,254]); plt.show() #2d yellow historgram


#cv.waitKey(0)
#cv.destroyAllWindows() #pressing any key closes all the windows, waits indefinitely 
