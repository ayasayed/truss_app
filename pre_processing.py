def pre (image):
    dim = (800,400)

    # resize image
    #image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    #noise elimination
    kernel = np.ones((2, 2), np.uint8)  # kernel for erosion
    erosion = cv2.erode(image, kernel, iterations=1)  # increase black area
    t = cv2.fastNlMeansDenoising(erosion, None, 20, 21, 7)  # remove some noise and bluring

    # img to binary 
    image = cv2.medianBlur(t,5)
    ret,image = cv2.threshold(image,115,255,cv2.THRESH_BINARY)

    return image
