
def getLines(image):
    image = cv2.bitwise_not(image)
    kernel0 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 4))
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 5))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    pro1 = cv2.erode(image, kernel1, iterations=1)
    pro2 = cv2.erode(pro1, kernel0, iterations=1)
    pro3 = cv2.dilate(pro2, kernel2, iterations=1)

    cv2.imshow("after dialte/erode image", pro3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    newimage = image - pro3
    #    newimage = cv2.morphologyEx(newimage, cv2.MORPH_OPEN, kernel0)

    cv2.imshow("new image", newimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    ret, thresh = cv2.threshold(newimage, 127, 255, 1)
    contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    x2 = len(contours)

    test_image = cv2.imread('ha5a.jpg', 1)
    i = 1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if (area > 1000):
            continue
        print(area)
        cv2.drawContours(test_image, cnt, -1, (0, 255, 0), 2)
        x, y, w, h = cv2.boundingRect(cnt)
        # cv2.rectangle(test_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        LineNum = "line" + str(i)
        i = i + 1
        cv2.putText(test_image, LineNum, (x + w / 2, y + h / 2), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0),
                    lineType=cv2.LINE_AA)

    cv2.imshow('pic', test_image)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # cv2.drawContours(test_image, contours, -1, (255,0,0), 5)

    return (x2 - 1)


no_of_lines = getLines(thresh1)
print(no_of_lines)
