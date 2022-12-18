import numpy as np
import cv2

def nothing(x):
    pass

#trackbars (for testing purposes only)
#cv2.namedWindow("Trackbar")
#cv2.createTrackbar("dp", "Trackbar", 1, 10, nothing)
#cv2.createTrackbar("minDist", "Trackbar",10, 200, nothing)
#cv2.createTrackbar("param1", "Trackbar", 0, 255, nothing)
#cv2.createTrackbar("param2", "Trackbar", 0, 255, nothing)
#cv2.createTrackbar("minRadius", "Trackbar", 20, 255, nothing)
#cv2.createTrackbar("maxRadius", "Trackbar", 20, 255, nothing)

#resizing image
def resize_image(image):
    width = int(image.shape[1] * 0.15)
    height = int(image.shape[0] * 0.15)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return image

while True:

    img = cv2.imread('C:/Users/quinn/Project-Change/Coins/all_coins2.jpg',cv2.IMREAD_GRAYSCALE)
    original_image = cv2.imread('C:/Users/quinn/Project-Change/Coins/all_coins2.jpg',1)

    img = resize_image(img)
    original_image = resize_image(original_image)

    #trackbars (for testing purposes only)
    #thresh1 = cv2.getTrackbarPos("dp", "Trackbar")
    #thresh2 = cv2.getTrackbarPos("minDist", "Trackbar")
    #thresh3 = cv2.getTrackbarPos("param1", "Trackbar")
    #thresh4 = cv2.getTrackbarPos("param2", "Trackbar")
    #thresh5 = cv2.getTrackbarPos("minRadius", "Trackbar")
    #thresh6 = cv2.getTrackbarPos("maxRadius", "Trackbar")

    #add blur
    img = cv2.GaussianBlur(img, (5,5), 0)

    #detect circles
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,thresh1,thresh2,param1=thresh3,param2=thresh4,minRadius=thresh5, maxRadius=thresh6)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,75,param1=50,param2=27,minRadius=20,maxRadius=50)
    print(circles)

    circles = np.uint16(np.around(circles))
    count = 1
    for i in circles[0,:]:
        
        # draw the outer circle
        cv2.circle(original_image,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(original_image,(i[0],i[1]),2,(0,0,255),3)
        cv2.putText(original_image, str(count),(i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)
        count += 1

    #show images
    cv2.imshow('Detected Coins', original_image)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
