import cv2
import numpy as np
############################# Preprocessing part ################################################## 
imagee = cv2.imread('1.jpg', 1)
imagee = cv2.cvtColor(imagee, cv2.COLOR_BGR2GRAY)

width = int(800)
height = int(400)
dim = (width, height)

# resize image
image = cv2.resize(imagee, dim, interpolation=cv2.INTER_AREA)

#noise elimination
kernel = np.ones((2, 2), np.uint8)  # kernel for erosion
erosion = cv2.erode(image, kernel, iterations=1)  # increase black area
t = cv2.fastNlMeansDenoising(erosion, None, 20, 21, 7)  # remove some noise and bluring

# img to binary 
image = cv2.medianBlur(image,5)
ret,image = cv2.threshold(image,115,255,cv2.THRESH_BINARY)



print('Resized Dimensions : ', image.shape)
cv2.imshow("Resized image", image)
#cv2.imwrite('11.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
