import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('image.png')

def  support(template,img_rgb) :
    w, h = template.shape[::-1]
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    f = set()

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        sensitivity = 100
        f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

    cv2.imwrite('res1.png',img_rgb)

    found_count = len(f)

    return found_count

def all_support(img_rgb) :
    template = cv2.imread('tr.png', 0)
    template1 = cv2.imread('tr1.png', 0)
    template2 = cv2.imread('tr2.png', 0)
    i=0
    i = support(template, img_rgb)
    i = i+support(template1, img_rgb)
    i = i+support(template2, img_rgb)


    return i;

print(all_support( img_rgb))