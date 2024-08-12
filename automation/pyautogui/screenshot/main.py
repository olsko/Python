import cv2 as cv
import numpy as np


img_rgb = cv.imread(r'original.png')
# the cropped image, expected to be smaller
target_img = cv.imread(r'logo.png') 

_, w, h = target_img.shape[::-1]
res = cv.matchTemplate(img_rgb,target_img,cv.TM_CCOEFF_NORMED)

# with the method used, the date in res are top left pixel coords
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)    
top_left = max_loc

# if we add to it the width and height of the target, then we get the bbox.
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img_rgb,top_left, bottom_right, 255, 2)
cv.imshow('', img_rgb)