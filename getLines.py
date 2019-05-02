
def getLines(image):
    (thresh, im_bw) = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    im_bw = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]

    image = cv2.bitwise_not(im_bw)
    kernel0 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 4))
    kernel1 = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    pro1 = cv2.erode(image, kernel1, iterations=1)
    pro2 = cv2.erode(pro1, kernel0, iterations=1)
    pro3 = cv2.dilate(pro2, kernel2, iterations=1)

    cv2.imshow("after dialte/erode image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("after dialte/erode image", pro2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("after dialte/erode i mage", pro3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    newimage = image - pro3
    # newimage = cv2.morphologyEx(newimage, cv2.MORPH_OPEN, kernel0)

    cv2.imshow("new image", newimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ret, thresh = cv2.threshold(newimage, 127, 255, 1)
    new=cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY);
    contours, h = cv2.findContours(new, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x2 = len(contours)

    #test_image = cv2.imread('whiteBG.jpg', 1)
    i = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > 1000):
            continue
        print(area)
        #cv2.drawContours(newimage, cnt, -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(newimage, (x, y), (x + w, y + h), (100, 255, 100), 2)
        LineNum = "line" + str(i)
        i = i + 1
        cv2.putText(newimage, LineNum, (x + w / 2, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100 , 255,100),
                    lineType=cv2.LINE_AA)

    cv2.imshow('pic', newimage)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # cv2.drawContours(test_image, contours, -1, (255,0,0), 5)

    return (x2 - 1)
