import cv2
from preprocessing import to_gray, blur, threshold

def scanned_document(image_path):
    img = cv2.imread(image_path)
    gray = to_gray(img)
    blurred = blur(gray)
    scanned = threshold(blurred)
    return scanned