import cv2

class SquareDetector:
    def __init__(self):
        pass

    def detect(self, contour):
        shape = "unknown"
        perimeter = cv2.arcLength(contour, True)
        approximate = cv2.approxPolyDP(c, 0.04 * perimeter, True)

        if len(approximate) == 4:
            (x, y, w, h) = cv2.boundingRect(approximate)
            aspectRatio = w / float(h)

            if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                shape = "square"

        return shape

