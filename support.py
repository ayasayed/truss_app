
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread('trus3.jpg')

def detectSupport(img_rgb):
  template1 = cv2.imread('tr.png', 0)
  template = cv2.imread('tr1.png', 0)
  template2 = cv2.imread('tr2.png', 0)
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
  w, h = template.shape[::-1]
  res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

  threshold = 0.8
  loc = np.where( res >= threshold)



  for pt in zip(*loc[::-1]):
       cv2.rectangle(img_rgb,pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

  ##
  w, h = template1.shape[::-1]

  res = cv2.matchTemplate(img_gray, template1, cv2.TM_CCOEFF_NORMED)
  threshold = 0.8
  loc = np.where(res >= threshold)


  for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
  ##
  w, h = template2.shape[::-1]
  res = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
  threshold = 0.8
  loc = np.where(res >= threshold)


  for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

  cv2.imshow('Detected',img_rgb)
  plt.imshow(img_rgb)
  plt.show()
  cv2.waitKey(0)
  cv2.destroyAllWindows()

detectSupport(img_rgb)
