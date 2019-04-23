def getLines(image):
    image = cv2.bitwise_not(image)
    kernel0 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 4))
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    pro1 = cv2.erode(image, kernel1, iterations=1)
    pro2 = cv2.erode(pro1, kernel0, iterations=1)
    pro3 = cv2.dilate(pro2, kernel2, iterations=1)

    #cv2.imshow("after dialte/erode image", pro3)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    newimage = image - pro3
    newimage = cv2.morphologyEx(newimage, cv2.MORPH_OPEN, kernel0)

    #cv2.imshow("new image", newimage)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    ret, thresh = cv2.threshold(newimage, 127, 255, 1)
    contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x2 = len(contours)

    return (x2 - 1)
