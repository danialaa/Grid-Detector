import cv2

class RectangleDetector:
    def __init__(self):
        pass
    
    def detect(self, contour):
        shape = "Unknown"
        perimeter = cv2.arcLength(contour, True)
        approximate = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        
        if len(approximate) == 4:
            shape = "Rectangle"
        
        return shape