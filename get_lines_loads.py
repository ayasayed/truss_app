import numpy as np
import cv2

def list_to_points(v_loads ,h_loads):
    #get points of loads
    v=[]
    vv=[]
    h=[]
    hh=[]
    for load in v_loads :
        x, y, w, ha = cv2.boundingRect(load)
        vv=[x,y]
        v.append(vv)
    #print(v)    
    for load in h_loads :
        x, y, w, ha = cv2.boundingRect(load)
        hh=[x,y]
        h.append(hh)
    #print(h)
    
    return v,h

def get_lines_loads(image):
    #preprocessing
    (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    im_bw = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    image = cv2.bitwise_not(im_bw)
    #erode and dilate kernels
    kernel0 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 4))
    kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    
    #erosion and dilation  to get image with lines only
    pro1 = cv2.erode(image, kernel1, iterations=1)
    pro2 = cv2.erode(pro1, kernel0, iterations=1)
    pro3 = cv2.erode(pro2, kernel0, iterations=1)
    pro4 = cv2.dilate(pro3 , kernel2, iterations=1)
    newimage = image - pro4
    '''
    cv2.imshow("new image", newimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    # lines and loads lists
    lines=[]
    v_loads=[]
    h_loads=[]
    
    #lines & loads contours
    ret, thresh = cv2.threshold(newimage, 127, 255, 1)
    new=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY);
    contours, h = cv2.findContours(new, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    
    cv2.imshow("new image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #remove max contour 
    largest_areas = sorted(contours, key=cv2.contourArea)
    contours=contours[1:]
    #print(len(contours))
    
    # classification of lines and loads
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if (area < 200) :
            x, y, w, h = cv2.boundingRect(cnt)
            if (h>w):
                h_loads.append(cnt)
            else:
                v_loads.append(cnt)
        else :
            lines.append(cnt)
    '''
    print(len(v_loads))
    print(len(h_loads))
    print(len(lines))
    '''
    v , h =list_to_points(v_loads , h_loads)
    return v,h


    
img = cv2.imread('101.jpg')
#imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img = getLines(img)
