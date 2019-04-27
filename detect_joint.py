import cv2
import numpy as np
from scipy.stats import itemfreq

frame1=cv2.imread('truss18.jpg')
gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray ,(23,23), 11)
circles = cv2.HoughCircles(
    img,
    cv2.HOUGH_GRADIENT,
    1,
    minDist=50,
    param1=50,
    param2=12,
    minRadius=1,
    maxRadius=30
)
if not circles is None:
        circles = np.uint16(np.around(circles))
for i in circles[0,:]:
   # draw the outer circle
   cv2.circle(frame1,(i[0],i[1]),i[2],(255,0,0),2)
cv2.imshow("detect joint",frame1)
print(circles.shape[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
