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
    

    cv2.imshow("new image", newimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # lines and loads lists
    lines=[]
    v_loads=[]
    h_loads=[]
    
    #lines & loads contours
    ret, thresh = cv2.threshold(newimage, 127, 255, 1)
    new=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY);
    contours, h = cv2.findContours(new, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for c in contours :
        print(cv2.contourArea(c))
        if cv2.contourArea(c) < 50 :
           contours.remove(c)
    #remove max contour
    largest_areas = sorted(contours, key=cv2.contourArea)
    contours=contours[1:]
    '''
    for i in contours :
        print( cv2.contourArea(i))
        cv2.drawContours(image, i, -1, (0,255,0), 3)
        cv2.imshow("new image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    '''
    cv2.drawContours(image, contours, -1, (0,255,0), 3)
    print(len(contours))
    cv2.imshow("new image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
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
    
    print(len(v_loads))
    print(len(h_loads))
    print(len(lines))
    #print(image.shape[0])
    imgg = np.zeros((image.shape[0],image.shape[1],3), np.uint8)#for sub =img_rgb -img2
    img2=cv2.bitwise_not(imgg)

    for vl in v_loads:
        x, y, w, h = cv2.boundingRect(vl)
        cv2.circle(img2,(x,y), 3*w , (0,0,0), -1)
    for hl in h_loads:
        x, y, w, h = cv2.boundingRect(hl)
        cv2.circle(img2,(x,y), 3*h , (0,0,0), -1)
    img2 = cv2.bitwise_not(img2)
    
    i =cv2.bitwise_not(im_bw) - img2
    i = cv2.bitwise_not(i)
    cv2.imshow("new image",i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    v , h =list_to_points(v_loads , h_loads)
    return i,v,h
