# Aim: stamp an image with its file name
# Hint: can be run in a loop

import os
import cv2
from PIL import Image

# set up the folder paths and the filename
path = 
file =
photos_stamped_folder = 

im = Image.open(os.path.join(path, file))  
   
# im.size includes the height and width of image 
width, height = im.size    
#print(width, height) 
  
# save the resized file
outfile = photos_stamped_folder + '\\' + os.path.basename(file)
imResize.save( outfile, 'JPEG', quality = 95) # setting quality
        
# add text
img = cv2.imread(outfile)
# Using syntax from https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
# org 
org = (0, 0, 255) 
# fontScale 
fontScale = 1
# Blue color in BGR 
color = (255, 153, 204) 
# Line thickness of 2 px 
thickness = 2
img_text = str(os.path.basename(file)) # the filename is the text to be added to the image
y_axis = height - 20
cv2.putText(img, img_text, (5, y_axis), font, fontScale, color, thickness, cv2.LINE_AA)
cv2.imwrite(outfile, img)
