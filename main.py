# Import required libraries to convert image
import cv2

# Load the image img1 from the directory
filename = 'img1.jpg'
img = cv2.imread(filename)

# Convert  normal image into gray_scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the image in the file format in the directory
cv2.imwrite('gray.png', gray_img)