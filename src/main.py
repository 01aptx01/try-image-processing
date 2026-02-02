import cv2
from scanner import scanned_document

result = scanned_document("images/input/image.png")

cv2.imwrite("images/output/scanned.png", result)
cv2.imshow("Scanned Document", result)
cv2.waitKey(0)
