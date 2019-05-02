
###############################################################
import cv2
import numpy as np
import sys
############################# Preprocessing part ##################################################

imagee = cv2.imread(sys.argv[1], 1)
print(imagee)
print('Original Dimensions : ',imagee.shape)
scale_percent = 20 # percent of original size
width = int(imagee.shape[1] * scale_percent / 100)
height = int(imagee.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(imagee, dim, interpolation=cv2.INTER_AREA)

#noise elimination
kernel = np.ones((2, 2), np.uint8)  # kernel for erosion
erosion = cv2.erode(image, kernel, iterations=1)  # increase black area
t = cv2.fastNlMeansDenoising(erosion, None, 20, 21, 7)  # remove some noise and bluring

# img to binary
image = cv2.medianBlur(image,5)
ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

print('Resized Dimensions : ', image.shape)
cv2.imwrite("after_pre2.jpg", image)


print(sys.argv[1])
sys.stdout.flush()
