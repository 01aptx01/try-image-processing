import cv2

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img):
    return cv2.GaussianBlur(img, (5,5), 0)

def threshold(img):
    _, th = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    return th
