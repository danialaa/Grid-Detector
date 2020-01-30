import cv2
import numpy as np


cam = cv2.VideoCapture(0)

while True:
    ret_val, img = cam.read()
    img = cv2.flip(img, 1)
    #cv2.imshow('Detector', img)
    if cv2.waitKey(1) == 27: 
        break  # esc to quit


    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ratio = img.shape[0] / float(img.shape[0])
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    
    mask = np.zeros((grey.shape), np.uint8)

    


    maxArea = 0
    c = 0
    pos = 0

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
    
        if area > 1000:
            if area > maxArea:
                maxArea = area
                maxContour = contour
                pos = c
                img = cv2.drawContours(grey, contours, c, (0, 255, 0), 3)
    
        c += 1

    #cv2.drawContours(mask, [maxContour], 0, 255, -1)
    #cv2.drawContours(mask, [maxContour], 0, 0, 2)
    out = np.zeros_like(grey)
    out[mask == 255] = grey[mask == 255]
    blur = cv2.GaussianBlur(out, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
        
    contours2, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    c = 0

    for contour in contours2:
        area = cv2.contourArea(contour)
    
        if area > 500:
            cv2.drawContours(img, contours2, c, (0, 255, 0), 3)
            print(c)
            cv2.imshow("Detector", img)
            cv2.waitKey(0)
            break
        c += 1

    cv2.imshow('Detector', img)
    #cv2.imshow('Gray', grey)
    #cv2.imshow('mask', mask)



cam.release()
cv2.destroyAllWindows()

if __name__ == '__main__':
    main()