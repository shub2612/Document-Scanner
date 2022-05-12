import numpy as np
import cv2
from imutils.perspective import four_point_transform

# ISO 216, 300 dpi
width = 2480
height = 3508

# pre-processing
doc = cv2.imread("doc.jpeg")  # original image
scale = cv2.resize(doc, (width, height))  # resized
copy = scale.copy()
gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)  # convert to grayscale
blur = cv2.GaussianBlur(gray, (7, 7), 0)  # gaussian blur
can = cv2.Canny(blur, 50, 250)  # edge detection

# processing
contours, _ = cv2.findContours(can, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  # finding contours
sort = sorted(contours, key=cv2.contourArea, reverse=True)  # sorting by area
peri = cv2.arcLength(sort[0], True)  # getting perimeter of document contour
approx = cv2.approxPolyDP(sort[0], 0.06 * peri, True)  # getting 4 corners

# warp perspective
a4 = np.float32(np.array([[0, 0], [0, height], [width, height],
                          [width, 0]]))  # corners of output image
corners = np.float32(approx)
perspectiveMatrix = cv2.getPerspectiveTransform(corners, a4)  # generating perspective matrix
warped = cv2.warpPerspective(scale, perspectiveMatrix, (width, height))  # creating bird-eye view

# 4 point transform
# warped = four_point_transform(scale, approx.reshape(4,2))
# warped = cv2.resize(warped, (2480, 3508))


# post-processing
b_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)  # converting to grayscale
b_blur = cv2.medianBlur(b_gray, 5)  # reducing noise
binary = cv2.adaptiveThreshold(b_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)  # converting to binary
cv2.imwrite('final12.jpg', binary)  # exporting final output
